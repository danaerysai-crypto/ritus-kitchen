# Ritu's Kitchen — Full Automation Blueprint
## Run Marketing + Orders Without Daily Interference

---

## What Can Be Automated Today (Free)

| Task | Tool | Your Effort |
|------|------|-------------|
| **Order form on website** | `order.html` | Customer fills it; WhatsApp opens automatically |
| **Order data → Google Sheet** | Google Form backend | Zero effort after setup |
| **Daily menu broadcast** | WhatsApp Business labels + scheduled message | 2 min/day to trigger or cron |
| **Customer follow-up after order** | WhatsApp Business saved replies | One tap |
| **Social media scheduling** | Meta Business Suite | 1 hour/week batch schedule |
| **Review request** | WhatsApp quick reply | One tap after delivery |
| **Dormant customer win-back** | WhatsApp label + weekly reminder | 15 min/week |
| **Analytics dashboard** | Google Sheets/Excel | Auto-updates from form |
| **UTM link tracking** | Google Analytics + Bitly | Set once, track forever |

---

## What Still Needs You (For Now)

| Task | Why |
|------|-----|
| **Cooking** | Ritu makes the food |
| **Packing** | Physical task |
| **Delivery** | Human courier |
| **Final order confirmation** | WhatsApp confirmation from Ritu |
| **Custom dietary requests** | Requires human judgment |
| **Handling complaints** | Personal touch matters |
| **Cash/UPI reconciliation** | Manual until POS integrated |

---

## The Fully Automated Customer Journey

### Step 1: Customer Discovers You
- Instagram post / WhatsApp status / Google search / flyer
- UTM link points to `https://ritus-kitchen.vercel.app/order.html`

### Step 2: Customer Orders Online
- Fills `order.html` (name, phone, area, meal, quantity, dietary, source)
- Form auto-submits to Google Sheet
- WhatsApp opens with pre-filled message to Ritu
- Customer sends it — order request complete

### Step 3: Order Data Auto-Logs
- Google Sheet captures all fields
- Excel dashboard pulls from Google Sheet (manual sync or via API)
- Customer is tagged by source and dietary need

### Step 4: Follow-Up Automation
- After delivery, send one-tap WhatsApp: "Hope you enjoyed! Quick feedback: [link]"
- Feedback goes into another Google Sheet
- Positive feedback → ask for Google review
- Negative feedback → Ritu handles personally

### Step 5: Retention Automation
- Weekly: check dormant customers (30+ days)
- Send win-back message via WhatsApp
- Weekly tiffin expiry reminder before renewal
- Festival box pre-order announcements

### Step 6: Marketing Automation
- Meta Business Suite schedules 7 posts/week
- Daily WhatsApp status update (manual photo + saved caption)
- Google Business posts scheduled weekly

---

## Automation Stack

| Layer | Tool | Purpose |
|-------|------|---------|
| **Landing + order capture** | GitHub Pages + `order.html` | 24/7 order intake |
| **Data pipeline** | Google Forms → Google Sheets | Auto-capture + storage |
| **Communication** | WhatsApp Business + quick replies | Confirmation + follow-up |
| **Social scheduling** | Meta Business Suite | Free Instagram/Facebook scheduling |
| **Short links + tracking** | Bitly + UTM | Know what converts |
| **Analytics** | Google Analytics 4 + Sheets/Excel | Traffic + revenue insights |
| **Review generation** | Google review link + WhatsApp | Build social proof |
| **Win-back** | WhatsApp labels + weekly checklist | Recover lost customers |

---

## Setup Checklist to Go Hands-Free

### Phase 1: Order Form Automation (2 hours)
- [ ] Create Google Form with the fields in `order.html`
- [ ] Get the form action URL and entry IDs
- [ ] Replace `GOOGLE_FORM_ACTION` and `GOOGLE_FORM_FIELDS` in `order.html`
- [ ] Link Google Form responses to a Google Sheet
- [ ] Add "Order Now" buttons to `index.html` and WhatsApp bio
- [ ] Test by submitting a fake order

### Phase 2: Daily Broadcast Automation (1 hour)
- [ ] Save 7 WhatsApp broadcast templates (one per day)
- [ ] Create WhatsApp Business labels: New, Regular, Subscriber, Wellness, Dormant
- [ ] Each morning: copy-paste today's menu + photo to status + broadcast groups
- [ ] Use `/menu`, `/order`, `/tiffin` quick replies

### Phase 3: Social Media Automation (2 hours/week)
- [ ] Create Meta Business Suite account
- [ ] Connect Instagram + Facebook
- [ ] Batch-create 7 posts every Sunday
- [ ] Schedule for the week
- [ ] Use UTM links in every post

### Phase 4: Follow-Up Automation (30 min setup)
- [ ] Create WhatsApp quick reply `/thanks` with feedback link
- [ ] Create `/review` quick reply with Google review link
- [ ] Create `/winback` quick reply for dormant customers
- [ ] Set Sunday reminder to check dormant list

### Phase 5: Dashboard Automation (1 hour)
- [ ] Link Excel dashboard to Google Sheets via `Data → Get Data → From Web` or copy-paste weekly
- [ ] Set up Google Analytics 4 with real ID
- [ ] Connect Google Business Profile Insights monthly

---

## Google Form Field Mapping for `order.html`

After creating your Google Form, right-click each field → Inspect → find `name="entry.XXXXXXXXXX"`.

Replace these in `order.html`:

| Field | Placeholder in Code |
|-------|---------------------|
| Name | `entry.1234567890` |
| Phone | `entry.1234567891` |
| Area | `entry.1234567892` |
| Meal | `entry.1234567893` |
| Quantity | `entry.1234567894` |
| Dietary | `entry.1234567895` |
| Source | `entry.1234567896` |
| Referrer | `entry.1234567897` |
| Notes | `entry.1234567898` |

---

## One-Hour-Per-Week Routine (After Setup)

| Day | Time | Task | Duration |
|-----|------|------|----------|
| Sunday | 10 AM | Schedule 7 social posts | 45 min |
| Sunday | 11 AM | Review dashboard, plan experiment | 15 min |
| Daily | 8 AM | Post WhatsApp status + broadcast | 5 min |
| Daily | 1 PM | Confirm orders, send `/thanks` | 10 min |
| Daily | 7 PM | Post tomorrow's menu status | 5 min |
| Sunday | 12 PM | Send win-back to dormant customers | 15 min |

**Total active time: ~2 hours/week.**

---

## The Ultimate Goal

Customer finds you → orders online → data logs itself → follow-up sends → reviews come in → dashboard shows what works → you just cook and deliver.

---

## Files Created

- `automation-blueprint.md` — this full plan
- `order.html` — self-service order page
- `tracking/google-form-mapping.md` — field mapping guide
- `tracking/weekly-automation-routine.md` — minimal weekly tasks
- `tracking/whatsapp-automation-templates.md` — quick replies for automation

---

## Next Action

1. Create the Google Form
2. Update `order.html` with real form IDs
3. Add "Order Now" link everywhere (website, Instagram bio, WhatsApp status, flyers)
4. Test one end-to-end order

Want me to create the exact Google Form questions and field mapping document so you only need to copy-paste into Google Forms?