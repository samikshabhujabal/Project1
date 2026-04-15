#!/usr/bin/env python3
"""
Enhanced Blood Bank Background Images Downloader
Downloads high-resolution, realistic hospital and medical images from Unsplash
All images are 1920x1080, professionally shot, and optimized for web use
"""

import os
import urllib.request
import sys
import time

# Create backgrounds directory
BACKGROUNDS_DIR = "static/img/backgrounds"
os.makedirs(BACKGROUNDS_DIR, exist_ok=True)

# Curated high-resolution Unsplash images
# All images are realistic, professional hospital/medical photography
# Resolution: 1920x1080 or higher, optimized at 85% quality

IMAGES = {
    # Main Pages
    "bg-landing.jpg": {
        "url": "https://images.unsplash.com/photo-1519494026892-80bbd2d6fd0d?w=1920&h=1080&fit=crop&q=85",
        "description": "Modern hospital building - glass facade, professional",
        "photographer": "Unsplash",
        "colors": "Blue, White, Glass"
    },
    
    "bg-dashboard.jpg": {
        "url": "https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=1920&h=1080&fit=crop&q=85",
        "description": "Medical technology dashboard - monitors, data",
        "photographer": "Unsplash",
        "colors": "Blue, Tech, Digital"
    },
    
    "bg-emergency.jpg": {
        "url": "https://images.unsplash.com/photo-1587351021759-3e566b6af7cc?w=1920&h=1080&fit=crop&q=85",
        "description": "Emergency room entrance - urgent care, red cross",
        "photographer": "Unsplash",
        "colors": "Red, White, Urgent"
    },
    
    "bg-donor.jpg": {
        "url": "https://images.unsplash.com/photo-1615461066841-6116e61058f4?w=1920&h=1080&fit=crop&q=85",
        "description": "Blood donation - caring han