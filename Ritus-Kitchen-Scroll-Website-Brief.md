# Ritu's Kitchen — Cinematic Scrollytelling Website

## Direction: "The Living Recipe Journey"

A single-page scroll experience where visitors don't just read a menu — they **cook with Ritu**. Every scroll reveals a step in the story: ingredients arrive, spices bloom, batter ferments, flames dance, steam rises, and a full thali comes together. The website feels less like a restaurant page and more like stepping into Ritu's kitchen at dawn.

This direction merges:
- **Direction #2 (Recipe as Scroll Journey)** — scroll-controlled cooking sequences
- **design.md** — warm, practical, trustworthy, mobile-first system
- **Ritu's actual menu** — idli sambar, poori bhaaji, thali, soups, starters, paysum

---

## Brand Positioning for This Build

| Element | Choice |
|---|---|
| Brand name | **Ritu's Kitchen** (final) — placeholder: *Amma's Table* from design.md is overridden |
| Tagline | "Homely food, away from home" |
| Emotional promise | "You don't just order. You cook with Ritu." |
| Visual style | Warm turmeric + curry-leaf green + handmade paper cream |
| Interaction signature | Scroll = stirring, pouring, plating |

---

## Anti-Gravity Master Prompt

```
Build a cinematic, single-page scrollytelling website for a home kitchen brand called "Ritu's Kitchen" in Auroville, India. The site must feel warm, trustworthy, and practical (mobile-first, fast, accessible) but also visually extraordinary — never generic. Use scroll-triggered animations to turn the menu into a cooking journey.

DESIGN SYSTEM:
- Colors: deep green #244A36, terracotta #C8663D, turmeric gold #D99B36, warm cream #FFF8ED, ink #1F2421, muted body #4C544F
- Typography: DM Serif Display (headings), Inter (body), system fallback
- Style: authentic Indian home kitchen, natural daylight, real brass/copper vessels, fresh vegetables, steam, imperfect beauty
- Motion: GSAP ScrollTrigger. Every section animates on scroll. No autoplay carousels. Respect prefers-reduced-motion.
- Layout: single continuous scroll. Header sticky. One persistent bottom CTA on mobile: "Order on WhatsApp".

SECTIONS — build in order:

1. HERO: "Good morning from Ritu's kitchen"
   - Full-height dawn scene. Soft sun through a kitchen window. A copper tumbler of chai steams gently.
   - Text reveals line by line on scroll: eyebrow, H1, trust line.
   - CTA: "Explore today's menu" (scrolls to next section) + "Order now" (WhatsApp link).
   - Parallax steam rising. Cursor becomes a small wooden spatula.

2. RITU'S PROMISE: "I cook what I feed my own family"
   - Split image/text. Ritu's note appears as if written on a recipe card.
   - Animated badge row: GF / Vegan / Fresh / No Maida / 24h Pre-book.
   - On scroll, the card tilts slightly and ink appears word-by-word.

3. BREAKFAST JOURNEY: "From batter to breakfast"
   - Scroll sequence: soaked urad dal + rice → grinder turns → batter ferments overnight → morning idli steams → coconut chutney falls → sambar ladled.
   - Floating price tag and "Add to breakfast order" micro-CTA.
   - Also show Poori Bhaaji as alternative path: dough rolled, poori puffs in hot oil, mother's aloo bhaaji simmers.
   - Dietary tags animate in (GF, Vegan swap).

4. LUNCH THALI JOURNEY: "One thali, no confusion"
   - A empty thali plate centers the screen.
   - Scroll adds each element one by one: sabji of the season, dal of the day, jeera rice, jowar/bajra roti puffing.
   - Each item lands with a soft sound-replacement visual (steam puff, spice dust).
   - Price options appear as handwritten labels around the plate.
   - "GF swap" and "vegan — no ghee" toggles show alternative plate composition.

5. DINNER JOURNEY: "Soup, starter, thali, sweet"
   - Four small scroll acts in one long section:
     a. Soup: pumpkin roasts, ginger sizzles, creamy soup poured into a bowl.
     b. Starter: honey-chilli potato toss, paneer tikka skewers charring, avocado toast.
     c. Main thali reappears at dusk lighting.
     d. Dessert: paysum (rice + coconut milk + jaggery) or kadha prashad halwa.
   - Horizontal scroll on desktop for the four courses; vertical stacked scroll on mobile.

6. HOW IT WORKS: "Choose. Book. Eat fresh."
   - 3 step cards with subtle number animation.
   - Emphasize: 24-hour pre-booking, WhatsApp, share allergies.

7. TESTIMONIALS: "What guests say"
   - 3 cards with real-feel quotes. No fake names. Rounded cards, star ratings.

8. JOIN THE KITCHEN (WhatsApp CTA): "Get tomorrow's menu first"
   - Large WhatsApp button. Phone number 90431 40686.
   - Background: evening kitchen, tiffin boxes being packed.

9. FOOTER: Practical links, hours, policies, location.

REQUIREMENTS:
- Mobile-first. Sticky WhatsApp CTA at bottom.
- All prices from the menu: Idli ₹110, Poori Bhaaji ₹120, Muesli ₹110, Omelet Bread ₹140, Tea ₹49, Millet/Oat Tea ₹69, Sindhi/Gujarati Breakfast ₹150, Veg Thali ₹220, GF Thali ₹250, Egg Thali ₹320, Chicken/Fish Thali ₹420, Soups ₹110, Starters ₹130–150, Popcorn ₹60, Dessert ₹60 / GF ₹90.
- Use actual menu items only.
- Accessibility: semantic headings, keyboard nav, focus rings, alt text, reduced motion support.
- Performance: lazy-load images below fold, optimize food photos, no heavy third-party scripts.
- No copied branding or stock generic photos. Use original style only.
- Generate or source warm, authentic Indian home-kitchen food photography.
- All text short, friendly, practical. No jargon. No aggressive sales.

OUTPUT:
- Single HTML file with embedded CSS/JS or linked files.
- Fully responsive, working scroll animations, working WhatsApp CTA.
- Component structure matching design.md: AnnouncementBar, Header, Hero, Category/ScrollSections, ProductCards, ValueProp, StorySplit, HowItWorks, Testimonials, WhatsAppCTA, Footer.
```

