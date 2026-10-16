### Syntax that avoids subtitles

Many video models were trained on videos with baked-in subtitles and will add them to outputs. To prevent this:

- Use a colon for dialogue: "She says: Hello there" rather than "She says 'Hello there'"
- Add "(no subtitles)" to the prompt
- If subtitles persist, repeat the instruction: "No subtitles. No subtitles!"

### Pronunciation

If a model mispronounces a name or word, spell it phonetically in the prompt. For example, write "foh-fur" instead of "fofr" or "Shreedar" instead of "Shridhar."

### Who says what

In multi-character scenes, the model can mix up who says what. Tie dialogue to distinctive visual descriptions: "The woman wearing pink says: ..." and "The man with glasses replies: ..."


## Multi-shot and time-coded prompting

Some models support generating multiple shots within a single clip (up to ~15 seconds). You can direct each shot individually using time codes.

### Time-coded format

Write timestamps directly into the prompt:

```
[0-4s]: Wide establishing shot, static camera, misty bamboo forest at dawn
[4-9s]: Medium shot, slow push-in, the fighter steps forward
[9-15s]: Close-up, orbit shot, the fighter strikes, slow motion
```

Each shot should specify:
- Camera position and motion
- Subject action
- Lighting or mood shifts

### Transition language

Use explicit transition instructions between shots:

- "Hard cut to..." for an abrupt switch
- "Seamless morph into..." for a fluid transition
- "Whip pan to..." for a fast, energetic cut
- "Snap cut to..." for a jarring, dramatic shift

Without explicit transitions, the model improvises, which may or may not match your intent.

### Example: multi-shot commercial

```
(0-3s) Macro shot of a luxury perfume bottle among scattered pink peonies,
       shallow depth of field, petals floating in warm afternoon light,
       soft ambient music.
(3-7s) Camera glides closer, a feminine hand enters frame from the right,
       fingers gently touch the glass bottle, the sound of silk rustling.
(7-12s) Hard cut to slow-motion spray, golden mist diffuses through the air,
        particles catching rim light against a dark background,
        the hiss of the atomizer.
(12-15s) Seamless pull-out to hero frame, product centered, volumetric
         lighting, minimal cream background, elegant silence.
```


## Reference inputs

Many video models accept images, video clips, or audio files as reference inputs alongside a text prompt. This shifts the workflow from "prompting" to something closer to "directing."

### Image-to-video

Feed a starting image and describe the motion. The model animates from that frame.

- The input image becomes the first frame of the video
- Describe what changes (action, camera movement), not the static scene the model can already see
- Style preservation is a strength: animated styles, paintings, photographs, and color grading all carry through
- For maximum style control, generate the starting image with a specialized image model first, then pass it to the video model

### First and last frame interpolation

Some models accept both a starting and ending image. The model generates the transition between them. This is useful for:

- Morphing between subjects (e.g. one animal transforming into another)
- Before/after transformations (room makeover, seasonal change)
- Controlled narrative arcs where you know the start and end state

### Subject references

Some models accept reference images of characters, products, or objects and maintain their appearance in the generated video. This is useful for:

- UGC-style product review videos (reference image of character + reference image of product)
- Brand consistency across multiple video clips
- Placing existing characters in new scenarios

When referencing input assets, many models use a bracket syntax like `[Image1]` or `[Audio1]` in the prompt to specify which reference maps to which role: "[Image2] is in the interior of [Image1]."

### Audio-driven generation

Some models accept audio files and sync the generated video to the audio. The model can match:

- Lip movements to speech
- Cuts and motion to musical beats
- Ambient rhythm to environmental sounds

When using audio references, it helps to also transcribe the audio content in the text prompt itself, and match the video duration to the audio length.

### Multi-reference workflows

The most powerful results come from combining multiple reference types:

- An image for character appearance
- A video clip for motion style
- An audio track for rhythm and pacing
- A text prompt describing how everything fits together


## Style control

### Name the style explicitly

Video models understand style labels. Include them directly in your prompt:

- "In the style of claymation"
- "Pixar animation style"
- "Anime"
- "Stop-motion"
- "8-bit retro"
- "Graphic novel"
- "Documentary footage"
- "Origami"
- "LEGO"
- "Blueprint technical drawing"

Style labels affect not just the visual look but also how characters move and interact. A claymation style produces jerky, stop-motion movement. An anime style produces fluid, exaggerated motion.

### Quality anchors

