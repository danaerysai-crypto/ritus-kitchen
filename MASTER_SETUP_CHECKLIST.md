# Ritu's Kitchen — Master Setup Checklist
## Activate Website, Analytics, Forms, and Google Business

**Status:** Email confirmed → `rituskitchen.av@gmail.com` | Phone → +91 90431 40686

---

## Step 0: Create Google Account (Required First)

- [ ] Go to `https://accounts.google.com/signup`
- [ ] Use **rituskitchen.av@gmail.com**
- [ ] Verify with a phone number that can receive SMS
- [ ] Complete profile

**Cannot be automated.** Ritu must do this or be present for OTP.

---

## Step 1: Fix GitHub Pages (Files at Root)

### Problem
`index.html` is inside `ritus-kitchen/ritus-kitchen/` instead of repo root.

### Fix Options

#### Option A: I Run It (Needs Your Approval + Token)
1. Approve me to use your GitHub token
2. I run the deploy script
3. Done in 2 minutes

#### Option B: You Run Commands
See `deploy_to_github.md` for exact copy-paste commands.

### After Fix, Test These URLs
- [ ] `https://ritus-kitchen.vercel.app/`
- [ ] `https://ritus-kitchen.vercel.app/order.html`
- [ ] `https://ritus-kitchen.vercel.app/order-history.html`
- [ ] `https://ritus-kitchen.vercel.app/admin.html`

---

## Step 2: Set Up Google Analytics 4

- [ ] Go to `https://analytics.google.com` while signed in as `rituskitchen.av@gmail.com`
- [ ] Click **Start measuring**
- [ ] Account name: **Ritu's Kitchen**
- [ ] Property name: **Ritu's Kitchen Website**
- [ ] Time zone: **India/Kolkata**
- [ ] Currency: **INR**
- [ ] Industry: **Food & Drink**
- [ ] Business size: **Small**
- [ ] Create Web data stream:
  - Website URL: `https://ritus-kitchen.vercel.app`
  - Stream name: **Website**
- [ ] Copy the **Measurement ID** (looks like `G-XXXXXXXXXX`)
- [ ] Replace all `G-XXXXXXXXXX` placeholders in:
  - `index.html`
  - `order.html`
  - `order-history.html`
  - `admin.html`
- [ ] Commit and push updated files
- [ ] Visit the live site and check Realtime report in GA4

---

## Step 3: Create Google Form + Link Order Page

- [ ] Go to `https://forms.google.com`
- [ ] Create blank form: **Ritu's Kitchen — Order Form**
- [ ] Add 9 questions exactly per `tracking/google-form-screenshot-guide.md`
- [ ] Link responses to new Google Sheet: **Ritu's Kitchen — Orders**
- [ ] Get form action URL (`.../formResponse`)
- [ ] Get field entry IDs using pre-filled link method
- [ ] Update `order.html` with real form action + field IDs
- [ ] Test order flow end-to-end
- [ ] Verify data appears in Google Sheet

---

## Step 4: Set Up Google Business Profile

- [ ] Go to `https://business.google.com`
- [ ] Sign in as `rituskitchen.av@gmail.com`
- [ ] Click **Add business**
- [ ] Enter **Ritu's Kitchen**
- [ ] Category: **Meal delivery**
- [ ] Add service area: **Auroville, Pondicherry, Tamil Nadu**
- [ ] Phone: **+91 90431 40686**
- [ ] Email: **rituskitchen.av@gmail.com**
- [ ] Website: `https://ritus-kitchen.vercel.app/`
- [ ] Hours: **7:00 AM – 8:00 PM daily**
- [ ] Paste description from `tracking/google-business-setup-checklist.md`
- [ ] Add photos: thali, kitchen, Ritu, delivery
- [ ] Request verification (postcard/phone/email)
- [ ] After verified, add first Google post with order link

---

## Step 5: Final Connection Checklist

- [ ] Website live on GitHub Pages
- [ ] WhatsApp click-to-chat link works
- [ ] Instagram bio updated with order link
- [ ] Google Business Profile published
- [ ] Google Analytics receiving data
- [ ] Google Form saving orders
- [ ] Excel dashboard ready for weekly use
- [ ] WhatsApp Business quick replies saved (`/order`, `/menu`, `/tiffin`, `/thanks`, `/review`, `/winback`)
- [ ] First social post scheduled

---

## Post-Launch Weekly Ritual

| Day | Task | Time |
|-----|------|------|
| Sunday | Schedule 7 social posts | 45 min |
| Sunday | Review dashboard + log orders | 15 min |
| Daily 8 AM | WhatsApp status | 5 min |
| Daily 1 PM | Confirm orders + send `/thanks` | 10 min |
| Daily 7 PM | Tomorrow's menu status | 5 min |
| Sunday | Win-back dormant customers | 15 min |

---

## Files to Reference

| Task | File |
|------|------|
| Full strategy | `automation-blueprint.md` |
| GitHub fix | `github-pages-fix-guide.md`, `deploy_to_github.md` |
| GA4 setup | `google-analytics-setup.md` |
| Google Form setup | `tracking/google-form-screenshot-guide.md`, `tracking/google-form-mapping.md` |
| GBP setup | `tracking/google-business-setup-checklist.md`, `google-business-quickstart.md` |
| Marketing routine | `tracking/weekly-automation-routine.md` |
| WhatsApp templates | `tracking/whatsapp-automation-templates.md` |
| Social content | `tracking/social-media-captions-30-days.md` |

---

## Estimated Total Setup Time

| Step | Time |
|------|------|
| Google account | 10 min |
| GitHub Pages fix | 5–30 min |
| Google Analytics | 15 min |
| Google Form | 30 min |
| Google Business Profile | 30 min |
| Final testing | 20 min |
| **Total** | **~2 hours** |

---

## Next Action

1. **Create the Google account** if not already done.
2. **Approve me to fix GitHub Pages** or run the deploy commands yourself.
3. Then we activate each Google service one by one.

Say **"fix GitHub now"** when ready to proceed.