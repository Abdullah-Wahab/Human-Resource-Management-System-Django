# Human Resource Management System (HRMS) - Django

A comprehensive Django-based Human Resource Management System designed to streamline employee management, attendance tracking, leave requests, payroll, recruitment, and departmental operations.

## Features

- **User Management**: Custom user model with profile images
- **Employee Management**: Complete employee profiles including personal details, contact information, bank details, and salary
- **Department Management**: Create and manage departments with history tracking
- **Attendance Tracking**: Record employee attendance with check-in/check-out times and status
- **Leave Management**: Handle employee leave requests with approval workflow
- **Payroll System**: Basic payroll information storage
- **Recruitment Module**: Manage job applications and CV uploads
- **Next of Kin Records**: Store emergency contact information for employees
- **Admin Dashboard**: Django admin interface for system administration
- **Responsive UI**: Bootstrap-based templates for a clean, responsive interface

## Technologies Used

- **Backend**: Django 4.1+
- **Database**: SQLite (default), configurable for PostgreSQL/MySQL
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Image Handling**: Pillow for image uploads

## Installation

### Prerequisites

- Python 3.8+
- pip (Python package installer)

### Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Abdullah-Wahab/Human-Resource-Management-System-Django.git
   cd Human-Resource-Management-System-Django
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install django pillow
   ```

4. **Navigate to the project directory:**
   ```bash
   cd project
   ```

5. **Run migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a superuser:**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

8. **Access the application:**
   - Main application: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## Usage

### Admin Panel

Access the Django admin panel to manage:
- Users and permissions
- Departments
- Employees
- Attendance records
- Leave requests
- Recruitment applications

### Employee Features

- View personal profile
- Submit leave requests
- Check attendance history
- Update next of kin information

### Recruitment

- Submit job applications with CV upload
- Admin review of applications

## Project Structure

```
project/
├── manage.py
├── hrms/
│   ├── models.py          # Database models
│   ├── views.py           # View functions
│   ├── urls.py            # URL routing
│   ├── forms.py           # Django forms
│   ├── admin.py           # Admin configurations
│   ├── templates/         # HTML templates
│   ├── static/            # CSS, JS, images
│   └── migrations/        # Database migrations
├── project/
│   ├── settings.py        # Django settings
│   ├── urls.py            # Main URL configuration
│   ├── wsgi.py            # WSGI configuration
│   └── asgi.py            # ASGI configuration
└── media/                 # Uploaded files
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
