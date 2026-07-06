# Ritu's Kitchen — Fix GitHub Pages 404 (Nested Folder Issue)
## Step-by-Step Fix with Screenshots Described

---

## The Problem

Your website files are currently inside a folder called `ritus-kitchen/` **inside** your GitHub repository `ritus-kitchen`.

GitHub Pages looks for `index.html` at the **root** of the repo, not inside a subfolder.

Because `index.html` is at `ritus-kitchen/ritus-kitchen/index.html`, the Pages URL returns **404**.

### Wrong Structure (Current)

```
ritus-kitchen/          ← this is your GitHub repo
└── ritus-kitchen/        ← this folder should not exist
    ├── index.html
    ├── menu-v2.html
    └── images/
```

### Correct Structure (Needed)

```
ritus-kitchen/          ← this is your GitHub repo
├── index.html          ← must be at the top level
├── menu-v2.html
├── order.html
├── order-history.html
├── admin.html
├── images/
└── tracking/
```

---

## Step 1: Open Your Repository on GitHub

1. Go to: `https://github.com/danaerysai-crypto/ritus-kitchen`
2. Sign in if needed
3. You will see a folder named `ritus-kitchen/` at the top level

---

## Step 2: Move All Files to the Root

### Method A: Using GitHub Web Interface (No Command Line)

1. Click on the `ritus-kitchen/` folder to open it
2. You will see files: `index.html`, `menu-v2.html`, `images/`, etc.
3. Click the **small checkbox** at the top-left of the file list to select all
4. Or select files one by one:
   - Click checkbox next to `index.html`
   - Click checkbox next to `menu-v2.html`
   - Click checkbox next to `images/`
   - Click checkbox next to `tracking/`
   - Click checkbox next to every other file/folder
5. At the top right, click the **... (three dots)** menu
6. Select **Move**
7. In the popup, delete `ritus-kitchen/` from the path
8. Leave the destination path **empty** (this means root of the repo)
9. Click **Move files**
10. Add a commit message: `Move files to repo root for GitHub Pages`
11. Click **Commit changes**

---

## Step 3: Delete the Empty Nested Folder

After moving the files, the `ritus-kitchen/` folder may still exist as an empty folder or with only hidden files.

1. Go back to the repo root: `https://github.com/danaerysai-crypto/ritus-kitchen`
2. If you see an empty `ritus-kitchen/` folder:
   - Open it
   - If it has any files left, select and delete them
   - Or use the **Delete directory** option
3. Commit the deletion with message: `Remove empty nested folder`

---

## Step 4: Verify the Root Structure

After moving, your repo root should look like this:

```
ritus-kitchen/
├── index.html
├── menu-v2.html
├── order.html
├── order-history.html
├── admin.html
├── images/
├── tracking/
├── marketing-plan-auroville.md
├── data-driven-marketing-system.md
├── automation-blueprint.md
└── .gitignore (if any)
```

**Critical:** `index.html` must be visible **immediately** when you open the repo. Not inside any folder.

---

## Step 5: Check GitHub Pages Settings

1. On GitHub, go to **Settings** tab (top of repo)
2. In the left sidebar, click **Pages**
3. Under **Source**, select:
   - **Deploy from a branch**
   - **Branch:** `main`
   - **Folder:** `/(root)`
4. Click **Save**
5. Wait for the green banner at the top showing the live URL

### What You Should See

```
Your site is live at https://ritus-kitchen.vercel.app/
```

---

## Step 6: Wait and Test

1. Wait **1–2 minutes** for GitHub Pages to rebuild
2. Open: `https://ritus-kitchen.vercel.app/`
3. If it still shows 404, wait another 2 minutes and hard-refresh:
   - Windows: `Ctrl + Shift + R`
   - Mac: `Cmd + Shift + R`
4. Test these URLs:
   - `https://ritus-kitchen.vercel.app/`
   - `https://ritus-kitchen.vercel.app/order.html`
   - `https://ritus-kitchen.vercel.app/order-history.html`

---

## Common Mistakes to Avoid

| Mistake | Why It Fails |
|---------|--------------|
| Moving files but leaving empty `ritus-kitchen/` folder | Folder still blocks root resolution |
| Selecting `/(root)` but branch is not `main` | Pages builds from wrong branch |
| Forgetting to click **Commit changes** | Move is not saved |
| Moving only `index.html` but not `images/` | Images break on live site |
| Pages folder set to `/docs` | GitHub looks for `docs/` folder |

---

## If GitHub Web Move Is Confusing, Use Git Command Line

If you prefer commands:

```bash
# Clone the repo (one-time)
git clone https://github.com/danaerysai-crypto/ritus-kitchen.git
cd ritus-kitchen

# Move all files from nested folder to root
mv ritus-kitchen/* .
mv ritus-kitchen/images/* images/ 2>/dev/null || true
mv ritus-kitchen/tracking/* tracking/ 2>/dev/null || true

# Remove empty nested folder
rmdir ritus-kitchen

# Add, commit, push
git add .
git commit -m "Move all files to repo root for GitHub Pages"
git push origin main
```

---

## After the Fix

Once Pages is live, update all your links:

| Where | Link to Add |
|-------|-------------|
| Instagram bio | `https://ritus-kitchen.vercel.app/order.html` |
| WhatsApp status | Same order link |
| Flyers / QR codes | Same order link |
| Google Business | Website field |
| WhatsApp Business quick reply `/order` | Same link |

---

## Expected Live URLs After Fix

| Page | URL |
|------|-----|
| Home | `https://ritus-kitchen.vercel.app/` |
| Order | `https://ritus-kitchen.vercel.app/order.html` |
| Order History | `https://ritus-kitchen.vercel.app/order-history.html` |
| Admin | `https://ritus-kitchen.vercel.app/admin.html` |
| Menu | `https://ritus-kitchen.vercel.app/menu-v2.html` |

---

## One-Sentence Summary

**Move every file out of the inner `ritus-kitchen/` folder so `index.html` sits at the top level of the GitHub repo, then set Pages source to `main` branch `/(root)`.**

---

## Need Help?

If the move fails or the folder won't delete:
1. Take a screenshot of your repo root on GitHub
2. Share it and I can give exact next steps
3. Or use the command-line method above — it is more reliable for nested folders