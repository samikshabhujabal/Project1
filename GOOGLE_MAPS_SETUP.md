# Google Maps Setup Instructions

## Issue Fixed
✅ Contact page created and working
✅ Map integration added to Find Blood Bank page

## To Enable Google Maps

The map on the Find Blood Bank page requires a Google Maps API key. Follow these steps:

### 1. Get a Google Maps API Key

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable the following APIs:
   - Maps JavaScript API
   - Geocoding API (optional, for address lookup)
4. Go to "Credentials" and create an API key
5. Restrict the API key to your domain for security

### 2. Add the API Key to Your Template

Open `templates/core/find_blood_bank.html` and find this line:

```html
<script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&callback=initMap" async defer></script>
```

Replace `YOUR_API_KEY` with your actual Google Maps API key:

```html
<script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX&callback=initMap" async defer></script>
```

### 3. Add Coordinates to Blood Banks

For the map to show blood bank locations, you need to add latitude and longitude to your blood banks in the admin panel:

1. Go to Django Admin
2. Navigate to Blood Banks
3. Edit each blood bank and add:
   - Latitude (e.g., 18.5204)
   - Longitude (e.g., 73.8567)

You can get coordinates from Google Maps by right-clicking on a location.

### 4. Fallback Behavior

If the API key is not configured, the map will show a placeholder message and users can still see the list of blood banks on the left side.

## Features Implemented

### Contact Page (`/contact/`)
- Contact form with name, email, phone, subject, and message
- Contact information display (address, phone, email, hours)
- Quick links to emergency services
- Futuristic AI theme styling
- Form submission with success/error messages

### Map on Find Blood Bank Page
- Interactive Google Maps integration
- Markers for each blood bank with coordinates
- Info windows showing bank details and blood groups
- "Get Directions" link for each bank
- User location detection (with permission)
- Auto-zoom to fit all markers
- Fallback UI if API key not configured

## Testing Without API Key

The page will work without an API key - it will show:
- List of blood banks on the left (fully functional)
- Placeholder message on the map area
- All search and filter functionality works

## Cost Information

Google Maps offers a free tier:
- $200 free credit per month
- Covers approximately 28,000 map loads per month
- More than enough for most blood bank websites

## Security Best Practices

1. Restrict your API key to specific domains
2. Set usage limits in Google Cloud Console
3. Monitor usage regularly
4. Never commit API keys to public repositories
5. Consider using environment variables for production
