#!/usr/bin/env python3
"""
Quick setup script for chatbot API key
"""
import os
from pathlib import Path

def setup_chatbot_api_key():
    print("=" * 60)
    print("CHATBOT API KEY SETUP")
    print("=" * 60)
    print()
    print("The chatbot needs a Google Gemini API key to work.")
    print()
    print("Steps to get your API key:")
    print("1. Go to: https://makersuite.google.com/app/apikey")
    print("2. Sign in with your Google account")
    print("3. Click 'Create API Key'")
    print("4. Copy the key")
    print()
    
    api_key = input("Paste your Gemini API key here (or press Enter to skip): ").strip()
    
    if not api_key:
        print()
        print("⚠️  No API key provided. Chatbot will not work.")
        print("   You can add it later to the .env file")
        return
    
    # Update .env file
    env_path = Path(__file__).parent / '.env'
    
    try:
        # Read existing .env content
        if env_path.exists():
            with open(env_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            # Update or add GEMINI_API_KEY
            updated = False
            for i, line in enumerate(lines):
                if line.startswith('GEMINI_API_KEY='):
                    lines[i] = f'GEMINI_API_KEY={api_key}\n'
                    updated = True
                    break
            
            if not updated:
                lines.append(f'\nGEMINI_API_KEY={api_key}\n')
            
            # Write back
            with open(env_path, 'w', encoding='utf-8') as f:
                f.writelines(lines)
        else:
            # Create new .env file
            with open(env_path, 'w', encoding='utf-8') as f:
                f.write(f'# Google Gemini API Key for Chatbot\n')
                f.write(f'GEMINI_API_KEY={api_key}\n')
        
        print()
        print("✅ API key saved to .env file!")
        print()
        print("Next steps:")
        print("1. Restart your Django server (Ctrl+C then run again)")
        print("2. Open the website and test the chatbot")
        print()
        print("The chatbot button is in the bottom-right corner of the page.")
        
    except Exception as e:
        print()
        print(f"❌ Error saving API key: {e}")
        print()
        print("Manual setup:")
        print(f"1. Open the .env file in your project root")
        print(f"2. Add this line: GEMINI_API_KEY={api_key}")
        print(f"3. Save and restart Django server")

if __name__ == '__main__':
    setup_chatbot_api_key()
