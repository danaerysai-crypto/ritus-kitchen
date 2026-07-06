# Ritu's Kitchen — 3-Question Customer Data Capture
## User-Friendly + History Available Openly

---

## What Changed

| Before | After |
|--------|-------|
| 10+ question form | 3 natural WhatsApp questions |
| Customer remembers orders | Self-service `order-history.html` page |
| Manual segmentation | Excel auto-infers segments from orders |
| Long feedback survey | 3-tap post-delivery form |

---

## The 3-Question Order Flow

When a new customer orders, ask naturally:

1. **"Where should I send today's thali?"** → Area + accommodation
2. **"Any dietary needs?"** → Vegan, GF, no onion-garlic, mild spice
3. **"How did you hear about us?"** → Marketing source

That's it. Order captured. Profile started.

---

## Files Created / Updated

| File | What It Is |
|------|------------|
| `tracking/lightweight-capture-guide.md` | Strategy: capture more by asking less |
| `tracking/whatsapp-3-question-flow.md` | Exact WhatsApp conversation scripts |
| `order-history.html` | Customer self-service order history page |
| `index.html` | Updated footer with "My Order History" link |
| `tracking/ritus-kitchen-marketing-dashboard.xlsx` | New "Inferred Segments" sheet with auto-formulas |

---

## Customer Self-Service Order History

**URL:** `ritus-kitchen.github.io/order-history.html`

**What customers see:**
- Total orders
- Total spent
- Average order value
- Favorite item
- Loyalty badge (New, Regular, VIP, etc.)
- Full order history table
- One-click "Order again on WhatsApp"

**Why this is useful:**
- They don't need to remember past orders
- They can prove loyalty for rewards
- Transparent and trustworthy

**Demo:** Try phone number `9876543210`

---

## Excel Now Auto-Infers Customer Segments

The new **"Inferred Segments"** sheet calculates:

| Field | Logic |
|-------|-------|
| Resident type | ≥15 orders in 60 days → Long-term; 1–3 → Visitor |
| Family size | Often orders quantity ≥2 → Family |
| Subscriber | Has ordered Weekly Tiffin |
| Regular | ≥3 orders |
| High value | Total spent ≥₹2,500 |
| Dormant | No order in 30+ days |
| Wellness customer | Ordered Wellness Thali |
| Advocate | High value customer |
| Preferred meal | Lunch vs Dinner based on orders |
| Preferred product | Most-ordered product |

You just log orders. The dashboard does the profiling.

---

## Updated 3-Question Feedback Form

Send this after delivery:

> Hi [Name], hope you enjoyed today's thali! 🍛 Quick 30-second feedback? [link]

**Form questions:**
1. How was your meal? ⭐⭐⭐⭐⭐
2. How did you hear about us?
3. Would you order again this week?

No typing. Three taps.

---

## WhatsApp Labels to Use

| Label | Use |
|-------|-----|
| 🟢 New | First-time customer |
| 🔵 Regular | 3+ orders |
| 🟣 Subscriber | Weekly tiffin |
| 🌿 Wellness | Dietary restriction |
| 👨‍👩‍👧 Family | Multiple thalis |
| 😴 Dormant | 30+ days no order |
| ⭐ VIP | High spend / referrer |

---

## Next Action

1. Replace `G-XXXXXXXXXX` in `order-history.html` and `index.html` with your real GA4 ID
2. Test the order history page by opening it in a browser
3. Use the 3-question flow on your next WhatsApp order
4. Add the order history page link to your Instagram/WhatsApp bio

Want me to connect the order history page to a real data source (Google Sheets or a simple JSON file) so it updates automatically as you log orders?