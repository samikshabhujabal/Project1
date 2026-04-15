# Email Setup Guide for OTP

## Quick Setup (Gmail)

### Step 1: Enable 2-Factor Authentication
1. Go to https://myaccount.google.com/security
2. Click on "2-Step Verification"
3. Follow the steps to enable it

### Step 2: Generate App Password
1. Go to https://myaccount.google.com/apppasswords
2. Select "Mail" and "Windows Computer" (or Other)
3. Click "Generate"
4. Copy the 16-character password (remove spaces)

### Step 3: Update .env File
Open `.env` file and update:

```env
EMAIL_HOST_USER=your-actual-email@gmail.com
EMAIL_HOST_PASSWORD=your-16-char-app-password
```

Example:
```env
EMAIL_HOST_USER=bloodbank@gmail.com
EMAIL_HOST_PASSWORD=abcd efgh ijkl mnop
```

### Step 4: Restart Django Server
```bash
# Stop server (Ctrl+C)
# Start again
python manage.py runserver
```

## Testing

1. Go to registration page
2. Fill out the form with a real email address
3. Click Register
4. Check your email inbox for OTP
5. Enter OTP on verification page
6. Account activated!

## Troubleshooting

### Error: "SMTPAuthenticationError"
- Check EMAIL_HOST_USER is correct
- Check EMAIL_HOST_PASSWORD is the App Password (not your regular password)
- Make sure 2-Factor Authentication is enabled

### Error: "Connection refused"
- Check internet connection
- Gmail SMTP might be blocked by firewall
- Try using port 465 with EMAIL_USE_SSL=True instead

### Email not received
- Check spam/junk folder
- Wait a few minutes (can take 1-5 minutes)
- Verify email address is correct
- Check Gmail account is active

### Alternative: Use Console Backend (Development Only)
If you can't set up Gmail, use console backend:

In `bloodbank/settings.py`, change:
```python
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

OTP will print in terminal instead of sending email.

## Map Fixed!

The map now uses OpenStreetMap (Leaflet) which:
- ✅ Works without API key
- ✅ Shows blood bank locations
- ✅ Shows your current location (with permission)
- ✅ Interactive markers with popups
- ✅ "Get Directions" links

## Summary

✅ Email sending configured with Gmail SMTP
✅ OTP sent to real email (not popup)
✅ Map working with OpenStreetMap
⚠️ Need to add your Gmail credentials to .env
⚠️ Need to restart Django server

After setup, registration will send real OTP emails!
