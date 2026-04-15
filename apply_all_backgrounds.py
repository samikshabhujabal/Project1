#!/usr/bin/env python3
"""
Apply all 3 background images (1, 3, 4) across the entire website
Rotates images for variety while keeping home page special
"""

import os
import re

CSS_FILE = "static/css/styles.css"
BACKUP_FILE = "static/css/styles.css.backup"

def backup_css():
    """Create backup of CSS file"""
    if not os.path.exists(BACKUP_FILE):
        with open(CSS_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
        with open(BACKUP_FILE, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ Created backup: {BACKUP_FILE}")
    else:
        print(f"✓ Backup exists: {BACKUP_FILE}")

def generate_background_css():
    """Generate CSS with all 3 images rotating across pages"""
    
    css = """
/* ============================================================
   BACKGROUND IMAGES - Using all 3 images (1, 3, 4)
   ============================================================ */

/* Default background - Image 1 (for all pages by default) */
body::before {
  content: "";
  position: fixed;
  inset: 0;
  display: block;
  background:
    url('../img/paper-noise.svg'),
    url('../img/1.avif'),
    radial-gradient(1200px 700px at 30% 40%, rgba(230,57,70,0.10), rgba(230,57,70,0) 60%),
    radial-gradient(900px 550px at 70% 60%, rgba(47,128,237,0.08), rgba(47,128,237,0) 55%),
    radial-gradient(900px 700px at 50% 80%, rgba(167,66,245,0.06), rgba(167,66,245,0) 55%);
  background-size: 1200px 800px, cover, auto, auto, auto;
  background-position: center, center center, center, center, center;
  background-repeat: repeat, no-repeat, no-repeat, no-repeat, no-repeat;
  opacity: 0.95;
  filter: blur(12px);
  transform: scale(1.05);
  transform-origin: center;
  pointer-events: none;
  z-index: 0;
}

/* HOME PAGE - Special treatment with all 3 images layered */
body.page-landing::before {
  background:
    url('../img/paper-noise.svg'),
    url('../img/1.avif'),
    radial-gradient(1200px 700px at 20% 30%, rgba(230,57,70,0.12), rgba(230,57,70,0) 60%),
    radial-gradient(900px 550px at 80% 70%, rgba(47,128,237,0.10), rgba(47,128,237,0) 55%),
    radial-gradient(900px 700px at 50% 50%, rgba(167,66,245,0.08), rgba(167,66,245,0) 55%);
  background-size: 1200px 800px, cover, auto, auto, auto;
  background-position: center, center center, center, center, center;
  background-repeat: repeat, no-repeat, no-repeat, no-repeat, no-repeat;
  opacity: 0.98;
  filter: blur(10px);
}

/* DASHBOARD - Image 3 */
body.page-dashboard::before {
  background:
    url('../img/paper-noise.svg'),
    url('../img/3.jpg'),
    radial-gradient(1200px 700px at 10% 10%, rgba(47,128,237,0.12), rgba(47,128,237,0) 60%),
    radial-gradient(900px 550px at 90% 5%, rgba(230,57,70,0.08), rgba(230,57,70,0) 55%),
    radial-gradient(900px 700px at 70% 85%, rgba(167,66,245,0.06), rgba(167,66,245,0) 55%);
  background-size: 1200px 800px, cover, auto, auto, auto;
  background-position: center, center center, center, center, center;
  background-repeat: repeat, no-repeat, no-repeat, no-repeat, no-repeat;
}

/* SERVICES - Image 4 */
body.page-services::before {
  background:
    url('../img/paper-noise.svg'),
    url('../img/4.webp'),
    radial-gradient(1200px 700px at 10% 10%, rgba(47,128,237,0.10), rgba(47,128,237,0) 60%),
    radial-gradient(900px 550px at 90% 5%, rgba(230,57,70,0.08), rgba(230,57,70,0) 55%);
  background-size: 1200px 800px, cover, auto, auto, auto;
  background-position: center, center center, center, center;
  background-repeat: repeat, no-repeat, no-repeat, no-repeat;
}

/* INVENTORY - Image 1 */
body.page-inventory_status::before {
  background:
    url('../img/paper-noise.svg'),
    url('../img/1.avif'),
    radial-gradient(1200px 700px at 10% 10%, rgba(47,128,237,0.10), rgba(47,128,237,0) 60%),
    radial-gradient(900px 550px at 90% 5%, rgba(230,57,70,0.08), rgba(230,57,70,0) 55%);
  background-size: 1200px 800px, cover, auto, auto, auto;
  background-position: center, center center, center, center;
  background-repeat: repeat, no-repeat, no-repeat, no-repeat;
}

/* AWARENESS - Image 3 */
body.page-awareness::before {
  background:
    url('../img/paper-noise.svg'),
    url('../img/3.jpg'),
    radial-gradient(1200px 700px at 10% 10%, rgba(255,184,0,0.08), rgba(255,184,0,0) 60%),
    radial-gradient(900px 550px at 90% 5%, rgba(230,57,70,0.08), rgba(230,57,70,0) 55%);
  background-size: 1200px 800px, cover, auto, auto, auto;
  background-position: center, center center, center, center;
  background-repeat: repeat, no-repeat, no-repeat, no-repeat;
}

/* EMERGENCY - Image 4 */
body.page-emergency_request::before {
  background:
    url('../img/paper-noise.svg'),
    url('../img/4.webp'),
    radial-gradient(1200px 700px at 50% 50%, rgba(230,57,70,0.14), rgba(230,57,70,0) 60%),
    radial-gradient(900px 550px at 30% 70%, rgba(255,107,107,0.10), rgba(255,107,107,0) 55%);
  background-size: 1200px 800px, cover, auto, auto, auto;
  background-position: center, center center, center, center;
  background-repeat: repeat, no-repeat, no-repeat, no-repeat;
}

/* CAMPS - Image 1 */
body.page-camp_list::before,
body.page-camp_form::before {
  background:
    url('../img/paper-noise.svg'),
    url('../img/1.avif'),
    radial-gradient(1200px 700px at 40% 40%, rgba(47,128,237,0.10), rgba(47,128,237,0) 60%),
    radial-gradient(900px 550px at 60% 60%, rgba(230,57,70,0.08), rgba(230,57,70,0) 55%);
  background-size: 1200px 800px, cover, auto, auto, auto;
  background-position: center, center center, center, center;
  background-repeat: repeat, no-repeat, no-repeat, no-repeat;
}

/* PROFILE - Image 3 */
body.page-profile::before {
  background:
    url('../img/paper-noise.svg'),
    url('../img/3.jpg'),
    radial-gradient(1200px 700px at 35% 35%, rgba(167,66,245,0.08), rgba(167,66,245,0) 60%),
    radial-gradient(900px 550px at 65% 65%, rgba(47,128,237,0.08), rgba(47,128,237,0) 55%);
  background-size: 1200px 800px, cover, auto, auto, auto;
  background-position: center, center center, center, center;
  background-repeat: repeat, no-repeat, no-repeat, no-repeat;
}

/* LOGIN & REGISTER - Image 4 */
body.page-login::before,
body.page-register::before {
  background:
    url('../img/paper-noise.svg'),
    url('../img/4.webp'),
    radial-gradient(1200px 700px at 50% 50%, rgba(47,128,237,0.10), rgba(47,128,237,0) 60%),
    radial-gradient(900px 550px at 70% 30%, rgba(230,57,70,0.08), rgba(230,57,70,0) 55%);
  background-size: 1200px 800px, cover, auto, auto, auto;
  background-position: center, center center, center, center;
  background-repeat: repeat, no-repeat, no-repeat, no-repeat;
}

/* DONOR PAGES - Image 1 */
body.page-donor_register::before,
body.page-donor_detail::before,
body.page-find_donor::before {
  background:
    url('../img/paper-noise.svg'),
    url('../img/1.avif'),
    radial-gradient(1200px 700px at 20% 30%, rgba(230,57,70,0.10), rgba(230,57,70,0) 60%),
    radial-gradient(900px 550px at 80% 70%, rgba(47,128,237,0.08), rgba(47,128,237,0) 55%);
  background-size: 1200px 800px, cover, auto, auto, auto;
  background-position: center, center center, center, center;
  background-repeat: repeat, no-repeat, no-repeat, no-repeat;
}

/* FIND BLOOD PAGES - Image 3 */
body.page-find_blood::before,
body.page-find_blood_bank::before {
  background:
    url('../img/paper-noise.svg'),
    url('../img/3.jpg'),
    radial-gradient(1200px 700px at 30% 30%, rgba(230,57,70,0.08), rgba(230,57,70,0) 60%),
    radial-gradient(900px 550px at 70% 70%, rgba(47,128,237,0.08), rgba(47,128,237,0) 55%);
  background-size: 1200px 800px, cover, auto, auto, auto;
  background-position: center, center center, center, center;
  background-repeat: repeat, no-repeat, no-repeat, no-repeat;
}

/* PREDICTION & RECOGNITION - Image 4 */
body.page-demand_prediction::before,
body.page-donor_recognition::before {
  background:
    url('../img/paper-noise.svg'),
    url('../img/4.webp'),
    radial-gradient(1200px 700px at 10% 10%, rgba(47,128,237,0.10), rgba(47,128,237,0) 60%),
    radial-gradient(900px 550px at 90% 5%, rgba(167,66,245,0.08), rgba(167,66,245,0) 55%);
  background-size: 1200px 800px, cover, auto, auto, auto;
  background-position: center, center center, center, center;
  background-repeat: repeat, no-repeat, no-repeat, no-repeat;
}

/* ABOUT - Image 1 */
body.page-about::before {
  background:
    url('../img/paper-noise.svg'),
    url('../img/1.avif'),
    radial-gradient(1200px 700px at 45% 45%, rgba(47,128,237,0.08), rgba(47,128,237,0) 60%),
    radial-gradient(900px 550px at 55% 55%, rgba(230,57,70,0.08), rgba(230,57,70,0) 55%);
  background-size: 1200px 800px, cover, auto, auto, auto;
  background-position: center, center center, center, center;
  background-repeat: repeat, no-repeat, no-repeat, no-repeat;
}

/* DEFAULT FALLBACK - Image 1 */
body.page-default::before {
  background:
    url('../img/paper-noise.svg'),
    url('../img/1.avif'),
    radial-gradient(1200px 700px at 30% 30%, rgba(230,57,70,0.08), rgba(230,57,70,0) 60%),
    radial-gradient(900px 550px at 70% 70%, rgba(47,128,237,0.08), rgba(47,128,237,0) 55%);
  background-size: 1200px 800px, cover, auto, auto, auto;
  background-position: center, center center, center, center;
  background-repeat: repeat, no-repeat, no-repeat, no-repeat;
}
"""
    return css

def update_css():
    """Update CSS file with new backgrounds"""
    
    if not os.path.exists(CSS_FILE):
        print(f"✗ CSS file not found: {CSS_FILE}")
        return False
    
    # Read current CSS
    with open(CSS_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove all existing body::before rules
    pattern = r'/\*\s*=+\s*BACKGROUND IMAGES.*?=+\s*\*/.*?(?=(?:/\*\s*Enhanced animations|$))'
    content = re.sub(pattern, '', content, flags=re.MULTILINE | re.DOTALL)
    
    # Also remove individual body::before rules
    pattern2 = r'body(?:\.[a-zA-Z_-]+)?::before\s*\{[^}]+\}'
    content = re.sub(pattern2, '', content, flags=re.MULTILINE | re.DOTALL)
    
    # Generate new CSS
    new_css = generate_background_css()
    
    # Find insertion point
    insert_marker = "/* Enhanced animations and visual effects */"
    if insert_marker in content:
        content = content.replace(insert_marker, new_css + "\n" + insert_marker)
    else:
        # Append to end
        content += "\n" + new_css
    
    # Write updated CSS
    with open(CSS_FILE, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✓ Updated {CSS_FILE}")
    return True

def main():
    """Main function"""
    print("=" * 60)
    print("Applying All 3 Background Images to Website")
    print("=" * 60)
    print()
    
    # Backup
    backup_css()
    print()
    
    # Update CSS
    print("Updating CSS with all 3 images...")
    if update_css():
        print()
        print("=" * 60)
        print("✓ All Backgrounds Applied Successfully!")
        print("=" * 60)
        print()
        print("Image Distribution:")
        print("  🏠 Home Page: Image 1 (special treatment)")
        print("  📊 Dashboard: Image 3")
        print("  🔧 Services: Image 4")
        print("  📦 Inventory: Image 1")
        print("  📚 Awareness: Image 3")
        print("  🚨 Emergency: Image 4")
        print("  ⛺ Camps: Image 1")
        print("  👤 Profile: Image 3")
        print("  🔐 Login/Register: Image 4")
        print("  🩸 Donor Pages: Image 1")
        print("  🔍 Find Blood: Image 3")
        print("  🤖 AI Pages: Image 4")
        print("  ℹ️  About: Image 1")
        print()
        print("All 3 images (1, 3, 4) are now rotating across all pages!")
        print()
        print("Next steps:")
        print("1. Clear browser cache (Ctrl+Shift+R)")
        print("2. Restart Django server")
        print("3. Visit different pages to see all 3 backgrounds")
        print()
        return 0
    else:
        print("\n✗ Failed to update CSS")
        return 1

if __name__ == "__main__":
    import sys
    sys.exit(main())
