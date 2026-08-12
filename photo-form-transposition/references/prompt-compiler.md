# Prompt compiler

Use this scaffold to convert the visual decision into a concise tool-ready image-edit prompt. Include only lines relevant to the source.

```text
Use case: style-transfer
Asset type: vertical or square fine-art editorial poster
Input image: Image 1 is the edit target and sole visual-content source.

Source reading:
- Dominant carriers: [two to four photographed structures]
- Direction and mood: [source motion, spatial direction, atmosphere]

Primary request:
Reorganize the photographed carriers into a [target form] through visual transposition. The target should register at [subtle / balanced / assertive] strength while the original photograph remains perceptible.

Recognition anchors:
- [anchor derived from source structure]
- [anchor derived from source structure]
- [anchor derived from source structure]

Environment reconnection:
Keep approximately [range] of the form readable. At [two or three named zones], let [source mist / shadow / water / light / texture] cross, dissolve, or continue beyond the boundary. Carry a faint source-derived echo into the negative space. Keep selected recognition anchors crisp.

Transformation grammar:
Use [one primary device] only where it reinforces [specific source structure]. Optionally add [one supporting treatment].

Composition and mood:
[placement, negative space, background tone, quietness or energy]

Invariants:
Preserve the source's [identity-defining texture, color, light, ridge, shadow, or rhythm]. Use no visual content outside Image 1. Do not add text, logos, frames, or unrelated objects.

Avoid:
hard closed mask, sticker edge, ordinary double exposure, full redraw, realistic illustration, invented anatomy, decorative veins, uniform transparency fade, excessive fragments, unrelated collage, watermark
```

## Compilation rules

- Name concrete source structures instead of abstract style adjectives.
- Express each recognition anchor as a transformation of something already photographed.
- State where the boundary should remain legible and where it should dissolve.
- Repeat invariants on every revision.
- Do not list every possible effect. Select only the chosen grammar.
- Do not name living artists, brands, or copyrighted characters as style targets.

## Targeted revision prompts

Use one of these patterns after inspection:

**Target too weak**

```text
Change only target recognition: strengthen [two missing anchors] using existing [source structures]. Preserve all current environmental bridges. Do not close the full contour.
```

**Result looks clipped**

```text
Change only subject-environment continuity: let [source texture] cross the boundary at [zones], and carry a faint echo into the field. Keep [three anchors] legible. Do not lower the whole subject's opacity.
```

**Result looks illustrated**

```text
Remove invented [veins / feathers / anatomy / outline]. Rebuild those cues only from existing [ridges / shadows / waves / repeated marks]. Preserve photographic texture and depth.
```

**Target choice is forced**

```text
Discard the current target form. Re-evaluate the source geometry and select a less literal form that needs no invented structure while preserving the existing photographic carriers.
```

