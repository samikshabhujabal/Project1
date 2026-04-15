#!/usr/bin/env python3
"""Test chatbot configuration in Django context"""
import os
import sys
import django

# Setup Django
sys.path.insert(0, os.path.dirname(__file__))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bloodbank.settings')
django.setup()

from django.conf import settings

print("=" * 60)
print("CHATBOT CONFIGURATION TEST")
print("=" * 60)

# Test 1: Check os.environ
api_key_env = os.environ.get('GEMINI_API_KEY')
print(f"\n1. os.environ.get('GEMINI_API_KEY'):")
if api_key_env:
    print(f"   ✓ Found: {api_key_env[:20]}... (length: {len(api_key_env)})")
else:
    print(f"   ✗ Not found")

# Test 2: Check Django settings
api_key_settings = getattr(settings, 'GEMINI_API_KEY', None)
print(f"\n2. settings.GEMINI_API_KEY:")
if api_key_settings:
    print(f"   ✓ Found: {api_key_settings[:20]}... (length: {len(api_key_settings)})")
else:
    print(f"   ✗ Not found")

# Test 3: Check the exact logic from chatbot view
api_key = os.environ.get('GEMINI_API_KEY') or os.environ.get('GOOGLE_API_KEY') or getattr(settings, 'GEMINI_API_KEY', None)
print(f"\n3. Chatbot view logic result:")
if api_key:
    print(f"   ✓ API key will be used: {api_key[:20]}...")
else:
    print(f"   ✗ No API key found - chatbot will fail")

# Test 4: Try to configure genai
print(f"\n4. Testing Google Generative AI:")
try:
    import google.generativeai as genai
    if api_key:
        genai.configure(api_key=api_key)
        print(f"   ✓ genai.configure() succeeded")
    else:
        print(f"   ✗ No API key to test")
except Exception as e:
    print(f"   ✗ Error: {e}")

print("\n" + "=" * 60)
if api_key:
    print("✓ Configuration looks good!")
    print("  If chatbot still doesn't work, the API key might be invalid.")
    print("  Get a new key from: https://makersuite.google.com/app/apikey")
else:
    print("✗ Configuration problem detected!")
    print("  Make sure .env file has: GEMINI_API_KEY=your_key_here")
    print("  Then restart Django server")
print("=" * 60)
