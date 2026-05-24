---
name: Aurelian Design System
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#201f1f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353534'
  on-surface: '#e5e2e1'
  on-surface-variant: '#d0c5af'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#99907c'
  outline-variant: '#4d4635'
  surface-tint: '#e9c349'
  primary: '#f2ca50'
  on-primary: '#3c2f00'
  primary-container: '#d4af37'
  on-primary-container: '#554300'
  inverse-primary: '#735c00'
  secondary: '#c6c6c6'
  on-secondary: '#303030'
  secondary-container: '#474747'
  on-secondary-container: '#b5b5b5'
  tertiary: '#cfcece'
  on-tertiary: '#2f3131'
  tertiary-container: '#b3b3b3'
  on-tertiary-container: '#444546'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffe088'
  primary-fixed-dim: '#e9c349'
  on-primary-fixed: '#241a00'
  on-primary-fixed-variant: '#574500'
  secondary-fixed: '#e2e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1b1b1b'
  on-secondary-fixed-variant: '#474747'
  tertiary-fixed: '#e3e2e2'
  tertiary-fixed-dim: '#c6c6c6'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#464747'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.02em
  display-lg-mobile:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
    letterSpacing: -0.01em
  headline-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
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
  label-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.02em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 64px
  max-width: 1440px
---

## Brand & Style

This design system is engineered for elite financial institutions, wealth management platforms, and private banking tiers. The brand personality is rooted in **sovereignty, precision, and exclusivity**. It seeks to evoke a sense of digital "vault" security while maintaining the sleekness of high-end Swiss horology.

The visual style is a fusion of **Dark Minimalism** and **Tactile Luxury**. It utilizes deep obsidian surfaces punctuated by sharp metallic accents. Every element is designed to feel "weighted" and intentional, moving away from the ephemeral nature of standard SaaS designs toward a more permanent, institutional presence. White space is treated as a luxury commodity, used generously to focus attention on critical financial data and premium content.

## Colors

The palette is anchored in a **Dark-First** philosophy to reflect the private, "after-hours" nature of high-end wealth management.

- **Primary (Metallic Gold):** Used sparingly for calls to action, active states, and brand signatures. It represents growth and prestige.
- **Surface (Black & Charcoal):** Pure Black (#000000) is reserved for the primary background, while Deep Charcoal (#121212) defines container levels.
- **Accents (Chrome/Silver):** Used for "hairline" borders, iconography, and secondary metadata. This adds a technical, industrial edge to the warmth of the gold.
- **Functional Colors:** Success (Emerald), Danger (Ruby), and Warning (Amber) should be desaturated to fit the dark aesthetic, ensuring they do not clash with the primary gold.

## Typography

This design system utilizes **Inter** exclusively to maintain a modern, systematic, and highly legible interface. The typographic hierarchy relies on weight and tracking rather than decorative fonts.

**Headlines:** Should feel authoritative. Use tighter letter-spacing for large display sizes to create a "locked-in" look. 
**Labels:** Use all-caps with generous letter-spacing (0.05em) for category headers and navigation elements to mimic the engraving found on luxury assets.
**Numbers:** Since this is a banking system, tabular figures should be used for all financial data to ensure columns of numbers align perfectly for easy scanning.

## Layout & Spacing

The layout philosophy follows a **Fixed-Grid hybrid** model. While the content is responsive, the core dashboard utilizes a centered 12-column grid on desktop with a strict max-width to prevent the interface from feeling "stretched" or "cheap."

**Rhythm:** An 8px linear scale is used for all padding and margins. 
- **Desktop:** 64px outer margins provide a "frame" for the content, emphasizing exclusivity.
- **Mobile:** Margins scale down to 16px, but internal padding within containers remains generous (20px+) to maintain a high-end feel.
- **Gutters:** A consistent 24px gutter provides ample breathing room between financial modules.

## Elevation & Depth

Hierarchy in this design system is achieved through **Tonal Layering** and **Metallic Outlines** rather than traditional shadows.

1.  **Base:** Pure Black (#000000).
2.  **Containers:** Deep Charcoal (#121212) with a 1px "Chrome" border at 15% opacity.
3.  **Active/Raised:** Subtle "Inner Glow" effects are used to simulate light hitting the edge of a metallic surface. 
4.  **Glassmorphism:** For overlays and modals, use a high-density background blur (20px+) with a 10% opacity white tint to simulate polished smoked glass.

Avoid heavy drop shadows; if a shadow is necessary, it should be a sharp, 0-blur "hard shadow" to mimic a direct light source in a dark room.

## Shapes

The shape language is **Refined and Geometric**. We avoid "bubbly" aesthetics in favor of professional, structured forms.

- **Primary Components:** Use a base 8px (`0.5rem`) radius. This provides enough softness to feel modern without losing the "institutional" rigidness.
- **Large Containers:** Use a 16px (`1rem`) radius for dashboard cards and main navigation blocks.
- **Interactive Elements:** Buttons and input fields should strictly adhere to the 8px rule to ensure a cohesive "click" experience across the platform.

## Components

**Buttons**
- **Primary:** Solid Gold (#D4AF37) with Black text. No gradients.
- **Secondary:** Transparent with a 1.5px Chrome border and Silver text.
- **Ghost:** Silver text with no background, used for low-priority actions.

**Cards**
- Cards should have a #121212 background and a subtle 1px border using the Chrome accent at low opacity. For premium "Tier-1" features, the border can transition to a subtle Gold-to-Charcoal gradient.

**Input Fields**
- Inputs are "Bottom-Line" only or fully enclosed with a dark background. On focus, the border-bottom should animate to Gold. Labels should be small, all-caps, and Silver.

**Chips & Tags**
- Small, rectangular with minimal rounding. Use Silver/Chrome for default tags and desaturated Emerald/Ruby for status indicators.

**Data Visualizations**
- Charts should use Gold as the primary data line, with a soft Gold glow (bloom effect). Grid lines should be faint Charcoal.