# Setup New Background Images - Complete Guide

This guide will help you replace the SVG backgrounds with high-quality PNG/JPG images from free stock photo websites.

## 🚀 Quick Start (Automated)

### Option 1: Automatic Download (Recommended)

```bash
# Step 1: Run the download script
python download_backgrounds.py

# Step 2: Update CSS to use new images
python update_css_backgrounds.py

# Step 3: Restart your Django server
python manage.py runserver
```

That's it! The backgrounds will be automatically downloaded and configured.

---

## 📋 Manual Setup (If Automatic Fails)

### Step 1: Create Backgrounds Folder

```bash
mkdir -p static/img/backgrounds
```

### Step 2: Download Images Manually

Visit these websites and download high-quality images:

#### 🌐 Recommended Sources:
- **Unsplash**: https://unsplash.com (Best quality, free)
- **Pexels**: https://pexels.com (Great variety)
- **Pixabay**: https://pixabay.com (Public domain)

#### 📸 Images to Download:

| Filename | Search Term | Recommended URL |
|----------|-------------|-----------------|
| `bg-landing.jpg` | "medical technology modern" | https://unsplash.com/s/photos/medical-technology |
| `bg-dashboard.jpg` | "medical data analytics" | https://unsplash.com/s/photos/medical-data |
| `bg-emergency.jpg` | "emergency room hospital" | https://unsplash.com/s/photos/emergency-room |
| `bg-donor.jpg` | "blood donation caring" | https://unsplash.com/s/photos/blood-donation |
| `bg-medical.jpg` | "hospital modern clean" | https://unsplash.com/s/photos/hospital-modern |
| `bg-profile.jpg` | "healthcare professional" | https://unsplash.com/s/photos/healthcare-worker |
| `bg-awareness.jpg` | "medical education" | https://unsplash.com/s/photos/medical-education |
| `bg-camps.jpg` | "community health event" | https://unsplash.com/s/photos/health-fair |
| `bg-about.jpg` | "hospital building" | https://unsplash.com/s/photos/hospital-building |
| `bg-services.jpg` | "medical services" | https://unsplash.com/s/photos/medical-services |
| `bg-inventory.jpg` | "medical supplies" | https://unsplash.com/s/photos/medical-supplies |
| `bg-login.jpg` | "medical security" | https://unsplash.com/s/photos/medical-technology |

### Step 3: Download Instructions

For each image:

1. **Click on the image** you like
2. **Click "Download"** button (usually top right)
3. **Select size**: Choose "Large" or "Original" (1920x1080 or bigger)
4. **Save to**: `static/img/backgrounds/` folder
5. **Rename**: Use the filename from the table above

### Step 4: Optimize Images (Optional but Recommended)

Use online tools to compress images:
- **TinyPNG**: https://tinypng.com
- **Squoosh**: https://squoosh.app

Target: Keep each image under 500KB

### Step 5: Update CSS

Run the update script:
```bash
python update_css_backgrounds.py
```

Or manually edit `static/css/styles.css` and replace:
```css
/* OLD */
url('../img/bg-landing-hero.svg')

/* NEW */
url('../img/backgrounds/bg-landing.jpg')
```

---

## 🎨 Image Selection Tips

### What to Look For:

✅ **Good Images:**
- Soft focus or slightly blurred
- Light, airy feel
- Professional medical setting
- Complementary colors (blues, whites, soft reds)
- High resolution (1920x1080+)
- Not too busy or distracting

❌ **Avoid:**
- Too dark or high contrast
- Busy, cluttered scenes
- Low resolution
- Watermarked images
- Overly saturated colors

### Color Preferences by Page:

| Page Type | Preferred Colors | Mood |
|-----------|------------------|------|
| Landing | Blue, White, Clean | Welcoming, Modern |
| Dashboard | Blue, Gray, Tech | Professional, Data-focused |
| Emergency | Red, White, Urgent | Dynamic, Attention-grabbing |
| Donor | Red, Warm tones | Caring, Community |
| Medical | Blue, White, Clean | Clinical, Trustworthy |
| Profile | Purple, Blue, Soft | Personal, Friendly |
| Awareness | Yellow, Bright | Educational, Positive |
| Camps | Green, Blue, Outdoor | Community, Active |

---

## 🔧 Troubleshooting

### Images Not Showing?

1. **Check file paths:**
   ```bash
   ls static/img/backgrounds/
   ```
   Should show all .jpg files

2. **Clear browser cache:**
   - Chrome/Edge: `Ctrl + Shift + R`
   - Firefox: `Ctrl + F5`

3. **Check CSS:**
   ```bash
   grep "backgrounds/" static/css/styles.css
   ```
   Should show references to new images

