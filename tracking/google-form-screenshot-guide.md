# Ritu's Kitchen — Google Form Setup Screenshot Guide
## Step-by-Step with Visual Descriptions

---

## Step 1: Open Google Forms

**URL:** `https://forms.google.com`

**What you see:**
- Google Forms homepage
- Button: **+ Blank** (top left)

**Action:** Click **+ Blank**

---

## Step 2: Name Your Form

**At the top of the page:**
- Click the title field
- Delete "Untitled form"
- Type: **Ritu's Kitchen — Order Form**
- Optional: Add description: *"Order home-cooked thalis in Auroville. Pre-booking only."*

---

## Step 3: Add Question 1 — Name

**Click the + icon to add question.**

| Setting | Value |
|---------|-------|
| Question title | Your Name |
| Question type | Short answer |
| Required | ON (toggle blue) |

---

## Step 4: Add Question 2 — Phone

**Click + again.**

| Setting | Value |
|---------|-------|
| Question title | WhatsApp Phone Number |
| Question type | Short answer |
| Required | ON |

---

## Step 5: Add Question 3 — Delivery Area

| Setting | Value |
|---------|-------|
| Question title | Deliver to (area / guesthouse) |
| Question type | Short answer |
| Required | ON |

---

## Step 6: Add Question 4 — Meal Need

| Setting | Value |
|---------|-------|
| Question title | Meal need |
| Question type | Multiple choice |
| Required | ON |
| Options | Lunch, Dinner, Both, Weekly Tiffin |

**To add options:**
- Option 1: Lunch
- Option 2: Dinner
- Click **Add option** for: Both, Weekly Tiffin

---

## Step 7: Add Question 5 — Quantity

| Setting | Value |
|---------|-------|
| Question title | How many people? |
| Question type | Multiple choice |
| Required | ON |
| Options | 1 person, 2 people, 3–4 people, 5+ people |

---

## Step 8: Add Question 6 — Dietary Needs

| Setting | Value |
|---------|-------|
| Question title | Dietary needs (optional) |
| Question type | Checkboxes |
| Required | OFF |
| Options | Vegan, Gluten-free, No onion-garlic, Low-oil, Mild spice, Diabetic-friendly |

---

## Step 9: Add Question 7 — Source

| Setting | Value |
|---------|-------|
| Question title | How did you hear about us? |
| Question type | Multiple choice |
| Required | ON |
| Options | WhatsApp Group, Instagram, Google Search, Friend Referral, Guesthouse, Auroville Notice Board, Auroville Today / Radio, Other |

---

## Step 10: Add Question 8 — Referrer

| Setting | Value |
|---------|-------|
| Question title | Who referred you? |
| Question type | Short answer |
| Required | OFF |
| **Conditional logic:** Show only if "Source" = "Friend Referral" |

**To add conditional logic:**
1. Click the **three dots** on the question → **Show section based on answer**
2. Wait — better method:
3. Click **Settings** (gear icon at top)
4. Click **Presentation**
5. Or use the question-level three dots → **Response validation**

Actually, for simple Google Forms, conditional logic is:
- Click the three dots on Question 7
- Select **Go to section based on answer**
- But for hiding Question 8, the easiest way is to skip conditional and just keep it optional.

**Simpler approach:** Leave Question 8 always visible and optional. Ritu can ignore blank answers.

---

## Step 11: Add Question 9 — Notes

| Setting | Value |
|---------|-------|
| Question title | Anything else? |
| Question type | Paragraph |
| Required | OFF |
| Help text | Delivery time, allergies, special request... |

---

## Step 12: Link to Google Sheets

1. Click **Responses** tab at the top
2. Click the green **Google Sheets icon**
3. A popup appears: **Select destination for responses**
4. Choose **Create a new spreadsheet**
5. Click **Create**
6. Google Sheets opens in a new tab
7. Sheet name: **Ritu's Kitchen — Orders (Responses)**

