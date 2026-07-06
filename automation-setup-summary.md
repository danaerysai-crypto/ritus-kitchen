# Ritu's Kitchen — Automation Setup Summary
## From Manual to Hands-Free Marketing + Orders

---

## What Was Just Built

| Component | File | Purpose |
|-----------|------|---------|
| **Self-service order page** | `order.html` | Customers order online, data auto-captures |
| **Automation blueprint** | `automation-blueprint.md` | Full automation strategy |
| **Google Form mapping** | `tracking/google-form-mapping.md` | Connect order form to Google Sheet |
| **Weekly routine** | `tracking/weekly-automation-routine.md` | ~2 hours/week checklist |
| **WhatsApp auto-templates** | `tracking/whatsapp-automation-templates.md` | Quick replies + broadcasts |
| **Updated `index.html`** | All CTAs point to `order.html` | Drive traffic to automated order page |

---

## The New Customer Journey

```
Customer sees post/flyer/search result
        ↓
Clicks UTM link → lands on order.html
        ↓
Fills 30-second form (name, phone, area, meal, source)
        ↓
Data silently saves to Google Sheet
        ↓
WhatsApp opens with pre-filled order message
        ↓
Customer sends message → Ritu confirms
        ↓
After delivery → auto `/thanks` message + feedback link
        ↓
Positive feedback → `/review` for Google
        ↓
3+ orders → `/tiffin` upsell
        ↓
30+ days dormant → `/winback` message
```

---

## What's Still Manual (Honestly)

| Task | Why |
|------|-----|
| Cooking | Ritu makes the food |
| Packing | Physical task |
| Delivery | Human courier needed |
| Final WhatsApp confirmation | Personal trust signal |
| Handling special/custom requests | Requires judgment |
| Daily WhatsApp status photo | Needs fresh thali photo |
| Weekly review of dashboard | Strategic decisions |

Everything else can be scheduled, templated, or automated.

---

## Setup Steps to Activate Automation

### Step 1: Create Google Form (30 min)
1. Go to `forms.google.com`
2. Add 9 questions per `google-form-mapping.md`
3. Get form action URL + field entry IDs
4. Replace placeholders in `order.html`
5. Link form responses to Google Sheet

### Step 2: Add Real Google Analytics ID (5 min)
1. Get GA4 Measurement ID from `analytics.google.com`
2. Replace `G-XXXXXXXXXX` in:
   - `index.html`
   - `order.html`
   - `order-history.html`

### Step 3: Set Up WhatsApp Business Quick Replies (20 min)
Add shortcuts:
- `/order` → order.html link
- `/menu` → today's menu
- `/tiffin` → weekly subscription
- `/thanks` → feedback link
- `/review` → Google review link
- `/winback` → dormant customer message

### Step 4: Schedule Social Media (45 min on Sunday)
1. Open Meta Business Suite
2. Connect Instagram + Facebook
3. Schedule 7 posts for the week
4. Use captions from `social-media-captions-30-days.md`
5. Add UTM links to every post

### Step 5: Start Weekly Ritual (15 min on Sunday)
1. Review dashboard
2. Check dormant customers
3. Send win-backs
4. Plan one experiment

---

## Time Required

| Phase | Time |
|-------|------|
| Initial setup | 2–3 hours |
| Weekly maintenance | ~2 hours |
| Daily WhatsApp status | 5 min × 2 = 10 min |
| Order confirmations | 10 min |
| Sunday batch + review | 1 hour |
| Win-backs | 15 min |

---

## Key URLs

| Page | URL |
|------|-----|
| Home | `https://ritus-kitchen.vercel.app` |
| Order | `https://ritus-kitchen.vercel.apporder.html` |
| Order History | `https://ritus-kitchen.vercel.apporder-history.html` |
| WhatsApp | `https://wa.me/919043140686` |
| Email | `rituskitchen.av@gmail.com` |

---

## Next Action

1. **Create the Google Form** using `tracking/google-form-mapping.md`
2. **Update `order.html`** with real form IDs
3. **Test one complete order** end-to-end
4. **Replace `G-XXXXXXXXXX`** with real GA4 ID
5. **Post the order link** in Instagram bio, WhatsApp bio, and flyers

Want me to create a **step-by-step Google Form creation video script** or **screenshot guide** next? Or shall I build an **admin page** where you can log orders from your phone directly into the system?