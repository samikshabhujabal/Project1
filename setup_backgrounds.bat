@echo off
echo ============================================================
echo Blood Bank Background Images Setup
echo ============================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from https://www.python.org/
    pause
    exit /b 1
)

echo Step 1: Creating backgrounds folder...
if not exist "static\img\backgrounds" (
    mkdir "static\img\backgrounds"
    echo Created: static\img\backgrounds\
) else (
    echo Folder already exists: static\img\backgrounds\
)
echo.

echo Step 2: Downloading background images...
echo This may take a few minutes depending on your internet speed...
echo.
python download_backgrounds.py
if errorlevel 1 (
    echo.
    echo WARNING: Some images failed to download
    echo You can download them manually from Unsplash.com
    echo See QUICK_DOWNLOAD_LINKS.md for direct links
    echo.
)

echo.
echo Step 3: Updating CSS to use new backgrounds...
python update_css_backgrounds.py
if errorlevel 1 (
    echo ERROR: Failed to update CSS
    pause
    exit /b 1
)

echo.
echo ============================================================
echo Setup Complete!
echo ============================================================
echo.
echo Next steps:
echo 1. Check images in: static\img\backgrounds\
echo 2. Clear your browser cache (Ctrl+Shift+R)
echo 3. Restart Django server: python manage.py runserver
echo 4. Visit your website to see new backgrounds
echo.
echo Backup created: static\css\styles.css.backup
echo.
pause