**What you see in the sheet:**
- Row 1: Timestamp, Your Name, WhatsApp Phone Number, Deliver to, Meal need, How many people?, Dietary needs, How did you hear about us?, Who referred you?, Anything else?
- Each form submission becomes one row

---

## Step 13: Get the Form Action URL

1. In Google Forms, click **Send** (top right)
2. Click the **link icon** (second tab)
3. Copy the URL. It looks like:
   ```
   https://docs.google.com/forms/d/e/1FAIpQLSdXxxxxxxxxxxxxxxxxxxx/viewform
   ```
4. Replace `/viewform` with `/formResponse`:
   ```
   https://docs.google.com/forms/d/e/1FAIpQLSdXxxxxxxxxxxxxxxxxxxx/formResponse
   ```
5. Save this URL as your `GOOGLE_FORM_ACTION`

---

## Step 14: Get Field Entry IDs (The Tricky Part)

### Method A: Pre-filled Link (Easiest)

1. In Google Forms, click the **three dots** (More options) → **Get pre-filled link**
2. A side panel opens
3. Fill in a sample value for **Your Name**:
   - Type: `TestName`
4. Click **Get link**
5. Copy the generated URL
6. Paste it in a text editor or browser address bar
7. Look for:
   ```
   entry.1234567890=TestName
   ```
8. The number after `entry.` is your **name field ID**

**Repeat for every question.**

---

## Step 15: Update order.html

Open `order.html` in a text editor.

Find this block near the bottom:

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

Replace:
- `YOUR_FORM_ID` with the long string from your form URL
- Each `entry.123456789X` with the real entry IDs you found

---

## Step 16: Test the Order Flow

1. Save `order.html`
2. Open it in a browser (double-click the file)
3. Fill in test data:
   - Name: Test Customer
   - Phone: 9876543210
   - Area: Verite Guesthouse
   - Meal: Lunch
   - Quantity: 1 person
   - Source: Instagram
4. Click **Confirm Order on WhatsApp**
5. Two things should happen:
   - WhatsApp opens (or new tab) with pre-filled message
   - Google Sheet gets a new row (check after 10–30 seconds)

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Data not appearing in Sheet | Wait 30 seconds; check form is accepting responses |
| WhatsApp doesn't open | Browser may have blocked popup; click the WhatsApp fallback button |
| Entry IDs don't work | Make sure you copied the full `entry.XXXXXXXXXX` number |
| Form says "This form is no longer accepting responses" | Go to Responses tab → Accepting responses → ON |
| Order form looks broken on phone | Make sure `order.html` is uploaded to GitHub Pages root |

---

## Alternative: Skip Google Form, Use Google Sheets API (Advanced)

If Google Forms feels fragile, you can use **Google Apps Script** to post directly to a Sheet.

But the Google Form method is free, simple, and works without API keys.

---

## Field Mapping Cheat Sheet

| Question | Variable in order.html | Entry ID Format |
|----------|------------------------|-----------------|
| Your Name | `name` | `entry.XXXXXXXXXX` |
| WhatsApp Phone Number | `phone` | `entry.XXXXXXXXXX` |
| Deliver to | `area` | `entry.XXXXXXXXXX` |
| Meal need | `meal` | `entry.XXXXXXXXXX` |
| How many people? | `quantity` | `entry.XXXXXXXXXX` |
| Dietary needs | `dietary` | `entry.XXXXXXXXXX` |
| How did you hear about us? | `source` | `entry.XXXXXXXXXX` |
| Who referred you? | `referrer` | `entry.XXXXXXXXXX` |
| Anything else? | `notes` | `entry.XXXXXXXXXX` |

---

## Your Final Form URL (Fill In)

**Form URL:** `https://docs.google.com/forms/d/e/________________/viewform`

**Form Response URL (for order.html):** `https://docs.google.com/forms/d/e/________________/formResponse`

**Google Sheet:** `https://docs.google.com/spreadsheets/d/________________/edit`

---

After setup, your orders will flow automatically:

`Customer fills order.html` → `Data saves to Google Form` → `Google Sheet updates` → `WhatsApp opens for confirmation`

You just confirm and cook.