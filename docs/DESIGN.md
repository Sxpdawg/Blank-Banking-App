---
name: Blank
colors:
  surface: '#16130b'
  surface-dim: '#16130b'
  surface-bright: '#3d392f'
  surface-container-lowest: '#110e07'
  surface-container-low: '#1f1b13'
  surface-container: '#231f17'
  surface-container-high: '#2d2a21'
  surface-container-highest: '#38342b'
  on-surface: '#eae1d4'
  on-surface-variant: '#d0c5af'
  inverse-surface: '#eae1d4'
  inverse-on-surface: '#343027'
  outline: '#99907c'
  outline-variant: '#4d4635'
  surface-tint: '#e9c349'
  primary: '#f2ca50'
  on-primary: '#3c2f00'
  primary-container: '#d4af37'
  on-primary-container: '#554300'
  inverse-primary: '#735c00'
  secondary: '#c4c6cd'
  on-secondary: '#2d3136'
  secondary-container: '#44474d'
  on-secondary-container: '#b3b5bc'
  tertiary: '#bfcdff'
  on-tertiary: '#082b72'
  tertiary-container: '#97b0ff'
  on-tertiary-container: '#254188'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffe088'
  primary-fixed-dim: '#e9c349'
  on-primary-fixed: '#241a00'
  on-primary-fixed-variant: '#574500'
  secondary-fixed: '#e0e2e9'
  secondary-fixed-dim: '#c4c6cd'
  on-secondary-fixed: '#191c21'
  on-secondary-fixed-variant: '#44474d'
  tertiary-fixed: '#dbe1ff'
  tertiary-fixed-dim: '#b4c5ff'
  on-tertiary-fixed: '#00174b'
  on-tertiary-fixed-variant: '#27438a'
  background: '#16130b'
  on-background: '#eae1d4'
  surface-variant: '#38342b'
typography:
  display-lg:
    fontFamily: Hanken Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.02em
  display-lg-mobile:
    fontFamily: Hanken Grotesk
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Hanken Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
    letterSpacing: -0.01em
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-sm:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
    letterSpacing: 0.05em
  financial-data:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 24px
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 8px
  container-max-width: 1280px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 64px
---

## Brand & Style
The design system for Blank is centered on the concept of "Essential Luxury." It targets a high-net-worth audience that values discretion, precision, and exclusivity. The brand personality is authoritative yet understated, evoking the feeling of a private vault or a high-end physical atelier.

The design style is **Ultra-Premium Minimalism** with a **High-Contrast** edge. It utilizes a deep black environment to allow gold accents and silver surfaces to feel luminous and valuable. The interface avoids unnecessary decoration, relying instead on perfect alignment, generous negative space, and the interplay between matte charcoal surfaces and metallic highlights. The goal is to evoke an emotional response of absolute security and sophisticated confidence.

## Colors
The palette is strictly limited to maintain the premium narrative. 

- **Primary (Gold):** Used sparingly for calls to action, active states, and critical financial indicators. It represents value and achievement.
- **Secondary (Chrome/Silver):** Used for interactive secondary elements, borders, and iconography. It provides a technical, precise counterpoint to the warmth of the gold.
- **Background (Deep Black):** The canvas for all views. It should be pure `#000000` to maximize contrast and visual depth.
- **Surface (Charcoal):** Used for cards, containers, and modals to create subtle layering without breaking the dark immersion.
- **Text:** High-contrast white for headings and primary data; muted grays for metadata to ensure a clear information hierarchy.

## Typography
The typography system uses **Hanken Grotesk** for headlines to provide a sharp, contemporary feel, and **Inter** for body copy to ensure maximum legibility for financial data. **JetBrains Mono** is introduced for labels and small captions to evoke a sense of technical precision and "algorithmic" accuracy.

For financial figures, always enable tabular num (tnum) and lining figures (lnum) to ensure columns of numbers align perfectly. Headlines should utilize tighter letter-spacing to appear more impactful, while labels should be tracked out slightly for better readability at small sizes.

## Layout & Spacing
This design system employs a **Fixed Grid** philosophy for desktop to maintain an editorial, "prestige" feel, transitioning to a fluid layout for mobile. 

A 12-column grid is used on desktop with wide 64px margins to create a "frame" around the content. Spacing follows a strict 8px linear scale. Large-scale layouts should prioritize "breathing room," often leaving entire columns empty to emphasize the content that remains. Elements should align to the grid edges with mathematical precision—no soft offsets or floating "organic" placements.

## Elevation & Depth
Depth is created through **Tonal Layers** and **Low-Contrast Outlines** rather than traditional shadows. 

In a pure black environment, shadows are invisible. Therefore, elevation is communicated by lightening the surface color (e.g., moving from `#000000` background to `#1A1A1A` surface). To further define boundaries, use ultra-thin 1px borders in a semi-transparent Silver (`rgba(192, 194, 201, 0.1)`). 

Interactive elements can use a subtle "inner glow" or a very slight Gold stroke to indicate focus. Avoid blurs or glassmorphism to maintain the "solid" and "heavy" feel of the brand.

## Shapes
The shape language is **Soft** but leans towards architectural rigidity. A base radius of 4px (`0.25rem`) is used for buttons and inputs, providing just enough comfort without losing the professional edge.

Large containers and cards may use 8px (`0.5rem`) to feel more substantial. Interactive elements like checkboxes should remain sharp or minimally rounded to reinforce the precision-tooled aesthetic. Circle shapes are reserved exclusively for avatars and status indicators.

## Components

### Buttons
- **Primary:** Solid Gold background with Black text. No border. High-gloss hover effect (slightly lighter gold).
- **Secondary:** Transparent background with a 1px Silver border. White text.
- **Tertiary:** Pure text-link style using Gold or White with an underline on hover.

### Input Fields
Inputs are Charcoal (`#1A1A1A`) with 1px Silver borders that turn Gold on focus. Use JetBrains Mono for placeholder text to emphasize the technical nature of the platform.

### Cards
Cards are flat Charcoal surfaces with no shadows. Boundary definition is achieved via the 1px Silver border at 10% opacity. For featured content, a "Gold top-border" (2px) can be used to denote priority.

### Chips & Tags
Small, rectangular shapes with 2px corner radius. Use silver-on-charcoal for neutral data and gold-on-black for "Exclusive" or "High Priority" statuses.

### Financial Lists
Data rows should have a subtle 1px divider (`rgba(255,255,255,0.05)`). Amounts should always use Inter in tabular-nums setting for vertical alignment of decimal points.