4. **Restart Django server:**
   ```bash
   python manage.py runserver
   ```

### Images Too Large?

Compress them using:
```bash
# If you have ImageMagick installed
mogrify -resize 1920x1080 -quality 80 static/img/backgrounds/*.jpg
```

Or use online tools:
- https://tinypng.com
- https://squoosh.app

### Wrong Colors/Mood?

1. Download different images from Unsplash/Pexels
2. Replace the files in `static/img/backgrounds/`
3. Keep the same filenames
4. Refresh browser

---

## 📊 File Structure

After setup, your structure should look like:

```
static/
├── img/
│   ├── backgrounds/          ← NEW FOLDER
│   │   ├── bg-landing.jpg
│   │   ├── bg-dashboard.jpg
│   │   ├── bg-emergency.jpg
│   │   ├── bg-donor.jpg
│   │   ├── bg-medical.jpg
│   │   ├── bg-profile.jpg
│   │   ├── bg-awareness.jpg
│   │   ├── bg-camps.jpg
│   │   ├── bg-about.jpg
│   │   ├── bg-services.jpg
│   │   ├── bg-inventory.jpg
│   │   └── bg-login.jpg
│   ├── bg-*.svg             ← OLD FILES (can delete)
│   └── ...
└── css/
    ├── styles.css           ← UPDATED
    └── styles.css.backup    ← BACKUP
```

---

## ✅ Verification Checklist

After setup, verify:

- [ ] All 12 images downloaded to `static/img/backgrounds/`
- [ ] Each image is 1920x1080 or larger
- [ ] File sizes are reasonable (< 500KB each)
- [ ] CSS updated with new paths
- [ ] Browser cache cleared
- [ ] Django server restarted
- [ ] Landing page shows new background
- [ ] Dashboard shows new background
- [ ] Emergency page shows new background
- [ ] All other pages tested

---

## 🎯 Specific Image Recommendations

### Landing Page (bg-landing.jpg)
**Perfect Image Examples:**
- Modern hospital lobby with natural light
- Abstract medical technology visualization
- Clean, bright medical facility
- Soft-focus healthcare environment

**Unsplash Search:** `medical technology modern clean`

### Emergency Page (bg-emergency.jpg)
**Perfect Image Examples:**
- Emergency room entrance (not too graphic)
- Ambulance with soft focus
- Red emergency signage
- Urgent care facility

**Unsplash Search:** `emergency medical hospital red`

### Blood Donation (bg-donor.jpg)
**Perfect Image Examples:**
- Blood donation bag close-up
- Donor giving blood (caring moment)
- Blood bank facility
- Medical professional with blood bag

**Unsplash Search:** `blood donation caring hands`

---

## 🚀 Performance Tips

### Optimize for Web:

1. **Resize to exact dimensions:**
   - Width: 1920px
   - Height: 1080px

2. **Compress:**
   - JPG Quality: 70-80%
   - Target size: 200-500KB

3. **Use WebP (Advanced):**
   ```bash
   # Convert JPG to WebP
   cwebp -q 80 bg-landing.jpg -o bg-landing.webp
   ```

4. **Lazy Loading:**
   - Backgrounds load automatically
   - No additional code needed

---

## 📞 Need Help?

### Common Issues:

**Q: Images are too dark, text is hard to read**
A: The CSS includes automatic overlays. Adjust in `styles.css`:
```css
body::before {
  background-color: rgba(255, 255, 255, 0.90) !important;
}
```

**Q: Images don't match the theme**
A: Download different images from Unsplash using the search terms provided

**Q: File sizes are too large**
A: Use TinyPNG.com to compress images

**Q: Some pages still show old backgrounds**
A: Clear browser cache (Ctrl+Shift+R) and restart Django server

---

## 🎨 Alternative: Use Provided URLs

If you want to use specific high-quality images, here are direct Unsplash URLs:

```python
# Add these to download_backgrounds.py
DIRECT_URLS = {
    "bg-landing.jpg": "https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=1920&q=80",
    "bg-dashboard.jpg": "https://images.unsplash.com/photo-1576091160550-2173dba999ef?w=1920&q=80",
    "bg-emergency.jpg": "https://images.unsplash.com/photo-1587351021759-3e566b6af7cc?w=1920&q=80",
    "bg-donor.jpg": "https://images.unsplash.com/photo-1615461066841-6116e61058f4?w=1920&q=80",
    # ... etc
}
```

---

## ✨ Final Result

After completing this setup:
- ✅ Professional, high-quality backgrounds on all pages
- ✅ Faster loading than SVG (optimized JPG)
- ✅ Better visual appeal
- ✅ Consistent medical/healthcare theme
- ✅ Improved user experience

---

**Last Updated:** 2026
**Version:** 1.0
