---
name: prompt-videos
description: >
  Prompting techniques for AI video generation models on Replicate.
  Use when writing prompts for video models or building video
  generation features.
---

# Prompting video models on Replicate

Distilled from Replicate's blog posts on prompting video models (2025-2026). Techniques are model-agnostic and focus on transferable principles.

## Choose a model with the API, not from memory

This skill describes general prompting techniques. To choose a model, use the [find-models](../find-models/SKILL.md) skill and query the Replicate API. The video model landscape changes weekly. Don't assume specific models exist or are still state-of-the-art based on names you've seen before. Always search the API for current options, then read the schema before running anything.

For pricing and feature comparison, see the [compare-models](../compare-models/SKILL.md) skill.


## Scene description

A good video prompt is a scene description, not a caption. Write what happens, where, and how it looks.

### Layer these elements into every prompt

1. **Subject**: Who or what is in the scene (a person, animal, object, landscape).
2. **Context**: Where the subject is (indoors, a city street, a forest, a spaceship corridor).
3. **Action**: What the subject does (walks, turns, picks up a phone, runs).
4. **Style**: The visual aesthetic (cinematic, animated, stop-motion, documentary).
5. **Camera**: How the camera moves (dolly shot, tracking, static, handheld).
6. **Composition**: How the shot is framed (wide shot, close-up, over-the-shoulder).
7. **Ambiance**: Mood and lighting (warm tones, blue light, golden hour, overcast).

### Be specific, not vague

Vague: "A car chase"

Specific: "A high-speed car chase on a rain-drenched highway at night. Two muscle cars weave through heavy traffic at 140mph, headlights slicing through the downpour. One car clips a semi-truck sending sparks showering across six lanes. Tires hydroplane on standing water. Neon highway signs blur overhead."

### Overdescribe

Modern video models handle long, dense prompts well. Don't write "a man on the phone." Write "a desperate man in a weathered green trench coat picks up a rotary phone mounted on a gritty brick wall, bathed in the eerie glow of a green neon sign." Every concrete detail you add gives the model less room to improvise poorly.

### Name subjects directly

Use descriptive phrases like "the woman in the red jacket" or "the bearded man in flannel." Avoid pronouns, which are ambiguous to video models just as they are to image models.


## Camera and cinematography

Video models understand filmmaking language. Use it to direct the shot rather than hoping for good framing.

### Shot types

Use standard shot terminology to control framing:

- Wide/establishing shot: shows the full scene and environment
- Medium shot: frames the subject from roughly the waist up
- Close-up: fills the frame with the subject's face or a key object
- Extreme close-up: isolates a detail (an eye, a hand gripping a handle, a drop of water)

### Camera motion

Describe how the camera moves:

- Static/tripod: locked-off, no movement
- Pan: horizontal rotation left or right
- Tilt: vertical rotation up or down
- Dolly: camera physically moves toward or away from the subject
- Tracking: camera moves alongside the subject
- Crane: camera rises or descends vertically
- Handheld: shaky, documentary-style movement
- Drone/aerial: overhead or sweeping bird's-eye shots
- Dolly zoom (Hitchcock/vertigo effect): background stretches while subject stays locked

### Camera position

Specify the camera's height and angle:

- Eye level: neutral, natural perspective
- Low angle / worm's eye: looking up at the subject (makes subjects feel powerful or imposing)
- High angle / bird's eye: looking down (makes subjects feel small or vulnerable)
- Over-the-shoulder: frames one subject from behind another
- POV / first-person: camera is the subject's eyes

### Lens and focus language

- Shallow depth of field: subject sharp, background blurred
- Deep focus: everything sharp from foreground to background
- Macro lens: extreme close-up with shallow focus
- Wide-angle lens: exaggerated perspective, more environment visible
- Tilt-shift: miniature effect, selective focus band

### Escalation pattern

A natural progression for short clips is wide > medium > close-up > extreme close-up. This maps well onto 8-15 second clips and gives the model clear structure. For example:

- 0-3s: wide establishing shot of the location
- 3-7s: medium shot, the subject enters or acts
- 7-12s: close-up on the key moment
- 12-15s: extreme close-up on a detail (a hand, an eye, a drop of rain)


## Audio and dialogue

Many video models generate audio natively alongside the visuals. If you don't prompt for the audio you want, the model will guess, and it often guesses wrong.

### Prompt all four audio layers

1. **Dialogue**: What characters say, either exact words or described intent.
2. **Ambient sound**: The background audio of the scene (rain on metal awnings, city traffic, forest birds).
3. **Sound effects**: Specific sounds from actions (a door slamming, glass breaking, a sword being drawn).
4. **Music**: Genre, mood, and instrumentation (a tense cinematic score, soft jazz piano, no music).

If you skip ambient audio, models may hallucinate inappropriate sounds. A common failure mode is adding a "live studio audience" laughing in the background. Prevent this by describing the soundscape explicitly: "sounds of distant bands, noisy crowd, ambient background of a busy festival field."

### Dialogue prompting

There are two approaches:

- Explicit: "The man says: My name is Ben." This gives you exact control over the words.
- Implicit: "The man introduces himself." This lets the model decide the phrasing.

Explicit dialogue should be short enough to fit the clip duration. Packing too much dialogue into an 8-second clip produces unnaturally fast speech. Too little dialogue can produce awkward silence or AI gibberish.


---

## 📚 Deep Reference (Progressive Disclosure)

> ⚠️ **CONTEXT OPTIMIZATION:** The detailed methodology, edge cases, attack vectors, and advanced configurations for this skill are stored externally to save tokens.

To access the full technical reference, you MUST use your iew_file tool to read:

d:\xampp\htdocs\0-fonte\.agent\skills\replicate-prompt-videos\references\reference.md
