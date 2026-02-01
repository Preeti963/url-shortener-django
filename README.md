# URL Shortener with QR Code (Django)

This is a Django-based URL Shortener application that allows users to:
- Shorten long URLs
- Use custom short codes
- Track click counts
- Generate QR codes for each short URL
- Set optional expiration dates
- Register, login, logout, and reset passwords
---

## Features
- User authentication (Login, Logout, Register)
- Password reset functionality
- Custom short URLs
- QR code generation for each short URL
- Click tracking
- URL expiration support
- Downloadable QR codes

---

## Technologies Used
- Python 3
- Django
- SQLite
- HTML / Django Templates
- qrcode library

---

##  Setup Instructions

## Step 1: Clone the repository
git clone <your-github-repo-link>
cd url_shortener


## Step 2: Create a virtual environment
python3 -m venv venv

## Step 3: Activate the virtual environment
**On Mac/Linux:**
source venv/bin/activate
**On Windows:**
venv\Scripts\activate

## Step 4: Install dependencies
pip install -r requirements.txt
If you don’t have a requirements.txt file, create it with:
pip freeze > requirements.txt

## Step 5: Apply database migrations
python manage.py makemigrations
python manage.py migrate

## Step 6: Create a superuser  (for admin access)
python manage.py createsuperuser

## Step 7: Run the development server
python manage.py runserver

## Step 8: Open the app in your browser
Go to: http://127.0.0.1:8000/

## Step 9: Test features
-Register and login
-Create short URLs
-Click on QR codes or download them
-Reset your password(check in terminal )


