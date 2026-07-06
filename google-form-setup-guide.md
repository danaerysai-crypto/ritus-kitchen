# Ritu's Kitchen — Google Form Order Integration

This guide creates a live Google Form and wires it into `order.html` so every order is logged in a Google Sheet.

---

## Step 1: Create the Google Form

1. Go to **https://forms.google.com**
2. Sign in as **rituskitchen.av@gmail.com**
3. Create a blank form
4. **Title:** `Ritu's Kitchen — Order Form`
5. **Description:** `Pre-book your home-cooked thali. We confirm via WhatsApp.`

---

## Step 2: Add These Questions (Exact Order)

| # | Question | Type | Required | Options / Notes |
|---|----------|------|----------|-----------------|
| 1 | Your Name | Short answer | ✅ | |
| 2 | WhatsApp Phone Number | Short answer | ✅ | |
| 3 | Deliver to (area / guesthouse) | Short answer | ✅ | |
| 4 | Meal need | Multiple choice | ✅ | Lunch, Dinner, Both, Weekly Tiffin |
| 5 | How many people? | Multiple choice | ✅ | 1 person, 2 people, 3–4 people, 5+ people |
| 6 | Dietary needs | Checkboxes | ⬜ | Vegan, Gluten-free, No onion-garlic, Low-oil, Mild spice, Diabetic-friendly |
| 7 | How did you hear about us? | Multiple choice | ✅ | WhatsApp Group, Instagram, Google Search, Friend Referral, Guesthouse, Auroville Notice Board, Auroville Today / Radio, Other |
| 8 | Who referred you? | Short answer | ⬜ | Only show if "Friend Referral" selected |
| 9 | Anything else? | Paragraph | ⬜ | |

---

## Step 3: Get the Form Action URL

1. Click **Send** → **Link icon** → copy URL
2. It looks like:
   ```
   https://docs.google.com/forms/d/e/1FAIpQLSdXxxxxxxxxxxxxxxxxxxx/viewform
   ```
3. Replace `/viewform` with `/formResponse`:
   ```
   https://docs.google.com/forms/d/e/1FAIpQLSdXxxxxxxxxxxxxxxxxxxx/formResponse
   ```
4. Save this as `GOOGLE_FORM_ACTION`

---

## Step 4: Get Field Entry IDs

For each question:

1. Click the **three dots** → **Get pre-filled link**
2. Fill in a sample answer for that question only
3. Click **Get link**
4. Copy the URL. It contains something like:
   ```
   entry.1234567890=Sample+Name
   ```
5. The number after `entry.` is the field ID.
6. Repeat for all 9 questions.

---

## Step 5: Update `order.html`

Replace this block:

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

---

## Step 6: Link Responses to Google Sheet

1. In Google Form, click **Responses** tab
2. Click **Link to Sheets**
3. Choose **Create a new spreadsheet**
4. Name: `Ritu's Kitchen — Orders`
5. The sheet now auto-fills with every order

---

## Step 7: Test the Full Flow

1. Open `https://ritus-kitchen.vercel.app/order.html`
2. Fill the form
3. Click **Confirm Order on WhatsApp**
4. Check the Google Sheet for the new row
5. Check WhatsApp opens with pre-filled message

---

## Field ID Cheat Sheet (Fill In After Creating Form)

| Field | Entry ID | Sample Test Value |
|-------|----------|-------------------|
| Name | `entry.__________` | Priya Sharma |
| Phone | `entry.__________` | 9876543210 |
| Area | `entry.__________` | Verite Guesthouse |
| Meal | `entry.__________` | Lunch |
| Quantity | `entry.__________` | 1 person |
| Dietary | `entry.__________` | Gluten-free |
| Source | `entry.__________` | Instagram |
| Referrer | `entry.__________` | (blank) |
| Notes | `entry.__________` | Deliver by 1 PM |

---

## Important Notes

- The form submits silently using `no-cors`. You won't see a success page, but data saves.
- WhatsApp is the real confirmation channel. The form captures data; WhatsApp sends the actual order.
- If Google blocks cross-origin submissions, fallback: open Google Form in a new tab.

---

## After Setup

Send the field IDs and form action URL to whoever updates `order.html`, or paste them here.
