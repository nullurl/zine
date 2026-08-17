import AppKit
import Carbon.HIToolbox
import CoreGraphics
import Darwin
import Foundation

private enum StickerDeskError: LocalizedError {
    case invalid(String)

    var errorDescription: String? {
        switch self {
        case .invalid(let message):
            return message
        }
    }
}

private struct Manifest: Decodable {
    let items: [ManifestItem]
}

private struct ManifestItem: Decodable {
    let id: Int
    let pngPath: String
    let status: String

    enum CodingKeys: String, CodingKey {
        case id
        case pngPath = "png_path"
        case status
    }
}

private struct StickerRequest {
    let sourceURL: URL
    let packURL: URL
    let itemID: Int
    let colorHex: String
    let assetURL: URL
}

private func oneQueryValue(_ components: URLComponents, name: String) throws -> String {
    let values = (components.queryItems ?? []).filter { $0.name == name }.compactMap(\.value)
    guard values.count == 1, let value = values.first, !value.isEmpty else {
        throw StickerDeskError.invalid("missing or repeated \(name)")
    }
    return value
}

private func isSafeRelativePath(_ path: String) -> Bool {
    if path.isEmpty || NSString(string: path).isAbsolutePath || path.contains("\\") {
        return false
    }
    let components = path.split(separator: "/", omittingEmptySubsequences: false)
    return !components.contains { $0.isEmpty || $0 == "." || $0 == ".." }
}

private func resolvedRegularFile(_ url: URL, maximumBytes: Int) throws -> URL {
    let standardized = url.standardizedFileURL
    let resolved = standardized.resolvingSymlinksInPath()
    guard resolved.path == standardized.path else {
        throw StickerDeskError.invalid("symbolic links are not allowed")
    }
    let values = try resolved.resourceValues(
        forKeys: [.isRegularFileKey, .isSymbolicLinkKey, .fileSizeKey]
    )
    guard values.isRegularFile == true, values.isSymbolicLink != true else {
        throw StickerDeskError.invalid("expected a regular file")
    }
    guard let size = values.fileSize, size > 0, size <= maximumBytes else {
        throw StickerDeskError.invalid("file size is outside the allowed range")
    }
    return resolved
}

private func parseStickerRequest(_ text: String) throws -> StickerRequest {
    guard text.utf8.count <= 16_384,
          let components = URLComponents(string: text),
          components.scheme?.lowercased() == "photosticker",
          components.host?.lowercased() == "add",
          components.path.isEmpty
    else {
        throw StickerDeskError.invalid("unsupported desktop sticker URL")
    }

    let allowedNames = Set(["pack", "id", "color"])
    guard (components.queryItems ?? []).allSatisfy({ allowedNames.contains($0.name) }) else {
        throw StickerDeskError.invalid("unexpected desktop sticker parameter")
    }

    let packPath = try oneQueryValue(components, name: "pack")
    guard packPath.utf8.count <= 4_096, NSString(string: packPath).isAbsolutePath else {
        throw StickerDeskError.invalid("pack must be an absolute local path")
    }
    let itemText = try oneQueryValue(components, name: "id")
    let colorText = try oneQueryValue(components, name: "color").uppercased()
    guard let itemID = Int(itemText), (1...8).contains(itemID) else {
        throw StickerDeskError.invalid("item id must be between 1 and 8")
    }
    guard colorText.count == 6,
          colorText.unicodeScalars.allSatisfy({
              CharacterSet(charactersIn: "0123456789ABCDEF").contains($0)
          })
    else {
        throw StickerDeskError.invalid("color must be a six-digit hex value")
    }

    let requestedPack = URL(fileURLWithPath: packPath, isDirectory: true).standardizedFileURL
    let packURL = requestedPack.resolvingSymlinksInPath()
    guard requestedPack.path == packURL.path else {
        throw StickerDeskError.invalid("pack path may not contain symbolic links")
    }
    let packValues = try packURL.resourceValues(forKeys: [.isDirectoryKey, .isSymbolicLinkKey])
    guard packValues.isDirectory == true, packValues.isSymbolicLink != true else {
        throw StickerDeskError.invalid("pack directory is unavailable")
    }

    let manifestURL = try resolvedRegularFile(
        packURL.appendingPathComponent("manifest.json"),
        maximumBytes: 1_048_576
    )
    let manifest = try JSONDecoder().decode(Manifest.self, from: Data(contentsOf: manifestURL))
    guard let item = manifest.items.first(where: { $0.id == itemID }),
          item.status == "complete",
          isSafeRelativePath(item.pngPath)
    else {
        throw StickerDeskError.invalid("manifest item is unavailable")
    }

    let assetURL = try resolvedRegularFile(
        packURL.appendingPathComponent(item.pngPath),
        maximumBytes: 25 * 1_048_576
    )
    let packPrefix = packURL.path.hasSuffix("/") ? packURL.path : packURL.path + "/"
    guard assetURL.path.hasPrefix(packPrefix), assetURL.pathExtension.lowercased() == "png" else {
        throw StickerDeskError.invalid("asset must be a manifest-backed PNG inside the pack")
    }
    guard NSImage(contentsOf: assetURL) != nil else {
        throw StickerDeskError.invalid("asset PNG is unreadable")
    }

    guard let sourceURL = components.url else {
        throw StickerDeskError.invalid("desktop sticker URL is malformed")
    }
    return StickerRequest(
        sourceURL: sourceURL,
        packURL: packURL,
        itemID: itemID,
        colorHex: colorText,
        assetURL: assetURL
    )
}

