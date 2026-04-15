#!/usr/bin/env python3
"""
Update CSS to use the 3 user-provided images as backgrounds
Distributes images across all pages
"""

import os
import re

CSS_FILE = "static/css/styles.css"
BACKUP_FILE = "static/css/styles.css.backup"

# Map pages to the 3 images (rotating them)
# Image 1 (1.avif) - Modern, clean pages
# Image 3 (3.jpg) - Medical, professional pages  
# Image 4 (4.webp) - Emergency, urgent pages

PAGE_BACKGROUNDS = {
    # Image 1 - Landing, Dashboard, Services, About
    "page-landing": "backgrounds/bg-landing.avif",
    "page-dashboard": "backgrounds/bg-dashboard.avif",
    "page-services": "backgrounds/bg-services.avif",
    "page-about": "backgrounds/bg-about.avif",
    
    # Image 3 - Medical, Donor, Profile, Find Blood
    "page-find_blood": "backgrounds/bg-medical.jpg",
    "page-find_blood_bank": "backgrounds/bg-find-blood.jpg",
    "page-find_donor": "backgrounds/bg-donor.jpg",
    "page-donor_register": "backgrounds/bg-donor.jpg",
    "page-donor_detail": "backgrounds/bg-donor.jpg",
    "page-profile": "backgrounds/bg-profile.jpg",
    "page-demand_prediction": "backgrounds/bg-medical.jpg",
    "page-donor_recognition": "backgrounds/bg-medical.jpg",
    
    # Image 4 - Emergency, Camps, Awareness, Inventory, Login
    "page-emergency_request": "backgrounds/bg-emergency.webp",
    "page-camp_list": "backgrounds/bg-camps.webp",
    "page-camp_form": "backgrounds/bg-camps.webp",
    "page-awareness": "backgrounds/bg-awareness.webp",
    "page-inventory_status": "backgrounds/bg-inventory.webp",
    "page-login": "backgrounds/bg-login.webp",
    "page-register": "backgrounds/bg-login.webp",
    
    # Default fallback
    "page-default": "backgrounds/bg-landing.avif",
}

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

def generate_css_rules():
    """Generate CSS rules for all pages"""
    css_rules = []
    
    # Default body background
    css_rules.append("""
/* User-provided background images */
body::before {
  content: "";
  position: fixed;
  inset: 0;
  display: block;
  background:
    url('../img/paper-noise.svg'),
    url('../img/backgrounds/bg-landing.avif'),
    radial-gradient(1200px 700px at 30% 40%, rgba(230,57,70,0.12), rgba(230,57,70,0) 60%),
    radial-gradient(900px 550px at 70% 60%, rgba(47,128,237,0.10), rgba(47,128,237,0) 55%),
    radial-gradient(900px 700px at 50% 80%, rgba(167,66,245,0.08), rgba(167,66,245,0) 55%);
  background-size: 1200px 800px, cover, auto, auto, auto;
  background-position: center, center center, center, center, center;
  background-repeat: repeat, no-repeat, no-repeat, no-repeat, no-repeat;
  opacity: 0.95;
  filter: blur(16px);
  transform: scale(1.08);
  transform-origin: center;
  pointer-events: none;
  z-index: 0;
}
""")
    
    # Individual page backgrounds
    for page_class, bg_image in PAGE_BACKGROUNDS.items():
        css_rules.append(f"""
body.{page_class}::before {{
  background:
    url('../img/paper-noise.svg'),
    url('../img/{bg_image}'),
    radial-gradient(1200px 700px at 30% 40%, rgba(230,57,70,0.12), rgba(230,57,70,0) 60%),
    radial-gradient(900px 550px at 70% 60%, rgba(47,128,237,0.10), rgba(47,128,237,0) 55%),
    radial-gradient(900px 700px at 50% 80%, rgba(167,66,245,0.08), rgba(167,66,245,0) 55%);
  background-size: 1200px 800px, cover, auto, auto, auto;
  background-position: center, center center, center, center, center;
  background-repeat: repeat, no-repeat, no-repeat, no-repeat, no-repeat;
}}
""")
    
    return "\n".join(css_rules)

def update_css():
    """Update CSS file with new background rules"""
    
    if not os.path.exists(CSS_FILE):
        print(f"✗ CSS file not found: {CSS_FILE}")
        return False
    
    # Read current CSS
    with open(CSS_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove old background rules
    # Find and remove the body::before section and all page-specific backgrounds
    pattern = r'body(?:\.[a-zA-Z_-]+)?::before\s*{[^}]+}'
    content = re.sub(pattern, '', content, flags=re.MULTILINE | re.DOTALL)
    
    # Generate new CSS rules
    new_rules = generate_css_rules()
    
    # Find a good place to insert (after the main styles, before animations)
    insert_marker = "/* Enhanced animations and visual effects */"
    if insert_marker in content:
        content = content.replace(insert_marker, new_rules + "\n\n" + insert_marker)
    else:
        # If marker not found, append to end
        content += "\n\n" + new_rules
    
    # Write updated CSS
    with open(CSS_FILE, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✓ Updated {CSS_FILE}")
    print(f"✓ Added {len(PAGE_BACKGROUNDS)} page-specific backgrounds")
    return True

def main():
    """Main function"""
    print("=" * 60)
    print("CSS Background Updater - User Images")
    print("=" * 60)
    print()
    
    # Backup CSS
    backup_css()
    print()
    
    # Update CSS
    print("Updating CSS with your 3 images...")
    if update_css():
        print()
        print("=" * 60)
        print("✓ CSS Updated Successfully!")
        print("=" * 60)
        print()
        print("Image Distribution:")
        print("  Image 1 (1.avif): Landing, Dashboard, Services, About")
        print("  Image 3 (3.jpg): Medical, Donor, Profile pages")
        print("  Image 4 (4.webp): Emergency, Camps, Awareness, Login")
        print()
        print("Next steps:")
        print("1. Clear browser cache (Ctrl+Shift+R)")
        print("2. Restart Django server")
        print("3. Visit different pages to see backgrounds")
        print()
        return 0
    else:
        print("\n✗ Failed to update CSS")
        return 1

if __name__ == "__main__":
    import sys
    sys.exit(main())