Phrases like "hyper-realistic, 8k" or "cinematic" push models toward their highest fidelity output. Use them when you want photorealistic results.

### Film and genre language

Reference specific genres or filmmaking styles for mood and tone:

- "Michael Mann cinematography" (neon, night, urban)
- "Wes Anderson" (symmetrical, pastel, quirky)
- "Roger Deakins lighting" (naturalistic, precise)
- "Blade Runner 2049 cinematography" (atmospheric, orange/teal)
- "National Geographic documentary" (nature, steady, observational)

### Use input images for style

Rather than describing a style verbally, generate an image with the exact aesthetic you want using an image model, then pass it to the video model. This gives you pixel-level control over the look. The video model preserves the style, color grading, and composition while adding motion.

### Grain and texture

Adding "slightly grainy, film-like" or "VHS aesthetic" pushes output away from the too-clean AI look and makes videos feel more organic.


## Character consistency

### Repeat descriptions verbatim

When generating multiple clips with the same character, use identical character descriptions across prompts. Create a "character sheet" with exact wording:

"John, a man in his 40s with short brown hair, wearing a blue jacket and glasses, looking thoughtful"

Paste this description into every prompt where John appears. The more specific and unique the description, the more consistent the results.

### What to specify

- Physical appearance: age, hair, skin, build
- Clothing: exact garments, colors, materials
- Accessories: glasses, jewelry, hat
- Expression or demeanor: thoughtful, cheerful, intense

### Vary the scene, not the character

When placing a consistent character in different scenarios, change only the action, location, and camera work. Keep the character description word-for-word identical.

### Reference images for identity

If the model supports subject reference images, use a clear photo of the character as input. This is more reliable than text descriptions alone, especially for maintaining facial features across clips.


## Common pitfalls

1. **Not describing audio**: If you skip audio prompting, models hallucinate ambient sounds. A common failure is adding inappropriate laughter or a "live studio audience." Always describe the soundscape.

2. **Too much dialogue for the clip length**: An 8-second clip can hold roughly 2-3 short sentences. Packing in a paragraph produces unnaturally fast speech or truncated output.

3. **Too little dialogue for the clip length**: If you only provide a few words for a long clip, the model fills silence with gibberish or awkward pauses. Match dialogue length to clip duration.

4. **Not specifying what to keep unchanged**: When using reference images or editing, always state what should stay the same. Without explicit instructions, models may change anything.

5. **Expecting variation from identical prompts**: Unlike image models, some video models produce very similar outputs for the same prompt (even with different seeds). If you want variety, change the prompt, don't just rerun it.

6. **Not prompting camera motion**: Without camera direction, you get either static shots or unpredictable movement. Describe the camera explicitly.

7. **Subtitle contamination**: Many models were trained on videos with baked-in subtitles. Use colons for dialogue (not quotes), add "(no subtitles)", and repeat if necessary.

8. **Vague prompts for complex scenes**: Modern video models handle long, detailed prompts. A prompt with 12+ specific requirements (camera moves, lighting, sound design, subject actions, environmental details) can work if each requirement is stated clearly. Don't undersell what you want.

9. **Ignoring aspect ratio and resolution**: Most video models have specific resolutions they support (480p, 720p, 1080p). Check what the model supports and choose the right resolution for your use case. If you need vertical video and the model only outputs landscape, you may need to reframe with a separate tool.

10. **Forgetting that video models don't have internet access**: No video model has live information. They work from training data. Don't expect them to know about current events or real-time information.


## Background reading

The techniques above are distilled from Replicate's blog posts on prompting video models. The posts are anchored to specific models that were current at the time, but the techniques generalize across modern video models. Use these for additional context, then use the [find-models](../find-models/SKILL.md) skill to pick a model that fits your task today.

- [How to make remarkable videos with Seedance 2.0](https://replicate.com/blog/seedance-2) (Apr 2026)
- [How to prompt Veo 3.1](https://replicate.com/blog/veo-3-1) (Oct 2025)
- [How to prompt Veo 3 with images](https://replicate.com/blog/veo-3-image) (Aug 2025)
- [Open source video is back (Wan 2.2)](https://replicate.com/blog/wan-22) (Jul 2025)
- [Compare AI video models](https://replicate.com/blog/compare-ai-video-models) (Jul 2025)
- [How to prompt Veo 3 for the best results](https://replicate.com/blog/using-and-prompting-veo-3) (Jun 2025)
