# WhatsApp Automation Templates
## Quick Replies + Broadcasts for Hands-Free Operation

---

## How to Set Up Quick Replies in WhatsApp Business

1. Open WhatsApp Business
2. Tap **More options** → **Business tools** → **Quick replies**
3. Tap **Add** (+)
4. Enter:
   - **Message:** Copy template below
   - **Shortcut:** e.g. `/menu`
5. Save
6. In chat, type `/menu` → it appears

---

## Order Intake Templates

### `/order` — Direct customer to order form
> Hi! 🍛 You can place your order here — it takes 30 seconds and Ritu gets all the details:
>
> https://ritus-kitchen.vercel.app/order.html?utm_source=whatsapp&utm_medium=chat&utm_campaign=direct_order
>
> Or just reply with: name, area, meal (lunch/dinner/both), and dietary needs.

### `/menu` — Today's menu
> 🍛 *Today's Thali — Ritu's Kitchen*
> 
> [Dal], [Sabzi], [Roti], [Rice], [Salad], [Papad], [Pickle]
> 
> ₹220 | Pre-book by 11 AM for lunch, 6 PM for dinner.
> 
> Order: https://ritus-kitchen.vercel.app/order.html

### `/tiffin` — Weekly subscription
> 📅 *Weekly Tiffin — Ritu's Kitchen*
>
> 5 home-cooked meals — ₹1,100
> No daily ordering. Delivered fresh.
>
> Customizable: vegan, gluten-free, low-oil, mild spice.
>
> Subscribe: https://ritus-kitchen.vercel.app/order.html

---

## Follow-Up Templates

### `/thanks` — After delivery
> Hi [Name], hope you enjoyed today's thali! 🍛
> 
> A quick 30-second feedback helps Ritu serve you better:
> [Google Form link]
> 
> Thank you! 🙏

### `/review` — Ask for Google review
> Hi [Name]! 🙏 If Ritu's Kitchen made your day better, a quick Google review helps more Aurovilians find home-cooked food.
> 
> [Google review link]
> 
> Thank you for supporting us!

### `/feedback2` — Two-question follow-up
> Hi [Name]! Quick 2-tap feedback:
> 1. How was your meal? 😍 / 🙂 / 😐
> 2. Will you order again this week? Yes / Maybe / No
> 
> Just reply with emojis/words. Thank you!

---

## Retention Templates

### `/winback` — Dormant customer
> Hi [Name], we haven't served you in a while! 🍛 We'd love to cook for you again.
> 
> This week's special: [dish]. Pre-book here:
> https://ritus-kitchen.vercel.app/order.html
>
> Reply YES and I'll save a thali for you.

### `/renew` — Weekly tiffin expiry
> Hi [Name], your weekly tiffin plan ends this week. 🍛
> 
> Want to renew for next week? 5 meals — ₹1,100.
> 
> Reply RENEW and I'll set it up.

### `/loyalty` — Reward repeat customer
> Hi [Name], you've ordered [X] thalis with us! 🌟
> 
> As a thank you, your next thali is ₹50 off.
> 
> Use it any time this week.

---

## Broadcast / Status Captions

### Morning status (daily)
🍛 Today's Thali — ₹220
[Menu items]
Pre-book by 11 AM
Order: [link]

### Evening status (daily)
🌙 Tomorrow's Thali — pre-book tonight
[Menu preview]
Weekly tiffin also available
Order: [link]

### Festival / special offer
🪔 [Festival] Special Box — ₹450
Limited boxes. Pre-order by [date].
Order: [link]

---

## New Customer Onboarding Flow

When a new customer first messages:

1. **Reply with `/order`** — send them to the form
2. **After first delivery, send `/thanks`** — get feedback
3. **If feedback is positive, send `/review`** — Google review
4. **After 3 orders, send `/tiffin`** — upsell subscription
5. **After 10 orders, send `/loyalty`** — reward

---

## VIP Customer Flow

For high-value / frequent customers:

1. **Priority confirmation** — "Saved for you, [Name]"
2. **Personal note** — "I made it extra mild like you prefer"
3. **Early access** — "New festival box — want one before I announce it?"
4. **Referral request** — "Know anyone who'd love home food?"

---

## Automation Rules

| Trigger | Action | Template |
|---------|--------|----------|
| New customer messages | Send order form | `/order` |
| Order delivered | Feedback request | `/thanks` |
| Positive feedback | Google review ask | `/review` |
| 3+ orders | Weekly tiffin upsell | `/tiffin` |
| 10+ orders | Loyalty reward | `/loyalty` |
| 30+ days no order | Win-back | `/winback` |
| Tiffin expiring | Renewal | `/renew` |
| Daily 8 AM | Status post | Morning status |
| Daily 7 PM | Status post | Evening status |

---

## Pro Tips

- Keep WhatsApp Business **labels** updated: New, Regular, Subscriber, Wellness, Dormant, VIP
- Use **broadcast lists** by label, not just one big list
- Personalize templates with customer name when possible
- Don't send more than 1 broadcast per day to avoid spam feel
- Always include an easy way to opt out: "Reply STOP to pause updates"

---

## Stop / Opt-Out Message

If someone wants fewer messages:

> No problem at all. I'll pause updates. Just message "ORDER" anytime when you'd like a thali. 🙏

This keeps the door open without annoying them.