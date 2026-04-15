#!/usr/bin/env python3
"""Test if .env file is being loaded correctly"""
import os
from pathlib import Path

# Test 1: Check if .env file exists
env_path = Path(__file__).parent / '.env'
print(f"1. .env file exists: {env_path.exists()}")
print(f"   Location: {env_path}")

# Test 2: Try to load with dotenv
try:
    from dotenv import load_dotenv
    print("2. python-dotenv is installed: ✓")
    
    # Load the .env file
    load_dotenv(env_path)
    print("3. load_dotenv() executed: ✓")
    
    # Test 3: Check if API key is in environment
    api_key = os.environ.get('GEMINI_API_KEY')
    if api_key:
        print(f"4. GEMINI_API_KEY found: ✓")
        print(f"   Key starts with: {api_key[:20]}...")
        print(f"   Key length: {len(api_key)} characters")
    else:
        print("4. GEMINI_API_KEY NOT found: ✗")
        print("   Available env vars:", [k for k in os.environ.keys() if 'API' in k or 'GEMINI' in k])
        
except ImportError as e:
    print(f"2. python-dotenv NOT installed: ✗")
    print(f"   Error: {e}")

# Test 4: Read .env file directly
print("\n5. Reading .env file directly:")
if env_path.exists():
    with open(env_path, 'r') as f:
        for line in f:
            if line.strip() and not line.strip().startswith('#'):
                print(f"   {line.strip()}")