private func colorComponents(_ hex: String) throws -> (UInt8, UInt8, UInt8) {
    guard let value = UInt32(hex, radix: 16) else {
        throw StickerDeskError.invalid("invalid color")
    }
    return (
        UInt8((value >> 16) & 0xff),
        UInt8((value >> 8) & 0xff),
        UInt8(value & 0xff)
    )
}

private func recoloredImage(for request: StickerRequest) throws -> NSImage {
    guard let source = NSImage(contentsOf: request.assetURL) else {
        throw StickerDeskError.invalid("asset PNG is unreadable")
    }
    var proposed = NSRect(origin: .zero, size: source.size)
    guard let input = source.cgImage(forProposedRect: &proposed, context: nil, hints: nil) else {
        throw StickerDeskError.invalid("asset PNG cannot be decoded")
    }
    let width = input.width
    let height = input.height
    guard width > 0, height > 0, width <= 4096, height <= 4096 else {
        throw StickerDeskError.invalid("asset dimensions are invalid")
    }
    var pixels = [UInt8](repeating: 0, count: width * height * 4)
    let space = CGColorSpaceCreateDeviceRGB()
    let bitmapInfo = CGBitmapInfo.byteOrder32Big.rawValue
        | CGImageAlphaInfo.premultipliedLast.rawValue
    guard let context = CGContext(
        data: &pixels,
        width: width,
        height: height,
        bitsPerComponent: 8,
        bytesPerRow: width * 4,
        space: space,
        bitmapInfo: bitmapInfo
    ) else {
        throw StickerDeskError.invalid("cannot create image renderer")
    }
    context.interpolationQuality = .high
    context.draw(input, in: CGRect(x: 0, y: 0, width: width, height: height))

    let target = try colorComponents(request.colorHex)
    let sourceBlue = (Double(46), Double(66), Double(155))
    for offset in stride(from: 0, to: pixels.count, by: 4) {
        let alpha = Double(pixels[offset + 3])
        if alpha <= 0 {
            continue
        }
        let scale = 255.0 / alpha
        let red = min(255.0, Double(pixels[offset]) * scale)
        let green = min(255.0, Double(pixels[offset + 1]) * scale)
        let blue = min(255.0, Double(pixels[offset + 2]) * scale)
        let ratios = [
            (255.0 - red) / (255.0 - sourceBlue.0),
            (255.0 - green) / (255.0 - sourceBlue.1),
            (255.0 - blue) / (255.0 - sourceBlue.2),
        ]
        let ink = max(0.0, min(1.0, ratios.reduce(0, +) / Double(ratios.count)))
        let output = (
            255.0 * (1.0 - ink) + Double(target.0) * ink,
            255.0 * (1.0 - ink) + Double(target.1) * ink,
            255.0 * (1.0 - ink) + Double(target.2) * ink
        )
        pixels[offset] = UInt8(max(0, min(255, output.0 * alpha / 255.0)).rounded())
        pixels[offset + 1] = UInt8(max(0, min(255, output.1 * alpha / 255.0)).rounded())
        pixels[offset + 2] = UInt8(max(0, min(255, output.2 * alpha / 255.0)).rounded())
    }
    guard let output = context.makeImage() else {
        throw StickerDeskError.invalid("cannot create recolored sticker")
    }
    return NSImage(cgImage: output, size: NSSize(width: width, height: height))
}

