# Ritu's Kitchen — Google Sheets → Excel Sync Script
## Auto-Sync Orders from Google Sheet to Local Excel Dashboard

---

## What This Does

This Python script downloads your Google Sheet responses and updates your local `ritus-kitchen-marketing-dashboard.xlsx`.

**Run it once a day or once a week.** No manual copy-paste.

---

## Option 1: Simple CSV Download (No API Keys)

### Step 1: Publish Google Sheet as CSV

1. Open your Google Sheet: `Ritu's Kitchen — Orders (Responses)`
2. Click **File** → **Share** → **Share with others**
3. Click **Copy link**
4. Change sharing to **Anyone with the link** → **Viewer**
5. Click **Copy link**
6. Note the Sheet ID from the URL:
   ```
   https://docs.google.com/spreadsheets/d/[SHEET_ID]/edit
   ```
7. Click **File** → **Share** → **Publish to web**
8. Select the **responses sheet**
9. Choose **Comma-separated values (.csv)**
10. Click **Publish**
11. Copy the URL. It looks like:
    ```
    https://docs.google.com/spreadsheets/d/e/2PACX-.../pub?gid=0&single=true&output=csv
    ```

### Step 2: Run the Sync Script

```bash
cd /c/Users/Admin/Desktop/projects/ritus-kitchen/tracking
python sync_orders.py
```

### sync_orders.py

```python
import pandas as pd
import requests
from openpyxl import load_workbook

# Replace with your published CSV URL
GOOGLE_SHEET_CSV_URL = "https://docs.google.com/spreadsheets/d/e/YOUR_SHEET_ID/pub?gid=0&single=true&output=csv"

# Load CSV from Google Sheet
response = requests.get(GOOGLE_SHEET_CSV_URL)
df = pd.read_csv(pd.io.common.StringIO(response.text))

# Rename columns to match dashboard
column_map = {
    "Timestamp": "Date",
    "Your Name": "Customer Name",
    "WhatsApp Phone Number": "Phone",
    "How did you hear about us?": "Source",
    "Deliver to (area / guesthouse)": "Delivery Area",
    "Meal need": "Product",
    "How many people?": "Quantity",
    "Dietary needs (optional)": "Dietary Note",
    "Who referred you?": "Referral By",
    "Anything else?": "Notes"
}

df = df.rename(columns=column_map)

# Convert timestamp to date only
df["Date"] = pd.to_datetime(df["Date"]).dt.strftime("%Y-%m-%d")

# Map meal to product
product_prices = {
    "Lunch": ("Today's Thali", 220),
    "Dinner": ("Today's Thali", 220),
    "Both": ("Today's Thali", 440),
    "Weekly Tiffin": ("Weekly Tiffin", 1100)
}

df[["Product", "Price"]] = df["Product"].map(product_prices).apply(pd.Series)

# Clean quantity
df["Quantity"] = df["Quantity"].str.extract('(\d+)').fillna(1).astype(int)

# Fill missing fields
df["UTM Campaign"] = "website_order_form"
df["Payment Mode"] = "Pending"
df["New or Repeat"] = "New"  # You can update this manually later

# Select and order columns
output_cols = [
    "Date", "Customer Name", "Phone", "Source", "UTM Campaign",
    "Product", "Quantity", "Price", "Payment Mode", "Delivery Area",
    "Dietary Note", "New or Repeat", "Referral By", "Notes"
]
df = df[output_cols]

# Load Excel workbook
wb = load_workbook("ritus-kitchen-marketing-dashboard.xlsx")
ws = wb["Orders"]

# Clear existing data except header
ws.delete_rows(2, ws.max_row)

# Write new data
for row in df.itertuples(index=False):
    ws.append(list(row))

wb.save("ritus-kitchen-marketing-dashboard.xlsx")
print(f"Synced {len(df)} orders to Excel dashboard.")
```

---

## Option 2: Using gspread (More Control)

### Install

```bash
pip install gspread oauth2client
```

### Setup Google Service Account

1. Go to `https://console.cloud.google.com/`
2. Create a project: **Ritu's Kitchen**
3. Enable **Google Sheets API**
4. Create a **Service Account**
5. Download the JSON key file
6. Share your Google Sheet with the service account email (found in JSON)
7. Save the JSON as `service-account.json` in `tracking/`

### sync_orders_gspread.py

```python
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from openpyxl import load_workbook

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('service-account.json', scope)
client = gspread.authorize(creds)

sheet = client.open("Ritu's Kitchen — Orders (Responses)").sheet1
rows = sheet.get_all_records()

# Process rows into dashboard format
# ... same logic as above ...

wb = load_workbook("ritus-kitchen-marketing-dashboard.xlsx")
ws = wb["Orders"]
ws.delete_rows(2, ws.max_row)

for row in rows:
    # Map and append
    pass

wb.save("ritus-kitchen-marketing-dashboard.xlsx")
print(f"Synced {len(rows)} orders.")
```

---

## Option 3: Windows Scheduled Task (Run Automatically)

### Create a batch file: `sync_orders.bat`

```batch
@echo off
cd /d C:\Users\Admin\Desktop\projects\ritus-kitchen\tracking
python sync_orders.py
```

### Schedule it daily

1. Press **Win + R** → type `taskschd.msc` → Enter
2. Click **Create Basic Task**
3. Name: **Ritu's Kitchen Order Sync**
4. Trigger: **Daily** at 11:00 PM
5. Action: **Start a program**
6. Program: browse to `sync_orders.bat`
7. Finish

Now your Excel dashboard updates every night automatically.

---

## Requirements

```bash
pip install pandas openpyxl requests
```

---

## What Gets Synced

| From Google Sheet | To Excel Orders Sheet |
|-------------------|-----------------------|
| Timestamp | Date |
| Your Name | Customer Name |
| WhatsApp Phone Number | Phone |
| How did you hear about us? | Source |
| Meal need | Product (mapped to prices) |
| How many people? | Quantity |
| Deliver to | Delivery Area |
| Dietary needs | Dietary Note |
| Who referred you? | Referral By |
| Anything else? | Notes |

---

## Notes

- Keep a backup of your Excel file before first sync
- "New or Repeat" is set to "New" by default — update manually or add lookup logic
- Payment mode defaults to "Pending" — update after payment
- Run the script before your Sunday review for fresh data

---

## Simpler Alternative

If scripting is too much, just:
1. Open Google Sheet every Sunday
2. Select all rows
3. Copy
4. Paste into Excel Orders tab
5. Run formulas

This takes 2 minutes and is completely fine for a one-woman kitchen.