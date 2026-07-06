# Deploy Ritu's Kitchen to GitHub Pages
## One-Time Fix: Move Files to Repo Root

---

## Quick Command Method (Recommended)

Run these commands in your terminal. They will move all files from the nested `ritus-kitchen/` folder to the repo root, delete the empty folder, and push to GitHub.

```bash
# 1. Go to the project folder
cd /c/Users/Admin/Desktop/projects/ritus-kitchen

# 2. Make sure git is connected
git remote -v
# You should see: https://github.com/danaerysai-crypto/ritus-kitchen.git

# 3. Move all nested files to root
mv ritus-kitchen/* .
mv ritus-kitchen/images/* images/ 2>/dev/null || true
mv ritus-kitchen/tracking/* tracking/ 2>/dev/null || true

# 4. Remove the now-empty nested folder
rmdir ritus-kitchen

# 5. Stage all changes
git add .

# 6. Commit
git commit -m "Move all website files to repo root for GitHub Pages"

# 7. Push to main
git push origin main

# 8. Wait 1-2 minutes, then test
echo "Live URL: https://ritus-kitchen.vercel.app/"
```

---

## What This Does

### Before (Broken — 404)

```
ritus-kitchen/          ← GitHub repo
└── ritus-kitchen/        ← wrong nested folder
    ├── index.html
    ├── menu-v2.html
    ├── order.html
    ├── images/
    └── tracking/
```

### After (Fixed — Live)

```
ritus-kitchen/          ← GitHub repo
├── index.html          ← at root
├── menu-v2.html
├── order.html
├── order-history.html
├── admin.html
├── images/
├── tracking/
└── *.md files
```

---

## GitHub Pages Settings

After pushing, go to:

`https://github.com/danaerysai-crypto/ritus-kitchen/settings/pages`

Make sure:
- **Source:** Deploy from a branch
- **Branch:** main
- **Folder:** /(root)

Then wait for the green banner with the live URL.

---

## Troubleshooting

| Error | Fix |
|-------|-----|
| `mv: cannot stat 'ritus-kitchen/*': No such file or directory` | The folder may have a different name or already be at root |
| `git push` fails | Run `git pull origin main` first, then push |
| Pages still 404 after 5 min | Check that `index.html` is truly at repo root, not inside any folder |
| Images not showing | Make sure `images/` folder moved to root too |

---

## Alternative: Web Interface Method

If you prefer not to use commands:

1. Go to `https://github.com/danaerysai-crypto/ritus-kitchen`
2. Click the `ritus-kitchen/` folder
3. Select all files
4. Click the three dots → **Move**
5. Delete the folder path so destination is root
6. Commit
7. Delete the now-empty `ritus-kitchen/` folder
8. Enable Pages in Settings

The command method is faster and more reliable.

---

## After Deployment

Test these URLs in your browser:

- `https://ritus-kitchen.vercel.app/`
- `https://ritus-kitchen.vercel.app/order.html`
- `https://ritus-kitchen.vercel.app/order-history.html`
- `https://ritus-kitchen.vercel.app/menu-v2.html`
- `https://ritus-kitchen.vercel.app/admin.html`

All should load without 404.