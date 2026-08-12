---
name: photo-form-transposition
description: Transform an uploaded photograph into an art-directed visual-transposition poster by extracting its strongest structures and reorganizing them into a source-compatible biological, natural, atmospheric, geological, or object-like form. Use for photo-borrowed-shape artwork, 照片借形转译, photographic abstraction, environment-fused silhouettes, editorial art posters, or requests to make a recognizable new form from one source photo without merely filtering, redrawing, masking, or double-exposing it.
---

# Photo Form Transposition

Create a poster with two simultaneous readings: a newly recognizable form and the still-perceptible source photograph. Let the source determine the form rather than forcing a preset subject.

## Preserve the source contract

- Treat the uploaded photograph as the sole visual-content source unless the user explicitly authorizes additional imagery.
- Inspect the source before choosing a target. If the file is local, view it before invoking an image-editing tool.
- Preserve the source's identity through its actual textures, light, color, rhythm, and spatial direction.
- Do not invent anatomy or decorative structure merely to complete a target.
- Do not add text, logos, frames, or unrelated objects unless requested.

## Run the workflow

1. **Extract visual carriers.** Identify two to four dominant features such as ridges, shadow axes, foam paths, tonal gradients, cloud masses, seams, repeated marks, or directional light. Omit secondary detail.
2. **Select the target form.** Read [references/visual-system.md](references/visual-system.md). Generate three to six candidates from the source geometry, score them, and choose the strongest. If the user names a target, test its fit rather than silently replacing it; propose a better target only when the named one requires major invention.
3. **Set transposition strength.** Use `balanced` by default. Use `subtle` when discovery matters more than immediate recognition, or `assertive` when the target must read at once.
4. **Build recognition and continuity.** Establish three or four recognition anchors, keep only the necessary boundary, and create two or three source-derived bridges between the form and its environment. Preserve large negative space without isolating the subject.
5. **Compile the edit prompt.** Read [references/prompt-compiler.md](references/prompt-compiler.md). Describe the source image as the edit target, name invariants, and specify only the structure needed for this source.
6. **Generate non-destructively.** Use an available image-generation or image-editing tool with the source image attached. Save project-bound outputs into the workspace with a new versioned filename.
7. **Inspect and revise once.** Read [references/quality-gate.md](references/quality-gate.md). Check the result both at normal size and as a thumbnail. If it fails, make one targeted revision addressing the dominant failure instead of adding more effects.

## Keep creative freedom disciplined

- Use slicing, repetition, offset, stair-step edges, frame echoes, grain, or print texture only when they reinforce a source structure.
- Choose at most one primary transformation grammar and one supporting device.
- Allow incomplete boundaries and perceptual closure. Do not equate clarity with a fully closed silhouette.
- Prefer an unnamed or archetypal form over a literal species when specific anatomy would require fabrication.
- Let the background participate through source-derived atmosphere, light, shadow, water, grain, or texture. Environmental fusion is not achieved by merely lowering opacity.

## Reject these outcomes

- A filtered photograph with no structural reorganization
- A photograph clipped into a clean mask or sticker-like silhouette
- A conventional double exposure with two independent images
- A realistic illustration or complete redraw of the source
- An unrecognizable target with no stable anchors
- Excessive fragments, unrelated collage, or effects that dominate the photograph
- A target choice that sounds plausible only after a verbal explanation

When the first result is attractive but structurally wrong, fix the target logic or boundary behavior before polishing texture.

