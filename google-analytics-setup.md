# Google Analytics 4 Setup for Ritu's Kitchen
## Track Website Visitors, Orders, and Marketing Performance

---

## What You Need

- Google account: **rituskitchen.av@gmail.com**
- Website URL: `https://ritus-kitchen.vercel.app/`
- 15 minutes

---

## Step 1: Create GA4 Property

1. Go to `https://analytics.google.com/analytics/academy/`
   - Or directly: `https://analytics.google.com`
2. Click **Start measuring**
3. **Account name:** Ritu's Kitchen
4. Click **Next**
5. **Property name:** Ritu's Kitchen Website
6. **Reporting time zone:** (GMT+05:30) India Time
7. **Currency:** Indian Rupee
8. Click **Next**
9. Fill business details:
   - **Industry category:** Food & Drink
   - **Business size:** Small
   - **Intent:** Get baseline reports, improve customer experience, generate more leads
10. Click **Create**
11. Accept Google Analytics Terms of Service

---

## Step 2: Create Web Data Stream

1. Choose **Web** platform
2. **Website URL:** `https://ritus-kitchen.vercel.app`
3. **Stream name:** Website
4. Click **Create stream**

---

## Step 3: Get Measurement ID

1. After creating the stream, you see a page with:
   - **Measurement ID:** `G-XXXXXXXXXX`
   - **Tagging instructions**
2. Copy the Measurement ID
3. It looks like `G-ABC123DEF0`

---

## Step 4: Add GA4 Code to Website Files

Replace `G-XXXXXXXXXX` in these files with your real ID:

1. `index.html`
2. `order.html`
3. `order-history.html`
4. `admin.html`

The code block looks like this in each file:

```html
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

Replace both occurrences of `G-XXXXXXXXXX` in each file.

---

## Step 5: Push Updated Files to GitHub

```bash
cd /c/Users/Admin/Desktop/projects/ritus-kitchen
git add .
git commit -m "Add real Google Analytics 4 ID"
git push origin main
```

---

## Step 6: Verify Data is Coming In

1. Wait 2 minutes after pushing
2. Open live website:
   `https://ritus-kitchen.vercel.app/`
3. In GA4, go to **Home** → **Realtime** report
4. You should see at least **1 user** on the site

---

## Step 7: Set Up Key Events (Conversions)

Track what actually matters for Ritu's Kitchen.

### Event 1: Order Form Started

In `order.html`, the form start is already tracked:

```javascript
gtag('event', 'begin_checkout');
```

### Event 2: Order Submitted

When customer clicks **Confirm Order on WhatsApp**:

```javascript
gtag('event', 'purchase', {
  value: price,
  currency: 'INR'
});
```

### Event 3: Admin Order Logged

In `admin.html`:

```javascript
gtag('event', 'admin_order_logged');
```

---

## Step 8: Mark Important Events as Conversions

1. In GA4, go to **Admin** (gear icon)
2. Under **Property**, click **Events**
3. Find these events:
   - `purchase`
   - `begin_checkout`
   - `admin_order_logged`
4. Toggle **Mark as conversion** for `purchase`

---

## Step 9: Add UTM Tracking to All Links

Use UTM parameters on every external link so you know which channel drives orders.

### Example UTM Link for Instagram Bio

```
https://ritus-kitchen.vercel.app/order.html?utm_source=instagram&utm_medium=bio&utm_campaign=organic
```

### Example UTM Link for WhatsApp Status

```
https://ritus-kitchen.vercel.app/order.html?utm_source=whatsapp&utm_medium=status&utm_campaign=daily_thali
```

### Example UTM Link for Google Business Profile

```
https://ritus-kitchen.vercel.app/order.html?utm_source=google_business&utm_medium=profile&utm_campaign=local_search
```

---

## Step 10: Create a Simple Report

1. In GA4, go to **Explore** → **Free form**
2. Add dimensions:
   - **Session source**
   - **Session medium**
   - **Page title**
3. Add metrics:
   - **Sessions**
   - **Conversions (purchase)**
   - **Event count**
4. Save as: **Ritu's Kitchen — Marketing Channels**

---

## What You Can Track

| Metric | Where to Find |
|--------|---------------|
| Website visitors | Home → Realtime / Reports → Engagement → Overview |
| Order page views | Reports → Engagement → Pages and screens |
| Orders started | Events → begin_checkout |
| Orders completed | Events → purchase |
| Top traffic sources | Reports → Acquisition → Traffic acquisition |
| Mobile vs desktop | Reports → Tech → Overview |
| Auroville vs outside | Reports → Demographics → Demographic details |

---

## Monthly Review

On the last Sunday of each month:

1. Open GA4
2. Go to **Reports → Acquisition → Traffic acquisition**
3. Note top 3 sources
4. Compare with Excel dashboard sources
5. Double down on what works
6. Cut what doesn't

---

## Your GA4 IDs (Fill In)

| Item | Value |
|------|-------|
| Measurement ID | `G-__________` |
| Stream ID | __________ |
| Property ID | __________ |

---

## Next Step

After GA4 is set up, create the **Google Form** and link `order.html` so orders are automatically tracked.