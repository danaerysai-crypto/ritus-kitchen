# Ritu's Kitchen — Google Form Quickstart
## Create, Link, and Test in 20 Minutes

---

## Already Done

- Order form page: `order.html`
- Field mapping guide: `tracking/google-form-mapping.md`
- Screenshot guide: `tracking/google-form-screenshot-guide.md`

---

## What You Do Now

### Step 1: Create the Form

1. Go to `https://forms.google.com`
2. Sign in as **rituskitchen.av@gmail.com**
3. Click **+ Blank**
4. Title: **Ritu's Kitchen — Order Form**

---

### Step 2: Add 9 Questions (Exact Order)

| # | Question | Type | Required | Options / Notes |
|---|----------|------|----------|-----------------|
| 1 | Your Name | Short answer | Yes | |
| 2 | WhatsApp Phone Number | Short answer | Yes | |
| 3 | Deliver to (area / guesthouse) | Short answer | Yes | |
| 4 | Meal need | Multiple choice | Yes | Lunch, Dinner, Both, Weekly Tiffin |
| 5 | How many people? | Multiple choice | Yes | 1 person, 2 people, 3–4 people, 5+ people |
| 6 | Dietary needs (optional) | Checkboxes | No | Vegan, Gluten-free, No onion-garlic, Low-oil, Mild spice, Diabetic-friendly |
| 7 | How did you hear about us? | Multiple choice | Yes | WhatsApp Group, Instagram, Google Search, Friend Referral, Guesthouse, Auroville Notice Board, Auroville Today / Radio, Other |
| 8 | Who referred you? | Short answer | No | Optional |
| 9 | Anything else? | Paragraph | No | Delivery time, allergies, special request |

---

### Step 3: Link to Google Sheet

1. Click **Responses** tab
2. Click the **green Google Sheets icon**
3. Choose **Create a new spreadsheet**
4. Name it: **Ritu's Kitchen — Orders**
5. Click **Create**

---

### Step 4: Get Form Action URL

1. Click **Send** (top right)
2. Click **link icon**
3. Copy the URL
4. It looks like:
   ```
   https://docs.google.com/forms/d/e/1FAIpQLSdX.../viewform
   ```
5. Replace `/viewform` with `/formResponse`:
   ```
   https://docs.google.com/forms/d/e/1FAIpQLSdX.../formResponse
   ```

This is your `GOOGLE_FORM_ACTION`.

---

### Step 5: Get Field Entry IDs

1. Click the **three dots** on a question → **Get pre-filled link**
2. Fill sample answer for that one question
3. Click **Get link**
4. Copy the generated URL
5. Paste it and find:
   ```
   entry.1234567890=YourAnswer
   ```
6. The number is the field ID

Repeat for all 9 questions.

---

### Step 6: Update order.html

Open `order.html` and replace:

```javascript
const GOOGLE_FORM_ACTION = 'https://docs.google.com/forms/d/e/YOUR_FORM_ID/formResponse';
const GOOGLE_FORM_FIELDS = {
  name: 'entry.1234567890',
  phone: 'entry.1234567891',
  area: 'entry.1234567892',
  meal: 'entry.1234567893',
  quantity: 'entry.1234567894',
  dietary: 'entry.1234567895',
  source: 'entry.1234567896',
  referrer: 'entry.1234567897',
  notes: 'entry.1234567898'
};
```

With your real values.

---

### Step 7: Test End-to-End

1. Open `order.html` in browser
2. Fill the form with test data
3. Click **Confirm Order on WhatsApp**
4. Check:
   - WhatsApp opens with correct message
   - Google Sheet has new row
5. If both work → done

---

### Step 8: Sync to Excel (Optional)

Run the sync script once you publish the Sheet as CSV:

```bash
cd /c/Users/Admin/Desktop/projects/ritus-kitchen/tracking
python sync_orders.py
```

See `tracking/google-sheet-sync-guide.md` for full setup.

---

## Cheat Sheet: Fill After Form Creation

| Field | Entry ID | Sample Value |
|-------|----------|--------------|
| Your Name | `entry.__________` | Priya Sharma |
| WhatsApp Phone | `entry.__________` | 9876543210 |
| Deliver to | `entry.__________` | Verite Guesthouse |
| Meal need | `entry.__________` | Lunch |
| How many people | `entry.__________` | 1 person |
| Dietary needs | `entry.__________` | Vegan |
| How heard | `entry.__________` | Instagram |
| Referrer | `entry.__________` | (blank) |
| Anything else | `entry.__________` | Deliver by 1 PM |

---

## Common Issues

| Issue | Fix |
|-------|-----|
| Google Sheet not updating | Make sure form is accepting responses |
| order.html doesn't send data | Check GOOGLE_FORM_ACTION URL ends with `/formResponse` |
| Wrong data in columns | Entry IDs are in wrong order; recheck each one |
| WhatsApp doesn't open | Browser blocked popup; click fallback link |

---

## Your Live Links (After GitHub Pages Fix)

- Order page: `https://danaerysai-crypto.github.io/ritus-kitchen/order.html`
- Order responses: Your Google Sheet
- Admin logger: `https://danaerysai-crypto.github.io/ritus-kitchen/admin.html`

---

## Next

After the form is live, test it yourself and place one test order. Then we activate social media scheduling.