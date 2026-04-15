#!/usr/bin/env python3
"""
Make background images clearly visible by removing white overlay
and reducing blur effects
"""

import os
import re

CSS_FILE = "static/css/styles.css"
BACKUP_FILE = "static/css/styles.css.backup"

def backup_css():
    """Create backup"""
    if not os.path.exists(BACKUP_FILE):
        with open(CSS_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
        with open(BACKUP_FILE, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ Created backup: {BACKUP_FILE}")
    else:
        print(f"✓ Backup exists: {BACKUP_FILE}")

def generate_visible_backgrounds():
    """Generate CSS with clearly visible backgrounds"""
    
    css = """
/* ============================================================
   BACKGROUND IMAGES - CLEARLY VISIBLE (No white overlay)
   ============================================================ */

/* Remove white background from HTML */
html {
  background-color: transparent;
  background-image: none;
}

/* Default background - Image 1 (VISIBLE) */
body::before {
  content: "";
  position: fixed;
  inset: 0;
  display: block;
  background:
    url('../img/1.avif');
  background-size: cover;
  background-position: center center;
  background-repeat: no-repeat;
  background-attachment: fixed;
  opacity: 1;
  filter: blur(0px);
  transform: scale(1);
  transform-origin: center;
  pointer-events: none;
  z-index: -1;
}

/* Add subtle dark overlay for text readability */
body::after {
  content: "";
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.3);
  z-index: -1;
  pointer-events: none;
}

/* HOME PAGE - Image 1 */
body.page-landing::before {
  background: url('../img/1.avif');
  background-size: cover;
  background-position: center center;
  background-repeat: no-repeat;
  background-attachment: fixed;
}

/* DASHBOARD - Image 3 */
body.page-dashboard::before {
  background: url('../img/3.jpg');
  background-size: cover;
  background-position: center center;
  background-repeat: no-repeat;
  background-attachment: fixed;
}

/* SERVICES - Image 4 */
body.page-services::before {
  background: url('../img/4.webp');
  background-size: cover;
  background-position: center center;
  background-repeat: no-repeat;
  background-attachment: fixed;
}

/* INVENTORY - Image 1 */
body.page-inventory_status::before {
  background: url('../img/1.avif');
  background-size: cover;
  background-position: center center;
  background-repeat: no-repeat;
  background-attachment: fixed;
}

/* AWARENESS - Image 3 */
body.page-awareness::before {
  background: url('../img/3.jpg');
  background-size: cover;
  background-position: center center;
  background-repeat: no-repeat;
  background-attachment: fixed;
}

/* EMERGENCY - Image 4 */
body.page-emergency_request::before {
  background: url('../img/4.webp');
  background-size: cover;
  background-position: center center;
  background-repeat: no-repeat;
  background-attachment: fixed;
}

/* CAMPS - Image 1 */
body.page-camp_list::before,
body.page-camp_form::before {
  background: url('../img/1.avif');
  background-size: cover;
  background-position: center center;
  background-repeat: no-repeat;
  background-attachment: fixed;
}

/* PROFILE - Image 3 */
body.page-profile::before {
  background: url('../img/3.jpg');
  background-size: cover;
  background-position: center center;
  background-repeat: no-repeat;
  background-attachment: fixed;
}

/* LOGIN & REGISTER - Image 4 */
body.page-login::before,
body.page-register::before {
  background: url('../img/4.webp');
  background-size: cover;
  background-position: center center;
  background-repeat: no-repeat;
  background-attachment: fixed;
}

/* DONOR PAGES - Image 1 */
body.page-donor_register::before,
body.page-donor_detail::before,
body.page-find_donor::before {
  background: url('../img/1.avif');
  background-size: cover;
  background-position: center center;
  background-repeat: no-repeat;
  background-attachment: fixed;
}

/* FIND BLOOD PAGES - Image 3 */
body.page-find_blood::before,
body.page-find_blood_bank::before {
  background: url('../img/3.jpg');
  background-size: cover;
  background-position: center center;
  background-repeat: no-repeat;
  background-attachment: fixed;
}

/* PREDICTION & RECOGNITION - Image 4 */
body.page-demand_prediction::before,
body.page-donor_recognition::before {
  background: url('../img/4.webp');
  background-size: cover;
  background-position: center center;
  background-repeat: no-repeat;
  background-attachment: fixed;
}

/* ABOUT - Image 1 */
body.page-about::before {
  background: url('../img/1.avif');
  background-size: cover;
  background-position: center center;
  background-repeat: no-repeat;
  background-attachment: fixed;
}

/* DEFAULT FALLBACK - Image 1 */
body.page-default::before {
  background: url('../img/1.avif');
  background-size: cover;
  background-position: center center;
  background-repeat: no-repeat;
  background-attachment: fixed;
}

/* Make cards more transparent to show background */
.bb-glass,
.card {
  background: rgba(255, 255, 255, 0.85) !important;
  backdrop-filter: blur(10px) !important;
}

/* Make navbar more transparent */
.bb-nav {
  background: rgba(255, 255, 255, 0.90) !important;
  backdrop-filter: blur(15px) !important;
}

/* Make footer more transparent */
footer.footer {
  background: rgba(255, 255, 255, 0.85) !important;
  backdrop-filter: blur(12px) !important;
}
"""
    return css

def update_css():
    """Update CSS to make backgrounds visible"""
    
    if not os.path.exists(CSS_FILE):
        print(f"✗ CSS file not found: {CSS_FILE}")
        return False
    
    # Read current CSS
    with open(CSS_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove old background rules
    pattern = r'/\*\s*=+\s*BACKGROUND IMAGES.*?(?=(?:/\*\s*Enhanced animations|$))'
    content = re.sub(pattern, '', content, flags=re.MULTILINE | re.DOTALL)
    
    # Remove individual body::before and body::after rules
    pattern2 = r'body(?:\.[a-zA-Z_-]+)?::(?:before|after)\s*\{[^}]+\}'
    content = re.sub(pattern2, '', content, flags=re.MULTILINE | re.DOTALL)
    
    # Remove html background
    pattern3 = r'html\s*\{[^}]*background[^}]*\}'
    content = re.sub(pattern3, '', content, flags=re.MULTILINE | re.DOTALL)
    
    # Generate new CSS
    new_css = generate_visible_backgrounds()
    
    # Find insertion point
    insert_marker = "/* Enhanced animations and visual effects */"
    if insert_marker in content:
        content = content.replace(insert_marker, new_css + "\n" + insert_marker)
    else:
        content += "\n" + new_css
    
    # Write updated CSS
    with open(CSS_FILE, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✓ Updated {CSS_FILE}")
    return True

def main():
    """Main function"""
    print("=" * 60)
    print("Making Background Images Clearly Visible")
    print("=" * 60)
    print()
    
    # Backup
    backup_css()
    print()
    
    # Update CSS
    print("Removing white overlay and blur effects...")
    if update_css():
        print()
        print("=" * 60)
        print("✓ Images Now Clearly Visible!")
        print("=" * 60)
        print()
        print("Changes made:")
        print("  ✓ Removed white background overlay")
        print("  ✓ Removed blur effect (0px)")
        print("  ✓ Set opacity to 100%")
        print("  ✓ Added dark overlay for text readability")
        print("  ✓ Made cards more transparent")
        print()
        print("Image Distribution:")
        print("  Image 1: Home, Inventory, Camps, Donor pages, About")
        print("  Image 3: Dashboard, Awareness, Profile, Find Blood")
        print("  Image 4: Services, Emergency, Login, AI pages")
        print()
        print("Next steps:")
        print("1. Clear browser cache (Ctrl+Shift+R)")
        print("2. Restart Django server")
        print("3. Your images will be CLEARLY VISIBLE!")
        print()
        return 0
    else:
        print("\n✗ Failed to update CSS")
        return 1

if __name__ == "__main__":
    import sys
    sys.exit(main())
