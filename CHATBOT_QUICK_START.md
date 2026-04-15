# Chatbot Quick Start Guide

## Current Status
✅ Contact page working
✅ Map integration added (needs Google Maps API key)
✅ Chatbot security fixed (hardcoded keys removed)
⚠️ Chatbot needs API key to function

## Quick Setup (2 Minutes)

### Option 1: Automated Setup (Easiest)

Run this command:
```bash
python setup_chatbot.py
```

Follow the prompts to paste your API key.

### Option 2: Manual Setup

1. **Get API Key**
   - Go to: https://makersuite.google.com/app/apikey
   - Sign in with Google
   - Click "Create API Key"
   - Copy the key

2. **Add to .env File**
   - Open `.env` file in project root
   - Replace the placeholder:
   ```env
   GEMINI_API_KEY=paste_your_actual_key_here
   ```
   - Save the file

3. **Restart Django**
   - Stop the server (Ctrl+C)
   - Start again: `python manage.py runserver`

4. **Test**
   - Open website
   - Click chatbot button (bottom-right)
   - Send a message

## Troubleshooting

### Error: "Chatbot API key not configured"
**Solution**: Add your API key to `.env` file and restart Django server

### Error: "403 Your API key was reported as leaked"
**Solution**: The old key was exposed. Get a NEW key from Google AI Studio

### Chatbot button not visible
**Solution**: Check browser console for errors, ensure CSS is loaded

### Chatbot not responding
**Solution**: 
1. Check API key is correct in `.env`
2. Verify Django loaded the `.env` file (restart server)
3. Check browser console for JavaScript errors

## Free Tier Limits

Google Gemini API free tier:
- ✅ 60 requests per minute
- ✅ 1,500 requests per day
- ✅ No credit card required

More than enough for testing and small websites!

## Features

The chatbot can help with:
- Blood donation information
- Blood group compatibility
- Emergency request guidance
- Donor eligibility questions
- Blood bank information

## Security Notes

- ✅ `.env` file is in `.gitignore` (not committed to Git)
- ✅ API key loaded from environment variables
- ✅ No hardcoded keys in source code
- ⚠️ Keep your `.env` file private
- ⚠️ Don't share API keys

## Alternative: Disable Chatbot

If you don't want to use the chatbot, add this to `static/css/styles.css`:

```css
/* Hide chatbot */
.chatbot-container {
  display: none !important;
}
```

## Summary

1. Get API key from https://makersuite.google.com/app/apikey
2. Add to `.env` file: `GEMINI_API_KEY=your_key`
3. Restart Django server
4. Test chatbot on website

That's it! 🎉
