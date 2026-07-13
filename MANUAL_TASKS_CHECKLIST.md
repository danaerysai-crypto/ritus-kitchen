# Ritu's Kitchen — Manual Tasks Checklist

This is the single source of truth for tasks only you can complete. Do them in order. Tick each box before moving to the next.

---

## Phase 1: Security (Do this first — 10 minutes)

- [ ] 1. Delete GitHub token messages from this Telegram chat
  - Long-press each message containing `ghp_...`
  - Tap **Delete** → **Delete for everyone**
- [ ] 2. Revoke old GitHub token
  - Go to https://github.com/settings/tokens
  - Find the token used today → click **Delete**
- [ ] 3. Generate a new GitHub token (only when needed for next push)
  - https://github.com/settings/tokens/new
  - Scopes: `repo`
  - Save it somewhere secure (password manager, not chat)

---

## Phase 2: Google Account Setup (Do in one sitting — 30 minutes)

Use account: **rituskitchen.av@gmail.com**

- [ ] 4. Set up Google Analytics 4
  - Go to https://analytics.google.com
  - Create property: **Ritu's Kitchen Website**
  - Add web stream: `https://ritus-kitchen.vercel.app`
  - Copy Measurement ID (starts with `G-`)
  - Send the ID to me → I will update all HTML files
- [ ] 5. Create the live Google Form for orders
  - Use the guide: `google-form-setup-guide.md`
  - Link responses to a Google Sheet
  - Copy the form action URL and 9 entry IDs
  - Send them to me → I will wire them into `order.html`
- [ ] 6. Set up Google Business Profile
  - Go to https://business.google.com
  - Search for / create **Ritu's Kitchen**
  - Address: Auroville, Tamil Nadu, India
  - Phone: +91 90431 40686
  - Email: rituskitchen.av@gmail.com
  - Website: https://ritus-kitchen.vercel.app
  - Category: Restaurant / Home-cooked food / Meal delivery
  - Description: use text from `whatsapp-instagram-bios.md`
  - Upload logo: `images/logo-ritus-kitchen-regenerated.png`
  - Upload menu card: `ritus-kitchen-menu-google.png`
  - Verify by postcard / phone / video (Google decides)
  - Send me the GBP public link → I will add it to the website and WhatsApp templates

---

## Phase 3: WhatsApp Business (Do on your phone — 20 minutes)

- [ ] 7. Install / open WhatsApp Business app on +91 90431 40686
- [ ] 8. Set business profile
  - Business name: Ritu's Kitchen
  - Category: Food & Drink / Home Cooked
  - About/bio: copy from `whatsapp-instagram-bios.md`
  - Profile photo: `images/logo-ritus-kitchen-regenerated.png`
  - Website: https://ritus-kitchen.vercel.app/order.html
- [ ] 9. Add greeting message
  - Use `/greet` text from `whatsapp-quick-replies.md`
- [ ] 10. Add away message (optional)
- [ ] 11. Add 12 quick replies
  - Settings → Business tools → Quick replies
  - Shortcuts: `/order`, `/menu`, `/tiffin`, `/price`, `/hours`, `/gf`, `/vegan`, `/location`, `/pay`, `/soldout`, `/waitlist`, `/thanks`, `/review`
  - Full text is in `whatsapp-quick-replies-print.txt` (printable)

---

## Phase 4: Instagram (Do on your phone — 20 minutes)

- [ ] 12. Create Instagram account
  - Username options (check availability in app):
    1. `@rituskitchen.auroville`
    2. `@rituskitchen_av`
    3. `@ritu.kitchen.av`
    4. `@ritus_kitchen_av`
- [ ] 13. Set profile
  - Name: Ritu's Kitchen
  - Bio: copy from `whatsapp-instagram-bios.md`
  - Website: https://ritus-kitchen.vercel.app/order.html
  - Profile photo: `images/logo-ritus-kitchen-regenerated.png`
  - Contact: +91 90431 40686, rituskitchen.av@gmail.com
- [ ] 14. First post
  - Image: `ritus-kitchen-menu-instagram.png`
  - Caption: use launch caption from `whatsapp-instagram-bios.md`
  - Hashtags included
- [ ] 15. First Story
  - Image: `ritus-kitchen-menu-story.png`
  - Text: "Swipe up / DM to order · Fresh thalis · Auroville · Pre-book by 11 AM"
- [ ] 16. Create Story highlights: Menu, Order, GF/Vegan, Reviews, Auroville
- [ ] 17. Send me the Instagram profile URL → I will add it to the website

---

## Phase 5: Content & Media (Do as time allows)

- [ ] 18. Generate 7 AI videos for scrollytelling homepage
  - Use prompts from `Ritus-Kitchen-Scroll-Website-Brief.md`
  - Tools: Runway Gen-3, Kling AI, or Luma Dream Machine
  - Save as:
    - `ritu-video-01-dawn.mp4`
    - `ritu-video-02-ingredients.mp4`
    - `ritu-video-03-idli.mp4`
    - `ritu-video-04-thali-cooking.mp4`
    - `ritu-video-05-plating.mp4`
    - `ritu-video-06-delivery.mp4`
    - `ritu-video-07-first-bite.mp4`
  - Send files to me → I will build the scrolltelling homepage
- [ ] 19. Take real photos (optional but better than AI)
  - Ritu cooking in kitchen
  - Close-ups of thali items
  - Packed tiffin / delivery
  - Happy customer with food
  - Send best 5–10 images to me
- [ ] 20. Collect real testimonials
  - Ask 3–5 customers for a short WhatsApp review
  - Send names + exact quotes to me → I will update website

---

## Phase 6: Operations (Ongoing)

- [ ] 21. Decide daily menu and update it every morning
  - I can build a simple daily-menu update system if you want
- [ ] 22. Update order counter manually on website
  - Or give me a simple way to track slots (sheet/JSON) and I'll automate it
- [ ] 23. Check Google Form responses daily
  - Confirm orders on WhatsApp
  - Mark payments received
- [ ] 24. Request Google reviews from happy customers
  - Once GBP is verified, send review link to 5 customers

---

## Do not do these (already handled)

| Task | Status |
|------|--------|
| Website copy and design | ✅ Done |
| Logo regeneration | ✅ Done |
| Menu card PNGs | ✅ Done |
| GitHub/Vercel deployment | ✅ Done |
| UPI QR code on order page | ✅ Done |
| FAQ, privacy, 404, OG/schema | ✅ Done |
| WhatsApp/Instagram bio text | ✅ Done |
| Quick reply templates | ✅ Done |

---

## How to use this checklist

1. Open this file: `C:/Users/Admin/Desktop/projects/ritus-kitchen/MANUAL_TASKS_CHECKLIST.md`
2. Start at Phase 1 (security)
3. Do not skip phases
4. Send me IDs/URLs as soon as you get them — I will update the website immediately

---

*Last updated: July 7, 2026*
