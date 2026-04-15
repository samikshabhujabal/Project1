#!/usr/bin/env python3
"""
Update CSS to use PNG/JPG backgrounds instead of SVG
"""

import os
import re

CSS_FILE = "static/css/styles.css"
BACKUP_FILE = "static/css/styles.css.backup"

# Mapping of SVG files to new JPG/PNG files
BACKGROUND_MAPPING = {
    "bg-landing-hero.svg": "backgrounds/bg-landing.jpg",
    "bg-dashboard.svg": "backgrounds/bg-dashboard.jpg",
    "bg-services.svg": "backgrounds/bg-services.jpg",
    "bg-inventory.svg": "backgrounds/bg-inventory.jpg",
    "bg-awareness.svg": "backgrounds/bg-awareness.jpg",
    "bg-emergency.svg": "backgrounds/bg-emergency.jpg",
    "bg-camps.svg": "backgrounds/bg-camps.jpg",
    "bg-profile.svg": "backgrounds/bg-profile.jpg",
    "bg-login.svg": "backgrounds/bg-login.jpg",
    "bg-donor.svg": "backgrounds/bg-donor.jpg",
    "bg-medical.svg": "backgrounds/bg-medical.jpg",
    "bg-about.svg": "backgrounds/bg-about.jpg",
    "bg-request.svg": "backgrounds/bg-emergency.jpg",
    "hero-bg.svg": "backgrounds/bg-landing.jpg",
}

def backup_css():
    """Create a backup of the CSS file"""
    if not os.path.exists(BACKUP_FILE):
        with open(CSS_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
        with open(BACKUP_FILE, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ Created backup: {BACKUP_FILE}")
    else:
        print(f"✓ Backup already exists: {BACKUP_FILE}")

def update_css_backgrounds():
    """Update CSS file to use new background images"""
    
    if not os.path.exists(CSS_FILE):
        print(f"✗ CSS file not found: {CSS_FILE}")
        return False
    
    # Read CSS file
    with open(CSS_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    replacements_made = 0
    
    # Replace each SVG reference with JPG/PNG
    for old_bg, new_bg in BACKGROUND_MAPPING.items():
        old_pattern = f"url\\(['\"]?\\.\\./{re.escape('img/' + old_bg)}['\"]?\\)"
        new_url = f"url('../img/{new_bg}')"
        
        # Count occurrences
        count = len(re.findall(old_pattern, content))
        if count > 0:
            content = re.sub(old_pattern, new_url, content)
            replacements_made += count
            print(f"  ✓ Replaced {old_bg} → {new_bg} ({count} occurrence(s))")
    
    # Also update any remaining svg references
    svg_pattern = r"url\(['\"]?\.\./img/bg-[^)]+\.svg['\"]?\)"
    remaining_svgs = re.findall(svg_pattern, content)
    
    if remaining_svgs:
        print(f"\n⚠ Found {len(remaining_svgs)} remaining SVG references:")
        for svg in set(remaining_svgs):
            print(f"    {svg}")
    
    # Write updated content
    if content != original_content:
        with open(CSS_FILE, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"\n✓ Updated {CSS_FILE}")
        print(f"✓ Made {replacements_made} replacements")
        return True
    else:
        print("\n✓ No changes needed")
        return True

def add_image_overlay_styles():
    """Add CSS for image overlays to improve text readability"""
    
    overlay_css = """

/* Background image overlays for better text readability */
body::before {
  /* Add a subtle overlay to darken/lighten backgrounds */
  background-color: rgba(255, 255, 255, 0.85) !important;
  background-blend-mode: overlay;
}

/* Adjust individual page overlays if needed */
body.page-emergency_request::before {
  background-color: rgba(255, 245, 245, 0.90) !important;
}

body.page-dashboard::before {
  background-color: rgba(245, 250, 255, 0.90) !important;
}

/* Ensure backgrounds cover and center properly */
body::before {
  background-size: cover !important;
  background-position: center center !important;
  background-repeat: no-repeat !important;
  background-attachment: fixed !important;
}
"""
    
    with open(CSS_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if overlay styles already exist
    if "Background image overlays for better text readability" not in content:
        with open(CSS_FILE, 'a', encoding='utf-8') as f:
            f.write(overlay_css)
        print("✓ Added image overlay styles for better readability")
        return True
    else:
        print("✓ Overlay styles already exist")
        return False

def main():
    """Main function"""
    print("=" * 60)
    print("CSS Background Updater")
    print("=" * 60)
    print()
    
    # Create backup
    backup_css()
    print()
    
    # Update backgrounds
    print("Updating background references...")
    if update_css_backgrounds():
        print()
        
        # Add overlay styles
        print("Adding overlay styles...")
        add_image_overlay_styles()
        print()
        
        print("=" * 60)
        print("✓ CSS updated successfully!")
        print("=" * 60)
        print()
        print("Next steps:")
        print("1. Clear browser cache (Ctrl+Shift+R)")
        print("2. Reload the website")
        print("3. Check all pages for new backgrounds")
        print()
        print(f"Note: Original CSS backed up to {BACKUP_FILE}")
        return 0
    else:
        print("\n✗ Failed to update CSS")
        return 1

if __name__ == "__main__":
    import sys
    sys.exit(main())
