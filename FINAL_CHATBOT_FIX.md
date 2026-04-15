# Final Chatbot Fix - Step by Step

## Current Situation

The chatbot API key configuration has been added to Django settings, but you need a NEW API key because the current one is compromised.

## What You'll See Now

After restarting Django server, you'll likely see:
- Either: "Chatbot API key not configured" (if .env not loading)
- Or: "403 Your API key was reported as leaked" (if using old key)

Both mean you need a NEW API key.

## Complete Fix (5 Minutes)

### Step 1: Get a NEW API Key

1. Open: https://makersuite.google.com/app/apikey
2. Sign in with your Google account
3. Click "Create API Key" or "Get API Key"
4. **Copy the entire key** (starts with AIzaSy...)

### Step 2: Update Settings File

Open `bloodbank/settings.py` and find this line near the end:

```python
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY', 'AIzaSyDvl1W87N5v_ECY9i6lgFzbTNpdbXbXoRY')
```

Replace the old key with your NEW key:

```python
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY', 'YOUR_NEW_KEY_HERE')
```

### Step 3: Restart Django Server

1. Stop the server: Press `Ctrl+C`
2. Start again: `python manage.py runserver`

### Step 4: Test Chatbot

1. Open your website
2. Click the chatbot button (bottom-right corner)
3. Send a test message like "What is blood donation?"
4. You should get a response!

## Alternative: Use .env File (Recommended for Production)

If you want to use the .env file instead:

### Option A: Activate Virtual Environment First

```powershell
# Activate virtual environment
.\.venv\Scripts\Activate.ps1

# Install python-dotenv
pip install python-dotenv

# Restart Django
python manage.py runserver
```

### Option B: Install to System Python

```powershell
# Install python-dotenv globally
pip install python-dotenv

# Restart Django
python manage.py runserver
```

Then update `.env` file with your NEW key:
```
GEMINI_API_KEY=your_new_key_here
```

## Troubleshooting

### Still getting "API key not configured"?
- Make sure you saved the settings.py file
- Restart Django server
- Check there are no typos in the API key

### Getting "403 leaked key" error?
- You're using the old compromised key
- Get a NEW key from Google AI Studio
- Replace it in settings.py

### Chatbot not responding?
- Check browser console (F12) for JavaScript errors
- Verify Django server is running
- Check Django terminal for error messages

## Why This Happened

1. The original code had a hardcoded API key (security issue)
2. We removed it and switched to environment variables (secure)
3. The .env file wasn't loading properly (python-dotenv not installed in right place)
4. Temporary fix: Added key directly to settings.py
5. Final fix: Get NEW key and update settings.py

## Security Note

⚠️ **IMPORTANT**: The key in settings.py is visible in your code. For production:
1. Use environment variables
2. Never commit API keys to Git
3. Use .env file (already in .gitignore)

## Quick Test Commands

Test if API key is accessible:
```python
python manage.py shell
```

Then:
```python
from django.conf import settings
print(settings.GEMINI_API_KEY)
```

Should print your API key.

## Summary

✅ Contact page working
✅ Map integration added (needs Google Maps key)
✅ Chatbot security fixed
⚠️ Need NEW Gemini API key for chatbot to work

**Next Action**: Get a new API key and update `bloodbank/settings.py`
