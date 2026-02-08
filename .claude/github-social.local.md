---
# Image generation provider
provider: svg

# SVG-specific settings
svg_style: illustrated
svg_custom_direction: >
  Colorful collage depicting happy sheep, ducks, dogs, and chickens
  like a grade school art piece conveying happiness and joy. Use bright,
  warm colors with a playful, hand-drawn feel. Include farm elements
  (barn, fence, sun, grass) as cheerful accents. The overall tone
  should be welcoming and non-intimidating — this is a farm system
  for people who are not tech-savvy.

# Dark mode support
# false = light mode only, true = dark mode only, both = generate both variants
dark_mode: both

# Output settings
output_path: .github/social-preview.svg
dimensions: 1280x640
include_text: true
colors: auto

# README infographic settings
infographic_output: .github/readme-infographic.svg
infographic_style: hybrid

# Upload to repository (requires gh CLI or GITHUB_TOKEN)
upload_to_repo: false
---

# GitHub Social Plugin Configuration

This configuration was created by `/github-social:setup`.

## Provider: SVG

Claude generates clean SVG graphics directly. No API key required.
- **Pros**: Free, instant, editable, small file size (10-50KB)
- **Best for**: Professional, predictable results

## Style: Custom Illustrated

A colorful, joyful farm animal collage — happy sheep, ducks, dogs, and chickens
in a playful, grade-school art style. Bright colors, warm tone, welcoming feel.

## Dark Mode: Both

Two variants will be generated:
- `.github/social-preview.svg` (light)
- `.github/social-preview-dark.svg` (dark)

## Commands

- Generate social preview: `/social-preview`
- Enhance README with badges and infographic: `/readme-enhance`
- Run all github-social skills: `/github-social:all`
- Update this configuration: `/github-social:setup`

## Command Overrides

Override any setting via command flags:
```bash
/social-preview --dark-mode
/readme-enhance --provider=svg
```
