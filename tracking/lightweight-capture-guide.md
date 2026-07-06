# Ritu's Kitchen — Lightweight Customer Data Capture
## Capture More by Asking Less

---

## The Rule: Customers Should Not Feel Surveyed

Every piece of data must either be:
1. **Inferred from the order itself** (what they ordered, when, how much)
2. **Collected in one natural sentence** during WhatsApp chat
3. **Optional** after delivery via a 30-second form

**Never ask 10 questions upfront.** Auroville customers value simplicity and trust.

---

## What You Capture Automatically (Zero Customer Effort)

| Data Point | How You Get It | Why It Helps |
|------------|----------------|--------------|
| **Phone number** | WhatsApp message itself | Core ID + broadcast list |
| **Order date & time** | When they message | Demand patterns |
| **Products ordered** | What they ask for | Product popularity |
| **Quantity & price** | Order details | Revenue & AOV |
| **Delivery area** | "Where should I send it?" | Route optimization |
| **Payment mode** | How they pay | Cash flow tracking |
| **Order frequency** | Days between orders | Retention signal |
| **Spending over time** | Sum of all orders | Customer value |
| **Preferred meal time** | Lunch vs dinner orders | Prep planning |
| **Dietary pattern** | Items they never order or customize | Segment offers |

---

## The 3-Question Order Flow

When a customer first orders, ask only these three things **in the natural flow of taking the order**:

### Question 1: Delivery
> "Great! Where should I send today's thali?"

**Captures:** Area, accommodation type (you can guess guesthouse vs house vs yoga center from the address)

### Question 2: Dietary Needs
> "Any dietary needs — vegan, gluten-free, no onion-garlic, mild spice?"

**Captures:** Dietary restrictions in one question

### Question 3: Source
> "One last thing — how did you hear about us? WhatsApp group, Instagram, a friend, guesthouse, or Google?"

**Captures:** Marketing attribution

**That's it. Order placed.**

---

## Infer the Rest from Order History

After 2–3 orders, you already know:

| Inferred Insight | Example |
|------------------|---------|
| **Resident type** | Orders daily for 2 months → long-term resident |
| **Family size** | Orders 2 thalis consistently → couple/family |
| **Frequency** | Orders every Monday–Friday → weekly tiffin candidate |
| **Price sensitivity** | Always orders cheapest → budget-conscious |
| **Loyalty** | 10+ orders → regular / advocate |
| **Dormant risk** | 30 days no order → win-back needed |
| **Preferred dish** | Always orders wellness thali → wellness segment |
| **Meal timing** | Only dinner orders → dinner customer |

---

## Optional 30-Second Feedback Form (After Delivery)

Send this only after the first or second order:

> Hi [Name], hope you enjoyed today's thali! 🍛 Quick 30-second feedback? [Google Form link]

### The 3-question form:

1. **How was your meal?** ⭐⭐⭐⭐⭐
2. **What made you try Ritu's Kitchen today?**
   - WhatsApp group
   - Instagram
   - Google
   - Friend told me
   - Guesthouse
   - Other
3. **Would you order again this week?**
   - Yes, lunch
   - Yes, dinner
   - Yes, both
   - Maybe
   - No

**Done.** Three taps. No typing required.

---

## Customer Self-Service Order History

Instead of asking customers to remember, let them look up their own history.

**How it works:**
1. Customer visits: `https://ritus-kitchen.vercel.app/order-history.html`
2. Enters their phone number
3. Sees their past orders, total spent, favorite items, and any loyalty rewards

**Why this is user-friendly:**
- They don't need to ask "What did I order last time?"
- They can prove repeat orders for loyalty rewards
- Builds transparency and trust

**Privacy note:** Since this is a small local business and customers check their own history, phone-number lookup is acceptable. For extra safety, use last 4 digits or a simple PIN if needed later.

---

## Publicly Useful Data (For Marketing)

You can share **anonymized** use history as social proof:

| Safe to Share | Not Safe to Share |
|---------------|-------------------|
| "Served 500 thalis this month" | Individual customer names |
| "85% of customers reorder within 7 days" | Individual phone numbers |
| "Top ordered dish: Palak Paneer Thali" | Individual order history |
| "Customers from 25+ guesthouses" | Specific customer addresses |

---

## Updated Excel Dashboard: Auto-Inferred Demographics

The dashboard now calculates customer segments automatically:

| Inferred Field | Formula Logic |
|----------------|---------------|
| **Resident type** | If ≥15 orders in 60 days → Long-term; if 1–3 orders → Visitor/Newcomer |
| **Family size** | If quantity ≥2 consistently → Family; else Single |
| **Subscriber** | If orders weekly tiffin product → Yes |
| **Regular** | If ≥3 orders → Yes |
| **Dormant** | If last order >30 days ago → Yes |
| **High-value** | If total spent ≥₹2,500 → Yes |
| **Wellness customer** | If ever ordered wellness/dietary product → Yes |
| **Advocate** | If referred someone → Yes |

---

## Daily 2-Minute Habit

When a customer messages:

1. **Take the order** — note product, quantity, price, area
2. **Ask the 3 questions naturally** — area, dietary, source
3. **Save phone + name in contacts** with a WhatsApp label
4. **Log into Orders sheet** at end of day

The dashboard does the analysis. You just collect orders.

---

## WhatsApp Labels to Use

| Label | When to Use |
|-------|-------------|
| 🟢 New | First-time customer |
| 🔵 Regular | 3+ orders |
| 🟣 Subscriber | Weekly tiffin |
| 🌿 Wellness | Dietary restriction |
| 👨‍👩‍👧 Family | Multiple thalis |
| 😴 Dormant | 30+ days no order |
| ⭐ VIP | High spend / referrer |

---

## Summary: Less Work for Customer, More Insight for You

| Old Way | New Way |
|---------|---------|
| 12-question form | 3 natural chat questions |
| Customer remembers history | Self-service lookup page |
| Manual segmentation | Excel auto-segments |
| Ask for reviews | Customer sees their own loyalty progress |

---

## Next Steps

1. Use the **3-question order flow** starting today
2. Set up the **order history page** on your website
3. Update WhatsApp labels for existing customers
4. Let the Excel dashboard auto-build customer profiles

Files created:
- `tracking/lightweight-capture-guide.md`
- `tracking/whatsapp-3-question-flow.md`
- `order-history.html` (customer self-service)
- Updated `ritus-kitchen-marketing-dashboard.xlsx` with inferred segments