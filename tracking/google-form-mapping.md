# Google Form Field Mapping for Ritu's Kitchen Order Page

## Step-by-Step Setup

### 1. Create the Google Form

Go to `https://forms.google.com` and create a blank form.

**Title:** Ritu's Kitchen — Order Form

---

### 2. Add These Questions (Exact Order)

| # | Question | Type | Options / Notes |
|---|----------|------|-----------------|
| 1 | Your Name | Short answer | Required |
| 2 | WhatsApp Phone Number | Short answer | Required |
| 3 | Deliver to (area / guesthouse) | Short answer | Required |
| 4 | Meal need | Multiple choice | Lunch, Dinner, Both, Weekly Tiffin |
| 5 | How many people? | Multiple choice | 1 person, 2 people, 3–4 people, 5+ people |
| 6 | Dietary needs | Checkboxes | Vegan, Gluten-free, No onion-garlic, Low-oil, Mild spice, Diabetic-friendly |
| 7 | How did you hear about us? | Multiple choice | WhatsApp Group, Instagram, Google Search, Friend Referral, Guesthouse, Auroville Notice Board, Auroville Today / Radio, Other |
| 8 | Who referred you? | Short answer | (Optional, only show if "Friend Referral" selected) |
| 9 | Anything else? | Paragraph | Optional |

---

**Email:** rituskitchen.av@gmail.com

## 3. Get the Form Action URL

1. Click **Send** → **Link icon** → copy the form URL
2. It looks like:
   ```
   https://docs.google.com/forms/d/e/1FAIpQLSdXxxxxxxxxxxxxxxxxxxx/viewform
   ```
3. Replace `/viewform` with `/formResponse`:
   ```
   https://docs.google.com/forms/d/e/1FAIpQLSdXxxxxxxxxxxxxxxxxxxx/formResponse
   ```
4. This is your `GOOGLE_FORM_ACTION`.

---

### 4. Get Field Entry IDs

For each question:

1. Click the **three dots** → **Get pre-filled link**
2. Fill in a sample answer for that question
3. Click **Get link**
4. Copy the URL. It will contain something like:
   ```
   entry.1234567890=Sample+Name
   ```
5. The number after `entry.` is your field ID.

Repeat for every question.

---

### 5. Update `order.html`

Replace these placeholders in `order.html`:

```javascript
const GOOGLE_FORM_ACTION = 'https://docs.google.com/forms/d/e/YOUR_FORM_ID/formResponse';
const GOOGLE_FORM_FIELDS = {
  name: 'entry.YOUR_NAME_FIELD_ID',
  phone: 'entry.YOUR_PHONE_FIELD_ID',
  area: 'entry.YOUR_AREA_FIELD_ID',
  meal: 'entry.YOUR_MEAL_FIELD_ID',
  quantity: 'entry.YOUR_QUANTITY_FIELD_ID',
  dietary: 'entry.YOUR_DIETARY_FIELD_ID',
  source: 'entry.YOUR_SOURCE_FIELD_ID',
  referrer: 'entry.YOUR_REFERRER_FIELD_ID',
  notes: 'entry.YOUR_NOTES_FIELD_ID'
};
```

---

### 6. Link Responses to Google Sheet

1. In Google Form, click **Responses** tab
2. Click **Link to Sheets**
3. Choose **Create a new spreadsheet**
4. Name it: `Ritu's Kitchen — Orders`

---

### 7. Test the Full Flow

1. Open `order.html` in browser
2. Fill the form
3. Submit
4. Check the Google Sheet for the new row
5. Check WhatsApp — it should open with pre-filled message

---

## Field ID Cheat Sheet (Fill In After Creating Form)

| Field | Entry ID | Sample Test Value |
|-------|----------|-------------------|
| Name | `entry.__________` | Priya Sharma |
| Phone | `entry.__________` | 9876543210 |
| Area | `entry.__________` | Verite Guesthouse |
| Meal | `entry.__________` | Lunch |
| Quantity | `entry.__________` | 1 person |
| Dietary | `entry.__________` | Mild spice |
| Source | `entry.__________` | Instagram |
| Referrer | `entry.__________` | (blank) |
| Notes | `entry.__________` | Deliver by 1 PM |

---

## Important Notes

- Google Forms submission from a custom page uses `mode: 'no-cors'` — you won't see a success response, but the data still saves.
- WhatsApp is the real confirmation channel. The form captures data silently; WhatsApp opens for the customer to send the actual order.
- If Google blocks cross-origin submissions in the future, fall back to: form opens Google Form in new tab → customer submits → WhatsApp opens.

---

## Alternative: Simple Mailto/Sheet-free Version

Email: **rituskitchen.av@gmail.com**

If Google Forms feels complex, just use `mailto:` or a simple `mailto` + WhatsApp combo. But Google Forms + Sheet is strongly recommended for automation.