private struct SavedFrame: Codable {
    var x: Double
    var y: Double
    var width: Double
    var height: Double
}

private struct SavedSticker: Codable {
    var uuid: UUID
    var requestURL: String
    var frame: SavedFrame
    var rotation: Double
    var floating: Bool
}

private protocol StickerViewController: AnyObject {
    func removeSticker(_ id: UUID)
    func toggleFloating(_ id: UUID)
    func resizeSticker(_ id: UUID, factor: CGFloat)
    func rotateSticker(_ id: UUID, degrees: CGFloat)
}

private final class StickerView: NSView {
    let stickerID: UUID
    let image: NSImage
    var rotation: CGFloat
    weak var controller: StickerViewController?

    init(
        frame: NSRect,
        stickerID: UUID,
        image: NSImage,
        rotation: CGFloat,
        controller: StickerViewController
    ) {
        self.stickerID = stickerID
        self.image = image
        self.rotation = rotation
        self.controller = controller
        super.init(frame: frame)
        wantsLayer = true
        layer?.backgroundColor = NSColor.clear.cgColor
    }

    required init?(coder: NSCoder) {
        nil
    }

    override var mouseDownCanMoveWindow: Bool {
        true
    }

    override func acceptsFirstMouse(for event: NSEvent?) -> Bool {
        true
    }

    override func draw(_ dirtyRect: NSRect) {
        super.draw(dirtyRect)
        NSGraphicsContext.saveGraphicsState()
        let transform = NSAffineTransform()
        transform.translateX(by: bounds.midX, yBy: bounds.midY)
        transform.rotate(byDegrees: rotation)
        transform.translateX(by: -bounds.midX, yBy: -bounds.midY)
        transform.concat()
        image.draw(
            in: bounds.insetBy(dx: 8, dy: 8),
            from: .zero,
            operation: .sourceOver,
            fraction: 1,
            respectFlipped: true,
            hints: [.interpolation: NSImageInterpolation.high]
        )
        NSGraphicsContext.restoreGraphicsState()
    }

    override func scrollWheel(with event: NSEvent) {
        if event.modifierFlags.contains(.option) {
            controller?.rotateSticker(stickerID, degrees: event.scrollingDeltaY >= 0 ? 4 : -4)
        } else {
            controller?.resizeSticker(stickerID, factor: event.scrollingDeltaY >= 0 ? 1.06 : 0.94)
        }
    }

