# Data Management Guide

## Quick Setup - Add Sample Data

Run this command to add sample data:

```bash
# Windows
add_sample_data.bat

# Or manually
python manage.py add_sample_data
```

This will add:
- ✅ 20 sample donors (various blood groups and cities)
- ✅ Blood stock for all 8 blood groups
- ✅ 5 blood banks with map coordinates
- ✅ 10 recent donations
- ✅ 5 blood requests
- ✅ 3 upcoming camps

## How Data Updates Work

### 1. Adding Donors
**Via Admin Panel:**
1. Go to `/admin/`
2. Click "Donors" → "Add Donor"
3. Fill in details (name, blood group, city, etc.)
4. Save

**Result:**
- Donor appears in "Find Donor" search
- Can be filtered by blood group and city
- Shows in dashboard statistics

### 2. Adding Donations
**Via Admin Panel:**
1. Go to `/admin/`
2. Click "Donations" → "Add Donation"
3. Select donor and blood group
4. Enter units collected
5. Save

**Result:**
- ✅ Blood stock automatically increases
- ✅ Dashboard shows updated inventory
- ✅ Inventory page reflects new units
- ✅ Donor's last donation date updates

### 3. Fulfilling Blood Requests
**Via Admin Panel:**
1. Go to `/admin/`
2. Click "Blood Requests"
3. Select a request
4. Change status to "Fulfilled"
5. Save

**Result:**
- ✅ Blood stock automatically decreases
- ✅ Dashboard shows updated inventory
- ✅ Used units increase
- ✅ Available units decrease

### 4. Adding Blood Banks
**Via Admin Panel:**
1. Go to `/admin/`
2. Click "Blood Banks" → "Add Blood Bank"
3. Fill in details including latitude/longitude
4. Save

**Result:**
- ✅ Appears on map in "Find Blood Bank"
- ✅ Shows in search results
- ✅ Marker added to map

## Testing the Features

### Test Find Donor
1. Go to "Find Donor" page
2. Select blood group (e.g., "A+")
3. Enter city (e.g., "Mumbai")
4. Click Search
5. Should show matching donors

### Test Dashboard
1. Login as admin
2. Go to Dashboard
3. Should see:
   - Total donors count
   - Available blood units
   - Pending requests
   - Blood stock by group
   - Recent donors
   - Emergency requests

### Test Inventory
1. Login as admin
2. Go to "Inventory Status"
3. Should see:
   - Blood stock for each group
   - Total units
   - Low stock alerts
   - Recent donations

### Test Find Blood Bank
1. Go to "Find Blood Bank"
2. Map should show markers for blood banks
3. Click markers to see details
4. Filter by blood group
5. Search by city

## Data Flow

```
Add Donor → Shows in Find Donor
    ↓
Add Donation → Increases Blood Stock → Updates Dashboard/Inventory
    ↓
Blood Request (Fulfilled) → Decreases Blood Stock → Updates Dashboard/Inventory
```

## Manual Data Entry

### Add Donor Manually
```python
python manage.py shell
```

```python
from donors.models import Donor
from django.utils import timezone

donor = Donor.objects.create(
    name="John Doe",
    blood_group="O+",
    email="john@example.com",
    phone_number="+919876543210",
    city="Mumbai",
    address="123 Main St",
    state="Maharashtra",
    pincode="400001",
    date_of_birth=timezone.now().date(),
    gender="M",
    weight=70,
    eligibility_status=Donor.Eligibility.ELIGIBLE
)
```

### Add Blood Stock Manually
```python
from inventory.models import BloodStock
from django.utils import timezone
from datetime import timedelta

stock = BloodStock.objects.create(
    blood_group="A+",
    available_units=25,
    total_units=25,
    expiry_date=timezone.now().date() + timedelta(days=60)
)
```

## Troubleshooting

### No donors showing in Find Donor
**Solution**: Run `python manage.py add_sample_data`

### Dashboard shows 0 units
**Solution**: 
1. Add blood stock via admin
2. Or add donations (auto-updates stock)

### Map not showing blood banks
**Solution**: 
1. Add blood banks via admin
2. Make sure latitude/longitude are filled
3. Check browser console for errors

### Stock not updating after donation
**Solution**: 
1. Make sure donation has blood_group set
2. Check admin messages for confirmation
3. Refresh dashboard page

## Reset Data

To start fresh:
```bash
python manage.py flush
python manage.py migrate
python manage.py createsuperuser
python manage.py add_sample_data
```

## Summary

✅ Sample data command adds realistic test data
✅ Donations automatically increase blood stock
✅ Fulfilled requests automatically decrease stock
✅ Dashboard and inventory update in real-time
✅ Find Donor shows all eligible donors
✅ Map shows all blood banks with coordinates

Run `add_sample_data.bat` to get started with test data!
