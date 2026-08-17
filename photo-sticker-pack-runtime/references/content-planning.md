# Content Planning

Plan the complete pack before any generation. Choose the visual protagonist automatically when a photo has multiple people: favor the most prominent, central, clearly visible person. Keep every item anchored in that person's visible profile and only use plainly visible accessories or direct, unambiguous scene cues.

## Required ordered kinds

1. `character_accessory`
2. `character_accessory`
3. `character_accessory`
4. `character_accessory_text`
5. `character_accessory_text`
6. `accessory_text`
7. `accessory_text`
8. `character_expression`

Use no caption for `character_accessory` or `character_expression`. For text kinds, use the situational-caption recipe below. Default all four text items to English-only copy with 2–4 uppercase English words each. Change language only when the user explicitly requests another language.

## Situational-caption recipe

1. Name the visible cue.
2. Convert it into a situational reaction, mood, or action consequence.
3. Compress the result to 2–4 uppercase English words by default.
4. Reject a literal object label such as “这是墨镜” or “黑色包包”.
5. Reserve integrated negative space beside the artwork and keep the caption to at most two lines.

The caption must react to the cue rather than merely identify it. Plan the integrated negative space before generation, while the image_gen artwork remains text-free and local post-processing places the copy.

Before saving, normalize whitespace/case and check that no caption, action, or action+accessory combination repeats. The exact ordered kind sequence is binding, not only the 3/2/2/1 counts. Derive each caption's joke from a visible accessory, expression, clothing cue, or direct scene context; rotate poses and emotional beats. Avoid inventing words visible in the photograph, brands, relationship claims, or personal facts.

Pass an input object with exactly the `new_manifest` inputs below. Its item objects use the planning fields that `new_manifest` preserves before adding output paths and state.

```json
{
  "source_path": "/absolute/path/to/photo.jpg",
  "subject": {
    "visible_features": ["short dark hair", "round glasses", "light overshirt"],
    "protagonist_reason": "largest clearly visible person"
  },
  "items": [
    {"id": 1, "kind": "character_accessory", "action": "raises a takeaway cup", "accessory": "takeaway cup", "expression": "calm smile", "caption": "", "prompt": "visible profile holding one cup"},
    {"id": 2, "kind": "character_accessory", "action": "adjusts round glasses", "accessory": "round glasses", "expression": "confident", "caption": "", "prompt": "visible profile adjusting glasses"},
    {"id": 3, "kind": "character_accessory", "action": "checks a phone", "accessory": "phone", "expression": "focused", "caption": "", "prompt": "visible profile holding one phone"},
    {"id": 4, "kind": "character_accessory_text", "action": "takes a coffee sip", "accessory": "takeaway cup", "expression": "content", "caption": "SIP HAPPENS", "prompt": "visible profile sipping one cup"},
    {"id": 5, "kind": "character_accessory_text", "action": "gives a thumbs-up", "accessory": "round glasses", "expression": "bright", "caption": "LOOKING SHARP", "prompt": "visible profile with glasses giving a thumbs-up"},
    {"id": 6, "kind": "accessory_text", "action": "rests upright", "accessory": "takeaway cup", "expression": "", "caption": "FUEL FIRST", "prompt": "one visible-style takeaway cup only"},
    {"id": 7, "kind": "accessory_text", "action": "waits for attention", "accessory": "round glasses", "expression": "", "caption": "MAIN CHARACTER", "prompt": "one visible-style pair of round glasses only"},
    {"id": 8, "kind": "character_expression", "action": "looks pleasantly surprised", "accessory": "", "expression": "pleasant surprise", "caption": "", "prompt": "visible profile close expression only"}
  ]
}
```

Replace the illustrative accessories and actions with only cues visible in the actual photo. The final prompt for a text kind must still request no model-rendered text; local post-processing renders the caption.
