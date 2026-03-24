# CSE3D - Project Definition

## 📋 Project Overview

**CSE3D** is a Django-based web application that provides user authentication, informational pages, and a contact management system. It serves as a platform for users to log in, access content, and submit contact inquiries.

**Technology Stack:**
- **Framework:** Django 5.2.12
- **Language:** Python
- **Database:** SQLite3 (db.sqlite3)
- **Frontend:** HTML, CSS, JavaScript

---

## 🎯 Project Purpose

The application is designed to:
1. Provide secure user authentication (login/signup)
2. Display informational content (home, about pages)
3. Enable user contact/feedback submission
4. Manage contact inquiries in the admin panel

---

## 📁 Project Structure

```
CSE3D/
├── CSE3D/                 # Project configuration folder
│   ├── settings.py        # Django settings & app configuration
│   ├── urls.py            # Main URL routing (includes Shop app)
│   ├── asgi.py            # ASGI configuration for deployment
│   ├── wsgi.py            # WSGI configuration for deployment
│   └── __init__.py        # Package initializer
│
├── Shop/                  # Main Django app
│   ├── models.py          # Database models (Contact model)
│   ├── views.py           # View functions (auth, pages, contact)
│   ├── urls.py            # App-specific URL routing
│   ├── admin.py           # Django admin configuration
│   ├── apps.py            # App configuration
│   ├── tests.py           # Unit tests
│   └── migrations/        # Database migration files
│
├── static/                # Static files (CSS, JS, images)
│   ├── css/               # Stylesheets
│   │   ├── base.css
│   │   ├── index.css
│   │   ├── login.css
│   │   └── signup.css
│   ├── img/               # Images
│   └── js/                # JavaScript files
│
├── templates/             # HTML templates
│   ├── base.html          # Base template (extends to other pages)
│   ├── index.html         # Home page (requires login)
│   ├── about.html         # About page
│   ├── contact.html       # Contact form page
│   ├── login.html         # Login page
│   └── signup.html        # Sign-up page
│
├── db.sqlite3             # SQLite database
├── manage.py              # Django management script
└── README.md              # This file
```

---

## 🗄️ Database Models

### Contact Model
Stores user contact inquiries:
- **Fields:**
  - `name` (CharField, max 100 chars) - Submitter's name
  - `email` (CharField, max 100 chars) - Contact email
  - `phone` (CharField, max 100 chars) - Phone number
  - `msg` (CharField, max 100 chars) - Contact message

---

## 🔐 Authentication & Authorization

### User Views
- **Login** (`/login`) - Authenticate existing users
- **Signup** (`/signup`) - Create new user accounts
- **Logout** (`/logout`) - Terminate user sessions

### Protected Routes
- **Home Page** (`/`) - `@login_required` decorator (users must be authenticated)

---

## 🌐 URL Routes

| Route | View | Method | Protected |
|-------|------|--------|-----------|
| `/` | `index` | GET | ✅ Yes |
| `/about` | `about` | GET | ❌ No |
| `/contact` | `contact` | GET/POST | ❌ No |
| `/login` | `login` | GET/POST | ❌ No |
| `/signup` | `signup` | GET/POST | ❌ No |
| `/logout` | `logout` | GET | ❌ No |
| `/admin` | Django Admin | GET/POST | ✅ Yes (staff only) |

---

## 📄 Template Pages

| Template | Purpose | Status |
|----------|---------|--------|
| `base.html` | Base layout template | Extends to other pages |
| `index.html` | Home/dashboard page | Login required |
| `about.html` | About information | Public |
| `contact.html` | Contact form & inquiries | Public |
| `login.html` | User login form | Public |
| `signup.html` | User registration form | Public |

---

## ⚙️ Features

### 1. **User Authentication**
   - User registration with email and password confirmation
   - User login with Django's built-in authentication system
   - Password validation and user creation
   - Login required decorator on protected pages

### 2. **Contact Management**
   - Accept contact inquiries via form submission
   - Store contact data in database
   - Display all contacts in contact page view
   - Data accessible through Django admin

### 3. **Static Resources**
   - Custom CSS styling for all pages
   - Static images directory for media content
   - JavaScript for client-side functionality

### 4. **Django Admin**
   - Manage users and permissions
   - View and edit contact inquiries
   - Database administration

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- Django 5.2.12
- pip (Python package manager)

### Installation

1. **Clone/Access the Project**
   ```bash
   cd c:\Users\ayush\Desktop\BBDCSE3D\BBDCSE3D\CSE3D
   ```

2. **Create Virtual Environment** (optional but recommended)
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   ```

3. **Install Dependencies**
   ```bash
   pip install django==5.2.12
   ```

4. **Run Migrations** (if needed)
   ```bash
   python manage.py migrate
   ```

5. **Create Superuser** (for admin access)
   ```bash
   python manage.py createsuperuser
   ```

6. **Run Development Server**
   ```bash
   python manage.py runserver
   ```

7. **Access Application**
   - App: http://localhost:8000
   - Admin: http://localhost:8000/admin

---

## 👤 Git Configuration

Current git identity is configured:
- **Email:** ayushsingh638684@gmail.com
- **Configuration Level:** Global (applies to all repositories)

---

## 📝 Development Notes

- **DEBUG Mode:** Currently enabled (change in `settings.py` for production)
- **Secret Key:** Change before deploying to production
- **ALLOWED_HOSTS:** Configure for production deployment
- **Static Files:** Run `python manage.py collectstatic` before deployment

---

## 🔄 Future Enhancements

- [ ] Add email notifications for contact submissions
- [ ] Implement user profile management
- [ ] Add product/service listings
- [ ] Implement shopping cart functionality
- [ ] Add payment integration
- [ ] Improve form validation and error handling
- [ ] Deploy to production (configure ALLOWED_HOSTS, SECRET_KEY, DEBUG)

---

## 📞 Support

For issues or questions, refer to:
- [Django Documentation](https://docs.djangoproject.com/)
- [Django Admin Guide](https://docs.djangoproject.com/en/5.2/ref/contrib/admin/)
- Project maintainer contact information

---

**Last Updated:** March 24, 2026
