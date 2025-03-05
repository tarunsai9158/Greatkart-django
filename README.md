# Greatkart-django




# GreatKart - Django E-commerce Website

GreatKart is a fully functional e-commerce platform built with Django. It includes essential features like product management, user authentication, shopping cart, order placement, and payment integration.

## Features
- User authentication (Login, Register, Logout, Profile Management)
- Product categories and filtering
- Shopping cart with product variations
- Secure checkout with payment integration
- Order tracking and order history
- Email notifications for orders
- Admin dashboard for product and order management

## Technologies Used
- **Backend:** Django, Python
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** SQLite (Can be replaced with PostgreSQL or MySQL)
- **Payment Gateway:** PayPal or Stripe
- **Deployment:** Heroku or AWS (optional)

## Installation & Setup

### 1. Clone the repository
```bash
 git clone https://github.com/tarunsai9158/Greatkart-django.git
 cd greatkart
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure database migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a superuser
```bash
python manage.py createsuperuser
```
Follow the prompts to create an admin account.

### 6. Run the development server
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000/` in your browser.

## Environment Variables
Create a `.env` file in the project root and add the following configurations:
```
SECRET_KEY=your_django_secret_key
DEBUG=True
ALLOWED_HOSTS=*
DATABASE_URL=sqlite:///db.sqlite3  # Change as needed for PostgreSQL/MySQL
```

SMTP Configuration

To enable email notifications (such as order confirmations), configure the SMTP settings in the .env file:

# SMTP CONFIGURATION
EMAIL_BACKEND=config('EMAIL_BACKEND')
EMAIL_HOST=config('EMAIL_HOST')
EMAIL_PORT=config('EMAIL_PORT', cast=int)
EMAIL_USE_TLS=config('EMAIL_USE_TLS', cast=bool)
EMAIL_HOST_USER=config('EMAIL_HOST_USER')  # Replace with your email
EMAIL_HOST_PASSWORD=config('EMAIL_HOST_PASSWORD')  # Replace with your email password

⚠️ Important: Before running the project, ensure you update your .env file with valid email credentials.



## Deployment
To deploy the project, follow these steps:
- Use services like **Heroku, AWS, or DigitalOcean**
- Set `DEBUG=False` and configure allowed hosts
- Use a production-ready database like PostgreSQL

## Contribution
Feel free to submit issues or pull requests. Follow the [contribution guidelines](CONTRIBUTING.md) for more details.


### Author
Developed by PEELA TARUN SAI - [GitHub](https://github.com/tarunsai9158)

