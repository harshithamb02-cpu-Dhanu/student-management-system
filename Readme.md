# 🎓 Student Management System

A full-stack **Student Management System** built using **Django**, **Django REST Framework**, and **JWT Authentication**. The application provides secure APIs for managing students, faculty, courses, attendance, dashboard statistics, audit logs, CSV import, and Excel/PDF export.

---

## 🚀 Features

- JWT Authentication (Register, Login, Refresh, Logout)
- Student Management (CRUD)
- Faculty Management (CRUD)
- Course Management (CRUD)
- Attendance Management
- Dashboard Statistics API
- Student Search
- Student Filtering
- CSV Bulk Import
- Excel Export
- PDF Export
- Audit Logging
- Serializer Validation
- PostgreSQL Database
- RESTful APIs

---

# 🛠 Tech Stack

### Backend

- Python
- Django
- Django REST Framework
- Simple JWT
- PostgreSQL

### Libraries

- django-filter
- pandas
- openpyxl
- reportlab
- pillow
- python-dotenv
- psycopg2-binary

---

# 📁 Project Structure

```
student_management/

│── accounts/
│── students/
│── faculty/
│── courses/
│── attendance/
│── dashboard/
│── auditlog/

│── student_management/
│── manage.py
│── requirements.txt
│── README.md
```

---

# ⚙ Installation

## Clone Repository

```bash
git clone https://github.com/your-username/student-management-system.git

cd student-management-system
```

---

## Create Virtual Environment

Windows

```bash
python -m venv venv

venv\Scripts\activate
```

Linux / Mac

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip install django
pip install djangorestframework
pip install djangorestframework-simplejwt
pip install psycopg2-binary
pip install django-filter
pip install pandas
pip install openpyxl
pip install reportlab
pip install pillow
pip install python-dotenv
```

---

# 🗄 Database Setup

Create PostgreSQL database.

Update **settings.py**

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "student_management",
        "USER": "postgres",
        "PASSWORD": "your_password",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
```

---

Run migrations

```bash
python manage.py makemigrations

python manage.py migrate
```

Create Super User

```bash
python manage.py createsuperuser
```

Run server

```bash
python manage.py runserver
```

---

# 🔐 Authentication APIs

| Method | Endpoint |
|---------|----------|
| POST | /api/register/ |
| POST | /api/login/ |
| POST | /api/token/refresh/ |
| POST | /api/logout/ |

Login returns

- Access Token
- Refresh Token

---

# 👨‍🎓 Student APIs

| Method | Endpoint |
|---------|----------|
| GET | /api/students/ |
| GET | /api/students/{id}/ |
| POST | /api/students/ |
| PUT | /api/students/{id}/ |
| DELETE | /api/students/{id}/ |

---

# 👨‍🏫 Faculty APIs

| Method | Endpoint |
|---------|----------|
| GET | /api/faculty/ |
| POST | /api/faculty/ |
| PUT | /api/faculty/{id}/ |
| DELETE | /api/faculty/{id}/ |

---

# 📚 Course APIs

| Method | Endpoint |
|---------|----------|
| GET | /api/courses/ |
| POST | /api/courses/ |
| PUT | /api/courses/{id}/ |
| DELETE | /api/courses/{id}/ |

Faculty can be assigned to multiple courses.

---

# 📅 Attendance APIs

| Method | Endpoint |
|---------|----------|
| GET | /api/attendance/ |
| POST | /api/attendance/ |
| PUT | /api/attendance/{id}/ |
| DELETE | /api/attendance/{id}/ |

Attendance Status

- Present
- Absent
- Leave

---

# 📊 Dashboard API

```
GET /api/dashboard/
```

Returns

- Total Students
- Total Faculty
- Total Courses
- Today's Attendance
- Recent Students

---

# 🔍 Search API

Search students by

- Name
- Email
- Phone

Example

```
GET /api/students/?search=Harshitha
```

---

# 🎯 Filter API

Filter students by Course

```
GET /api/students/?course=Python
```

Filter students by Faculty

```
GET /api/students/?faculty=John
```

Filter students by Gender

```
GET /api/students/?gender=Female
```

---

# ✅ Validation

Backend validation is implemented using Django REST Framework Serializers.

Includes

- Required Fields
- Email Validation
- Phone Validation
- Password Validation

---

# 📝 Audit Logs

Audit logs are automatically created for

- Student Created
- Student Updated
- Student Deleted

Each log stores

- User
- Action
- Table Name
- Record ID
- Timestamp

---

# 📥 Bulk Student Import

Upload CSV file

Example

```csv
Name,Email,Phone

Harshitha,harshitha@gmail.com,9876543210

Rahul,rahul@gmail.com,9988776655
```

API

```
POST /api/students/import/
```

Uses

- pandas

---

# 📤 Export Excel

API

```
GET /api/export/excel/
```

Uses

- openpyxl

---

# 📄 Export PDF

API

```
GET /api/export/pdf/
```

Uses

- reportlab

---

# 🗃 Database Models

## Student

- student_name
- email
- phone
- gender
- dob
- address
- course
- created_at
- updated_at

---

## Faculty

- faculty_name
- email
- phone
- department
- experience

---

## Course

- course_name
- duration
- fees
- faculty

---

## Attendance

- student
- date
- status

---

## Audit Log

- user
- action
- table_name
- record_id
- created_at

---

# 🔒 Authentication

Protected APIs require JWT Access Token.

Example

```
Authorization: Bearer <access_token>
```

---

# 📌 Future Improvements

- React Frontend
- Role-Based Access Control
- Swagger/OpenAPI Documentation
- Pagination
- Docker Support
- AWS Deployment
- Email Notifications
- Unit Testing
- CI/CD Pipeline

---

# 👩‍💻 Author

**Harshitha MB**

Python Backend Developer

GitHub: https://github.com/your-username

LinkedIn: https://linkedin.com/in/your-profile

---

