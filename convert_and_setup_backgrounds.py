#!/usr/bin/env python3
"""
Convert provided images and set them as backgrounds for all pages
"""

import os
import shutil

# Source images
SOURCE_IMAGES = {
    "1.avif": "static/img/1.avif",
    "3.jpg": "static/img/3.jpg",
    "4.webp": "static/img/4.webp"
}

# Create backgrounds directory
BACKGROUNDS_DIR = "static/img/backgrounds"
os.makedirs(BACKGROUNDS_DIR, exist_ok=True)

# Distribution plan: Assign images to different page types
# We'll rotate the 3 images across all pages
IMAGE_DISTRIBUTION = {
    # Image 1 (1.avif) - Use for landing, dashboard, services
    "bg-landing.avif": "1.avif",
    "bg-dashboard.avif": "1.avif",
    "bg-services.avif": "1.avif",
    "bg-about.avif": "1.avif",
    
    # Image 3 (3.jpg) - Use for medical, donor, profile pages
    "bg-medical.jpg": "3.jpg",
    "bg-donor.jpg": "3.jpg",
    "bg-profile.jpg": "3.jpg",
    "bg-find-blood.jpg": "3.jpg",
    
    # Image 4 (4.webp) - Use for emergency, camps, awareness
    "bg-emergency.webp": "4.webp",
    "bg-camps.webp": "4.webp",
    "bg-awareness.webp": "4.webp",
    "bg-inventory.webp": "4.webp",
    "bg-login.webp": "4.webp",
}

def copy_images():
    """Copy and rename images to backgrounds folder"""
    print("=" * 60)
    print("Setting up background images")
    print("=" * 60)
    print()
    
    copied = 0
    
    for dest_name, source_name in IMAGE_DISTRIBUTION.items():
        source_path = f"static/img/{source_name}"
        dest_path = os.path.join(BACKGROUNDS_DIR, dest_name)
        
        if os.path.exists(source_path):
            shutil.copy2(source_path, dest_path)
            print(f"✓ Copied {source_name} → {dest_name}")
            copied += 1
        else:
            print(f"✗ Source not found: {source_path}")
    
    print()
    print(f"✓ Copied {copied} background images")
    print()
    return copied > 0

if __name__ == "__main__":
    if copy_images():
        print("✓ Images ready!")
        print()
        print("Next step: Run update_css_for_user_images.py to update CSS")
    else:
        print("✗ Failed to copy images")
