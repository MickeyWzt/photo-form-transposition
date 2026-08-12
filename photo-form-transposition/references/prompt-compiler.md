# Prompt compiler

Use this scaffold to convert the visual decision into a concise image-edit prompt. Include only relevant lines.

```text
Use case: style-transfer
Asset type: fine-art editorial poster
Input image: Image 1 is the edit target and sole visual-content source.

Source reading:
- Carrier type: [mass-led / flow-led / topology-led / hybrid]
- Keystone carrier: [source feature and its direction]
- Supporting carriers: [two or three features]
- Mood and depth: [source atmosphere]

Primary request:
Reorganize Image 1 into a [target form] using the [contained / permeable / gestural] architecture at [subtle / balanced / assertive] strength. Preserve the original photograph as the active material.

Carrier-to-form role map:
- [keystone] -> [main target role]
- [carrier 2] -> [secondary role]
- [carrier 3] -> [boundary, rhythm, depth, or trailing role]

Recognition anchors:
- [source-derived anchor]
- [source-derived anchor]
- [source-derived anchor]

Architecture behavior:
[insert one architecture block below]

Completion budget:
Use [minimal / restrained / extended] completion only for [named edges or separations]. Derive every cue from source color, material, and direction. Do not invent [source-specific anatomy risks].

Transformation grammar:
Use [one primary device] only where it reinforces [carrier]. Optionally add [one supporting treatment].

Composition and mood:
[placement, negative space, background tone, energy]

Invariants:
Preserve [identity-defining source properties]. Use no visual content outside Image 1. No text, logo, frame, unrelated object, or watermark.

Avoid:
filter-only result, generic photo mask, ordinary double exposure, full redraw, decorative anatomy, uniform opacity fade, excessive fragments, unrelated collage
```

## Architecture blocks

### Contained

```text
Allow a mostly complete target contour because the source supplies a coherent internal map. Keep at least three source regions performing distinct roles and preserve internal photographic depth. Add at most one or two small source-texture escapes; do not turn the image into generic fill inside a prefabricated mask.
```

### Permeable

```text
Keep approximately [range] of the target readable. Let [source material] cross or dissolve at [two or three zones], while [anchors] remain legible. Preserve the original field or surface through and around the form. Do not fuse by lowering total opacity.
```

### Gestural

```text
Let [dominant source motion] carry the target. Establish [anchors], but keep trailing or distal zones incomplete. Source motion must dominate anatomy; do not independently complete multiple limbs, joints, or facial structures.
```

## Compilation rules

- Name concrete source structures instead of abstract style adjectives.
- Write a role map; do not merely say the photo is “inside” the target.
- State architecture explicitly so its boundary rules are not mixed with another architecture.
- Repeat source invariants on every revision.
- Do not name living artists, brands, or copyrighted characters as style targets.

## Targeted revisions

**Weak target:** strengthen two source-derived anchors without completing the full anatomy.

**Generic mask:** restore three distinct carrier roles and coherent internal depth; remove any contour unsupported by the source.

**Weak permeable fusion:** add two directional source crossings while keeping selected anchors crisp; do not lower overall opacity.

**Gestural form too anatomical:** dissolve separately completed limbs or facial parts and restore one dominant source motion.

**Result looks illustrated:** remove invented veins, feathers, fur, joints, faces, or outlines; rebuild only from existing carriers.

**Forced target:** discard it, reclassify the source, and choose a lower-completion candidate with a stronger keystone.

