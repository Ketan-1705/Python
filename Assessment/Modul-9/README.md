# WriteSphere Blogging Platform

A premium blogging platform built for **WriteHub Community** using Django and MySQL.

## 🚀 Deployment Readiness Checklist

### 1. Local Environment Setup
- **Virtual Environment**: Use the provided `venv` folder.
- **Dependencies**: Run `pip install -r requirements.txt`.
- **Database**: Ensure MySQL is running and update the `.env` file credentials.

### 2. PythonAnywhere Deployment
Follow these steps to host **WriteSphere** live:

1.  **Clone on PythonAnywhere**:
    - Push your current project to **GitHub**.
    - Open a Bash console on PythonAnywhere and run `git clone <your-repo-url>`.
2.  **Setup Virtualenv**:
    - `mkvirtualenv writesphere --python=python3.10`
    - `pip install -r requirements.txt`
3.  **Database Configuration**:
    - Go to the **Databases** tab on PythonAnywhere.
    - Create a **MySQL** database.
    - Update the `.env` file on PythonAnywhere with the provided host, username, and password.
4.  **Web App Setup**:
    - Create a new web app using **Manual Configuration**.
    - Set the **Virtualenv** path to `/home/<username>/.virtualenvs/writesphere`.
    - Configure the **WSGI file** to point to your project's settings.
5.  **Static & Media**:
    - Configure static and media paths in the **Web** tab.
    - Run `python manage.py collectstatic`.

## 🛠️ Tech Stack
- **Backend**: Django 5.x
- **Frontend**: Bootstrap 5 + Glassmorphism CSS
- **Database**: MySQL
- **Editor**: django-ckeditor
- **MVT Architecture**: Clean separation of Models, Views, and Templates.

## 👤 Role-Based Access
- **Admin**: Full access.
- **Author**: Create/Edit own stories.
- **Reader**: Interaction (Likes, Comments, Following).
