# Chatbot API Key Setup

## Issue Fixed
✅ Removed leaked/hardcoded API key from chatbot code
✅ Updated to use environment variables for security

## Security Issue Resolved

The chatbot had a hardcoded Google Gemini API key that was reported as leaked. This has been removed and replaced with secure environment variable configuration.

## Setup Instructions

### Option 1: Using .env File (Recommended)

1. Open or create the `.env` file in your project root
2. Add your Gemini API key:

```env
GEMINI_API_KEY=your_new_api_key_here
```

3. Make sure `.env` is in your `.gitignore` file (it should already be there)

### Option 2: Using System Environment Variables

**Windows (PowerShell):**
```powershell
$env:GEMINI_API_KEY="your_new_api_key_here"
```

**Windows (Command Prompt):**
```cmd
set GEMINI_API_KEY=your_new_api_key_here
```

**Linux/Mac:**
```bash
export GEMINI_API_KEY=your_new_api_key_here
```

### Option 3: Using Django Settings

Add to `bloodbank/settings.py`:

```python
# Chatbot Configuration
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY', '')
```

## Getting a New Gemini API Key

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the key and add it to your `.env` file

**Important**: 
- Never commit API keys to Git
- Keep your `.env` file private
- Regenerate keys if they're exposed

## Testing the Chatbot

1. Set up your API key using one of the methods above
2. Restart your Django development server
3. Open the website and click the chatbot button (bottom right)
4. Try sending a message like "What blood types can donate to O+?"

## If Chatbot Doesn't Work

The chatbot will show an error message if:
- API key is not configured
- API key is invalid or expired
- API quota is exceeded

**Error Message**: "Chatbot API key not configured. Please set GEMINI_API_KEY in your environment variables or settings."

## Free Tier Limits

Google Gemini API offers a generous free tier:
- 60 requests per minute
- 1,500 requests per day
- More than enough for a blood bank website

## Alternative: Disable Chatbot

If you don't want to use the chatbot, you can hide it by adding this CSS to `static/css/styles.css`:

```css
.chatbot-container {
  display: none !important;
}
```

## Security Best Practices

1. ✅ Never hardcode API keys in source code
2. ✅ Use environment variables or secure vaults
3. ✅ Add `.env` to `.gitignore`
4. ✅ Rotate keys regularly
5. ✅ Set up API key restrictions in Google Cloud Console
6. ✅ Monitor API usage for unusual activity

## What Changed

**Before** (INSECURE):
```python
api_key = 'AIzaSyBzmw82xaZ3Dudn_XsThE3Tf74M9H4dMdU'  # Hardcoded - BAD!
```

**After** (SECURE):
```python
api_key = os.environ.get('GEMINI_API_KEY') or os.environ.get('GOOGLE_API_KEY') or getattr(settings, 'GEMINI_API_KEY', None)
```

The chatbot now safely reads the API key from environment variables instead of having it exposed in the code.
