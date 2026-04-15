@echo off
echo ========================================
echo Adding Sample Data to Blood Bank
echo ========================================
echo.

echo Activating virtual environment...
call .venv\Scripts\activate.bat

echo.
echo Adding sample data...
python manage.py add_sample_data

echo.
echo ========================================
echo Sample data added successfully!
echo ========================================
echo.
echo You can now:
echo - Find donors by blood group
echo - View inventory with blood stock
echo - See blood banks on map
echo - View dashboard with real data
echo.
pause
