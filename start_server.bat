@echo off
echo ========================================
echo Starting Blood Bank Server
echo ========================================
echo.

echo Activating virtual environment...
call .venv\Scripts\activate.bat

echo.
echo Running migrations...
python manage.py makemigrations
python manage.py migrate

echo.
echo Starting Django server...
echo Server will be available at: http://127.0.0.1:8000
echo Press Ctrl+C to stop the server
echo.
python manage.py runserver