---

## Scroll Sequence Storyboard

| Scroll % | Scene | Visual Action | Menu Item Revealed | Interaction |
|---|---|---|---|---|
| 0–10% | Dawn kitchen | Sun enters window, chai steams | Hero + promise | Scroll reveals text |
| 10–20% | Ritu's note | Recipe card appears, ink writes | Trust badges | Card tilt on hover |
| 20–35% | Batter to idli | Dal + rice → grind → ferment → steam | Idli Sambar Chutney | "Add" button pops |
| 35–45% | Poori path | Dough → roll → puff in oil + aloo bhaaji | Poori Bhaaji | GF swap toggle |
| 45–60% | Empty thali fills | Sabji, dal, rice, roti land one by one | Lunch Thali | Choose thali type |
| 60–70% | Dinner courses | Soup, starter, thali, dessert in sequence | Dinner section | Horizontal scroll (desktop) |
| 70–80% | How it works | 3 numbered steps animate | Ordering process | Sticky CTA appears |
| 80–90% | Guest stories | Testimonial cards slide in | Social proof | Swipe on mobile |
| 90–100% | Join WhatsApp | Evening kitchen, tiffin packing | CTA | WhatsApp button pulse |

---

## Image Generation Prompts

Use these for Midjourney / DALL-E / Flux / Anti-Gravity image generation.

### Hero / Atmosphere
1. **Dawn kitchen still life**: "Warm morning sunlight through a rustic Indian kitchen window, copper tumbler with steaming chai on a wooden counter, fresh curry leaves, raw turmeric root, soft shadows, film photography aesthetic, shallow depth of field, cream and green color palette, cinematic 4:3"