    override func rightMouseDown(with event: NSEvent) {
        let menu = NSMenu()
        let floating = NSMenuItem(
            title: "Toggle Always on Top",
            action: #selector(toggleFloating),
            keyEquivalent: ""
        )
        floating.target = self
        menu.addItem(floating)
        let left = NSMenuItem(title: "Rotate Left", action: #selector(rotateLeft), keyEquivalent: "")
        left.target = self
        menu.addItem(left)
        let right = NSMenuItem(title: "Rotate Right", action: #selector(rotateRight), keyEquivalent: "")
        right.target = self
        menu.addItem(right)
        menu.addItem(.separator())
        let remove = NSMenuItem(title: "Remove Sticker", action: #selector(removeSticker), keyEquivalent: "")
        remove.target = self
        menu.addItem(remove)
        NSMenu.popUpContextMenu(menu, with: event, for: self)
    }

    @objc private func toggleFloating() {
        controller?.toggleFloating(stickerID)
    }

    @objc private func rotateLeft() {
        controller?.rotateSticker(stickerID, degrees: -15)
    }

    @objc private func rotateRight() {
        controller?.rotateSticker(stickerID, degrees: 15)
    }

    @objc private func removeSticker() {
        controller?.removeSticker(stickerID)
    }
}

private final class StickerPanel: NSPanel {
    let stickerID: UUID

    init(stickerID: UUID, frame: NSRect) {
        self.stickerID = stickerID
        super.init(
            contentRect: frame,
            styleMask: [.borderless],
            backing: .buffered,
            defer: false
        )
        isOpaque = false
        backgroundColor = .clear
        hasShadow = false
        hidesOnDeactivate = false
        isMovableByWindowBackground = true
        collectionBehavior = [.canJoinAllSpaces, .stationary, .ignoresCycle]
    }

    override var canBecomeKey: Bool {
        false
    }

    override var canBecomeMain: Bool {
        false
    }
}

private final class AppDelegate: NSObject, NSApplicationDelegate, NSWindowDelegate,
    StickerViewController
{
    private var saved: [UUID: SavedSticker] = [:]
    private var panels: [UUID: StickerPanel] = [:]
    private var statusItem: NSStatusItem?
    private var editMenuItem: NSMenuItem?
    private var welcomeWindow: NSWindow?
    private var editMode = false

    private var stateURL: URL {
        let support = FileManager.default.urls(
            for: .applicationSupportDirectory,
            in: .userDomainMask
        )[0]
        return support.appendingPathComponent("StickerDesk", isDirectory: true)
            .appendingPathComponent("stickers.json")
    }

    func applicationWillFinishLaunching(_ notification: Notification) {
        NSAppleEventManager.shared().setEventHandler(
            self,
            andSelector: #selector(handleGetURLEvent(_:withReplyEvent:)),
            forEventClass: AEEventClass(kInternetEventClass),
            andEventID: AEEventID(kAEGetURL)
        )
    }

    func applicationDidFinishLaunching(_ notification: Notification) {
        NSApp.setActivationPolicy(.accessory)
        configureStatusItem()
        restore()
        showWelcomeIfNeeded()
    }

    func applicationWillTerminate(_ notification: Notification) {
        persist()
        NSAppleEventManager.shared().removeEventHandler(
            forEventClass: AEEventClass(kInternetEventClass),
            andEventID: AEEventID(kAEGetURL)
        )
    }

    @objc private func handleGetURLEvent(
        _ event: NSAppleEventDescriptor,
        withReplyEvent replyEvent: NSAppleEventDescriptor
    ) {
        guard let text = event.paramDescriptor(forKeyword: keyDirectObject)?.stringValue else {
            return
        }
        do {
            try add(request: parseStickerRequest(text))
        } catch {
            NSSound.beep()
            fputs("StickerDesk rejected URL: \(error.localizedDescription)\n", stderr)
        }
    }

    private func configureStatusItem() {
        let item = NSStatusBar.system.statusItem(withLength: NSStatusItem.squareLength)
        item.button?.title = "◈"
        item.button?.toolTip = "StickerDesk"
        let menu = NSMenu()
        let edit = NSMenuItem(
            title: "Edit Desktop Stickers",
            action: #selector(toggleEditMode),
            keyEquivalent: "e"
        )
        edit.target = self
        edit.state = .off
        menu.addItem(edit)
        editMenuItem = edit
        menu.addItem(.separator())
        let show = NSMenuItem(title: "Show Desktop Stickers", action: #selector(showAll), keyEquivalent: "")
        show.target = self
        menu.addItem(show)
        let hide = NSMenuItem(title: "Hide Desktop Stickers", action: #selector(hideAll), keyEquivalent: "")
        hide.target = self
        menu.addItem(hide)
        menu.addItem(.separator())
        let quit = NSMenuItem(title: "Quit StickerDesk", action: #selector(quit), keyEquivalent: "q")
        quit.target = self
        menu.addItem(quit)
        item.menu = menu
        statusItem = item
    }

    private func showWelcomeIfNeeded() {
        let defaults = UserDefaults.standard
        guard !defaults.bool(forKey: "didShowWelcomeV1") else {
            return
        }

        let window = NSWindow(
            contentRect: NSRect(x: 0, y: 0, width: 430, height: 360),
            styleMask: [.titled, .closable],
            backing: .buffered,
            defer: false
        )
        window.title = "StickerDesk"
        window.isReleasedWhenClosed = false
        window.delegate = self

        let content = NSView()
        window.contentView = content

        let icon = NSImageView()
        icon.image = NSImage(
            systemSymbolName: "square.stack.3d.up.fill",
            accessibilityDescription: "StickerDesk"
        )
        icon.contentTintColor = NSColor(
            calibratedRed: 46.0 / 255.0,
            green: 66.0 / 255.0,
            blue: 155.0 / 255.0,
            alpha: 1
        )
        icon.symbolConfiguration = NSImage.SymbolConfiguration(pointSize: 36, weight: .medium)

        let title = NSTextField(labelWithString: "StickerDesk 已启动")
        title.font = .systemFont(ofSize: 23, weight: .semibold)
        title.alignment = .center

        let subtitle = NSTextField(
            wrappingLabelWithString: "现在可以从贴纸画廊把贴纸放到 Mac 桌面。"
        )
        subtitle.textColor = .secondaryLabelColor
        subtitle.font = .systemFont(ofSize: 14)
        subtitle.alignment = .center

        let instructions = NSTextField(
            wrappingLabelWithString:
                "1. 在画廊右上角选择小显示器，再点击贴纸\n"
                + "2. 点击菜单栏 ◈ → Edit Desktop Stickers\n"
                + "3. 拖动移动、滚轮缩放、右键删除"
        )
        instructions.font = .systemFont(ofSize: 14)
        instructions.maximumNumberOfLines = 0
        instructions.preferredMaxLayoutWidth = 340

        let button = NSButton(
            title: "开始使用",
            target: self,
            action: #selector(finishWelcome)
        )
        button.bezelStyle = .rounded
        button.keyEquivalent = "\r"

        let stack = NSStackView(views: [icon, title, subtitle, instructions, button])
        stack.orientation = .vertical
        stack.alignment = .centerX
        stack.spacing = 14
        stack.setCustomSpacing(7, after: title)
        stack.setCustomSpacing(22, after: subtitle)
        stack.setCustomSpacing(24, after: instructions)
        stack.translatesAutoresizingMaskIntoConstraints = false
        content.addSubview(stack)

        NSLayoutConstraint.activate([
            stack.leadingAnchor.constraint(greaterThanOrEqualTo: content.leadingAnchor, constant: 34),
            stack.trailingAnchor.constraint(lessThanOrEqualTo: content.trailingAnchor, constant: -34),
            stack.centerXAnchor.constraint(equalTo: content.centerXAnchor),
            stack.centerYAnchor.constraint(equalTo: content.centerYAnchor),
            instructions.widthAnchor.constraint(equalToConstant: 340),
        ])

        welcomeWindow = window
        window.center()
        window.makeKeyAndOrderFront(nil)
        NSApp.activate(ignoringOtherApps: true)
    }

    @objc private func finishWelcome() {
        UserDefaults.standard.set(true, forKey: "didShowWelcomeV1")
        welcomeWindow?.close()
        welcomeWindow = nil
    }

    private func defaultFrame(for image: NSImage) -> NSRect {
        let visible = NSScreen.main?.visibleFrame ?? NSRect(x: 0, y: 0, width: 1440, height: 900)
        let ratio = max(0.35, min(2.8, image.size.width / max(image.size.height, 1)))
        let width: CGFloat = ratio >= 1 ? 260 : 260 * ratio
        let height: CGFloat = ratio >= 1 ? 260 / ratio : 260
        let offset = CGFloat(panels.count % 6) * 22
        return NSRect(
            x: visible.midX - width / 2 + offset,
            y: visible.midY - height / 2 - offset,
            width: width,
            height: height
        )
    }

    private func add(request: StickerRequest) throws {
        let image = try recoloredImage(for: request)
        let id = UUID()
        let frame = defaultFrame(for: image)
        let record = SavedSticker(
            uuid: id,
            requestURL: request.sourceURL.absoluteString,
            frame: SavedFrame(
                x: frame.origin.x,
                y: frame.origin.y,
                width: frame.width,
                height: frame.height
            ),
            rotation: 0,
            floating: false
        )
        saved[id] = record
        show(record: record, image: image)
        persist()
    }

    private func show(record: SavedSticker, image: NSImage) {
        let frame = NSRect(
            x: record.frame.x,
            y: record.frame.y,
            width: record.frame.width,
            height: record.frame.height
        )
        let panel = StickerPanel(stickerID: record.uuid, frame: frame)
        panel.delegate = self
        setLevel(panel, floating: record.floating)
        let view = StickerView(
            frame: NSRect(origin: .zero, size: frame.size),
            stickerID: record.uuid,
            image: image,
            rotation: CGFloat(record.rotation),
            controller: self
        )
        view.autoresizingMask = [.width, .height]
        panel.contentView = view
        panels[record.uuid] = panel
        panel.orderFrontRegardless()
    }

    private func setLevel(_ panel: StickerPanel, floating: Bool) {
        let elevated = floating || editMode
        panel.ignoresMouseEvents = !elevated
        panel.acceptsMouseMovedEvents = elevated
        panel.hasShadow = elevated
        if elevated {
            panel.level = .floating
            panel.collectionBehavior = [.canJoinAllSpaces, .canJoinAllApplications, .ignoresCycle]
        } else {
            let desktop = CGWindowLevelForKey(.desktopIconWindow) - 1
            panel.level = NSWindow.Level(rawValue: Int(desktop))
            panel.collectionBehavior = [.canJoinAllSpaces, .stationary, .ignoresCycle]
        }
    }

    private func restore() {
        guard let data = try? Data(contentsOf: stateURL),
              let records = try? JSONDecoder().decode([SavedSticker].self, from: data)
        else {
            return
        }
        for record in records {
            do {
                let request = try parseStickerRequest(record.requestURL)
                let image = try recoloredImage(for: request)
                saved[record.uuid] = record
                show(record: record, image: image)
            } catch {
                continue
            }
        }
        persist()
    }

    private func persist() {
        let directory = stateURL.deletingLastPathComponent()
        do {
            try FileManager.default.createDirectory(
                at: directory,
                withIntermediateDirectories: true
            )
            let data = try JSONEncoder().encode(
                saved.values.sorted { $0.uuid.uuidString < $1.uuid.uuidString }
            )
            try data.write(to: stateURL, options: .atomic)
        } catch {
            fputs("StickerDesk could not save state: \(error.localizedDescription)\n", stderr)
        }
    }

    func windowDidMove(_ notification: Notification) {
        updateFrame(from: notification)
    }

    func windowWillClose(_ notification: Notification) {
        guard let closingWindow = notification.object as? NSWindow,
              closingWindow === welcomeWindow
        else {
            return
        }
        UserDefaults.standard.set(true, forKey: "didShowWelcomeV1")
        welcomeWindow = nil
    }

    func windowDidResize(_ notification: Notification) {
        updateFrame(from: notification)
    }

    private func updateFrame(from notification: Notification) {
        guard let panel = notification.object as? StickerPanel,
              var record = saved[panel.stickerID]
        else {
            return
        }
        record.frame = SavedFrame(
            x: panel.frame.origin.x,
            y: panel.frame.origin.y,
            width: panel.frame.width,
            height: panel.frame.height
        )
        saved[panel.stickerID] = record
        persist()
    }

    func removeSticker(_ id: UUID) {
        panels[id]?.orderOut(nil)
        panels[id]?.close()
        panels[id] = nil
        saved[id] = nil
        persist()
    }

    func toggleFloating(_ id: UUID) {
        guard let panel = panels[id], var record = saved[id] else {
            return
        }
        record.floating.toggle()
        saved[id] = record
        setLevel(panel, floating: record.floating)
        panel.orderFrontRegardless()
        persist()
    }

    func resizeSticker(_ id: UUID, factor: CGFloat) {
        guard let panel = panels[id] else {
            return
        }
        let current = panel.frame
        let width = max(96, min(720, current.width * factor))
        let height = max(96, min(720, current.height * factor))
        let frame = NSRect(
            x: current.midX - width / 2,
            y: current.midY - height / 2,
            width: width,
            height: height
        )
        panel.setFrame(frame, display: true, animate: false)
    }

    func rotateSticker(_ id: UUID, degrees: CGFloat) {
        guard let view = panels[id]?.contentView as? StickerView,
              var record = saved[id]
        else {
            return
        }
        record.rotation = (record.rotation + Double(degrees)).truncatingRemainder(dividingBy: 360)
        saved[id] = record
        view.rotation = CGFloat(record.rotation)
        view.needsDisplay = true
        persist()
    }

    @objc private func toggleEditMode() {
        editMode.toggle()
        editMenuItem?.state = editMode ? .on : .off
        editMenuItem?.title = editMode ? "Finish Editing Stickers" : "Edit Desktop Stickers"
        for (id, panel) in panels {
            setLevel(panel, floating: saved[id]?.floating ?? false)
            panel.orderFrontRegardless()
        }
    }

    @objc private func showAll() {
        for panel in panels.values {
            panel.orderFrontRegardless()
        }
    }

    @objc private func hideAll() {
        for panel in panels.values {
            panel.orderOut(nil)
        }
    }

    @objc private func quit() {
        NSApp.terminate(nil)
    }
}

private func runValidationMode() -> Never {
    let arguments = CommandLine.arguments
    do {
        guard arguments.count == 3, arguments[1] == "--validate-url" else {
            throw StickerDeskError.invalid("usage: StickerDesk --validate-url URL")
        }
        let request = try parseStickerRequest(arguments[2])
        print(request.assetURL.path)
        exit(EXIT_SUCCESS)
    } catch {
        fputs("\(error.localizedDescription)\n", stderr)
        exit(EXIT_FAILURE)
    }
}

if CommandLine.arguments.count > 1 {
    runValidationMode()
}

private let application = NSApplication.shared
private let delegate = AppDelegate()
application.delegate = delegate
application.run()
