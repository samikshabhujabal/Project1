#!/usr/bin/env python3
"""
Blood Bank Background Images Downloader
Downloads high-quality medical/healthcare themed images from Unsplash
"""

import os
import urllib.request
import sys

# Create backgrounds directory
BACKGROUNDS_DIR = "static/img/backgrounds"
os.makedirs(BACKGROUNDS_DIR, exist_ok=True)

# High-resolution Unsplash image URLs
# All images are 1920x1080 or higher, optimized for web use
# Free to use under Unsplash License

IMAGES = {
    "bg-landing.jpg": {
        "url": "https://images.unsplash.com/photo-1519494026892-80bbd2d6fd0d?w=1920&h=1080&fit=crop&q=85",
        "description": "Modern hospital building exterior - clean, professional"
    },
    "bg-dashboard.jpg": {
        "url": "https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=1920&h=1080&fit=crop&q=85",
        "description": "Medical technology and data - blue tones"
    },
    "bg-emergency.jpg": {
        "url": "https://images.unsplash.com/photo-1587351021759-3e566b6af7cc?w=1920&h=1080&fit=crop&q=85",
        "description": "Emergency medical scene - urgent, red tones"
    },
    "bg-donor.jpg": {
        "url": "https://images.unsplash.com/photo-1615461066841-6116e61058f4?w=1920&h=1080&fit=crop&q=85",
        "description": "Blood donation - caring hands, medical care"
    },
    "bg-medical.jpg": {
        "url": "https://images.unsplash.com/photo-1538108149393-fbbd81895907?w=1920&h=1080&fit=crop&q=85",
        "description": "Hospital corridor - clean, bright, modern"
    },
    "bg-profile.jpg": {
        "url": "https://images.unsplash.com/photo-1559839734-2b71ea197ec2?w=1920&h=1080&fit=crop&q=85",
        "description": "Healthcare professionals - friendly, team"
    },
    "bg-awareness.jpg": {
        "url": "https://images.unsplash.com/photo-1532938911079-1b06ac7ceec7?w=1920&h=1080&fit=crop&q=85",
        "description": "Medical education - books, learning"
    },
    "bg-camps.jpg": {
        "url": "https://images.unsplash.com/photo-1582213782179-e0d53f98f2ca?w=1920&h=1080&fit=crop&q=85",
        "description": "Community health event - outdoor, people"
    },
    "bg-about.jpg": {
        "url": "https://images.unsplash.com/photo-1586773860418-d37222d8fce3?w=1920&h=1080&fit=crop&q=85",
        "description": "Hospital interior - professional, welcoming"
    },
    "bg-services.jpg": {
        "url": "https://images.unsplash.com/photo-1579684385127-1ef15d508118?w=1920&h=1080&fit=crop&q=85",
        "description": "Medical services - equipment, care"
    },
    "bg-inventory.jpg": {
        "url": "https://images.unsplash.com/photo-1584515933487-779824d29309?w=1920&h=1080&fit=crop&q=85",
        "description": "Medical supplies - organized, professional"
    },
    "bg-login.jpg": {
        "url": "https://images.unsplash.com/photo-1576091160550-2173dba999ef?w=1920&h=1080&fit=crop&q=85",
        "description": "Medical technology - secure, modern"
    },
    "bg-hospital-room.jpg": {
        "url": "https://images.unsplash.com/photo-1519494140681-8b17d830a3ec?w=1920&h=1080&fit=crop&q=85",
        "description": "Hospital patient room - clean, comfortable"
    },
    "bg-lab.jpg": {
        "url": "https://images.unsplash.com/photo-1582719471384-894fbb16e074?w=1920&h=1080&fit=crop&q=85",
        "description": "Medical laboratory - scientific, precise"
    },
    "bg-surgery.jpg": {
        "url": "https://images.unsplash.com/photo-1551190822-a9333d879b1f?w=1920&h=1080&fit=crop&q=85",
        "description": "Operating room - professional, sterile"
    },
}

def download_image(url, filename, description):
    """Download an image from URL to filename"""
    filepath = os.path.join(BACKGROUNDS_DIR, filename)
    
    if os.path.exists(filepath):
        print(f"✓ {filename} already exists, skipping...")
        return True
    
    try:
        print(f"⬇ Downloading {filename} ({description})...")
        
        # Add user agent to avoid 403 errors
        req = urllib.request.Request(
            url,
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        
        with urllib.request.urlopen(req) as response:
            data = response.read()
            
        with open(filepath, 'wb') as f:
            f.write(data)
            
        file_size = len(data) / 1024  # KB
        print(f"  ✓ Downloaded {filename} ({file_size:.1f} KB)")
        return True
        
    except Exception as e:
        print(f"  ✗ Error downloading {filename}: {e}")
        return False

def main():
    """Main function to download all images"""
    print("=" * 60)
    print("Blood Bank Background Images Downloader")
    print("=" * 60)
    print()
    
    print(f"📁 Saving images to: {BACKGROUNDS_DIR}/")
    print()
    
    success_count = 0
    total_count = len(IMAGES)
    
    for filename, info in IMAGES.items():
        if download_image(info["url"], filename, info["description"]):
            success_count += 1
        print()
    
    print("=" * 60)
    print(f"✓ Downloaded {success_count}/{total_count} images successfully")
    print("=" * 60)
    print()
    
    if success_count == total_count:
        print("🎉 All images downloaded successfully!")
        print()
        print("Next steps:")
        print("1. Check the images in static/img/backgrounds/")
        print("2. Run update_css_backgrounds.py to update CSS")
        print("3. Test the website to see new backgrounds")
    else:
        print("⚠ Some images failed to download.")
        print("You can manually download them from Unsplash.com")
    
    return 0 if success_count == total_count else 1

if __name__ == "__main__":
    sys.exit(main())