2. **Ritu cooking portrait**: "Indian woman in her 40s stirring a pot in a sunlit home kitchen, genuine smile, steam rising, brass kadai, natural daylight, documentary food photography style, warm and honest, 4:5 portrait"

### Breakfast Journey
3. **Idli batter sequence opener**: "Close-up of soaked urad dal and rice in a terracotta bowl, water droplets, morning light, top-down food photography, warm cream tones"

4. **Idli steaming**: "Freshly steamed fluffy idlis in a traditional idli steamer, wisps of steam, coconut chutney in small brass bowl, sambar in the background, authentic South Indian home kitchen, 1:1"

5. **Poori puffing**: "Golden wheat pooris puffing in hot oil in a kadai, hands rolling dough in background, warm action shot, shallow depth of field, 16:9"

6. **Mother's aloo bhaaji**: "Simple aloo bhaaji in a black iron pan with hing and mustard seeds visible, rustic home kitchen, top-down angle, warm tones"

### Lunch Thali
7. **Empty thali plate**: "Empty steel thali on a banana leaf, warm daylight, rustic wooden table, cream and green palette, top-down, ready to be filled"

8. **Seasonal sabji**: "Fresh seasonal vegetable sabji in a brass bowl, vibrant colors, home-style, shallow depth, 1:1"

9. **Dal of the day**: "Comforting yellow dal tadka with ghee, cumin, and red chili, steam rising, copper bowl, warm light, 1:1"

10. **Jowar/bajra roti**: "Stack of rustic jowar rotis, slightly charred, on a cotton cloth, millet texture visible, honest food photography, 4:5"

### Dinner
11. **Roasted pumpkin soup**: "Creamy roasted pumpkin soup with ginger swirl, crusty bread slice, ceramic bowl, warm autumn tones, 1:1"

12. **Honey chilli potato**: "Crispy honey chilli potato toss in a wok, sesame seeds, green chili, action shot with slight motion blur, appetizing, 16:9"

13. **Paneer tikka skewers**: "Charred paneer tikka skewers on a brass plate, yogurt marinade, mint chutney, smoky, warm light, 1:1"

14. **Paysum dessert**: "Traditional South Indian paysum in a brass bowl, rice pudding texture, coconut milk, jaggery, garnished with cashews, warm dessert photography, 1:1"

### Process / Trust
15. **Tiffin packing**: "Hands packing a steel tiffin dabba with rice, dal, and sabji, cotton napkin, warm evening kitchen light, documentary style, 4:3"

16. **Ingredient close-up**: "Fresh vegetables, whole spices, and lentils arranged on a weathered wooden surface, turmeric, red chili, cumin seeds, curry leaves, top-down, 16:9"

### UI / Texture Assets
17. **Handmade paper texture**: "Subtle cream handmade paper texture with faint fiber detail, seamless, warm off-white, no text"

18. **Spice dust particles**: "Fine turmeric and spice powder particles floating against dark warm background, cinematic, usable as overlay texture"

---

## Mobile Adaptation Notes

- Replace horizontal dinner scroll with vertical stacked cards, each with a mini scroll reveal.
- Keep hero shorter; text first, image second.
- Sticky bottom WhatsApp CTA persists after hero.
- Thali section becomes tap-to-add-items instead of full scroll animation.
- Reduce parallax intensity. Respect prefers-reduced-motion.

---

## Implementation Stack Recommendation

| Layer | Tool |
|---|---|
| Animation | GSAP + ScrollTrigger |
| Icons | Phosphor Icons or Lucide (rounded line style) |
| Fonts | DM Serif Display + Inter via Google Fonts |
| Images | AVIF/WebP with srcset |
| Build | Anti-Gravity / plain HTML+CSS+JS |
| Form/CTA | WhatsApp deep link: `https://wa.me/919043140686` |

---

## Next Action

Paste the Anti-Gravity master prompt above into Anti-Gravity to generate the full website. Use the image prompts to produce hero/food/process photography. Then refine based on real photos Ritu can provide from her actual kitchen.
