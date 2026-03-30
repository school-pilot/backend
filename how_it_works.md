# How It Works

## Project Overview

This project is a Django-based school management backend built on:
- Django 4.2
- Django REST Framework (DRF)
- DRF Spectacular for API schema generation
- Simple JWT for authentication
- SQLite by default for local development

The root Django project is `config`, and the main application packages are:
- `accounts`
- `schools`
- `students`
- `staffs`
- `academics`
- `attendance`
- `results`
- `fees`
- `communications`
- `timetable`
- `reports`
- `subscriptions`
- `audit`

## Core Architecture

### Request flow
1. Client sends an HTTP request to the server.
2. `config.urls` routes the request to the correct app based on the URL prefix.
3. The app's view function processes the request.
4. Views interact with Django models and serializers to read or write data.
5. Responses are returned as JSON, except for admin pages and static documentation templates.

### Authentication

The project uses JWT authentication from `rest_framework_simplejwt`.
- `POST /api/accounts/token/` issues an access and refresh token.
- `POST /api/accounts/token/refresh/` exchanges a refresh token for a new access token.
- Protected endpoints require `Authorization: Bearer <access_token>`.

Only the registration endpoint and JWT token endpoints are public.
All other API endpoints require authentication.

### Settings and configuration

Key configuration is defined in `config/settings/base.py`:
- `AUTH_USER_MODEL = 'accounts.User'`
- `INSTALLED_APPS` includes Django apps, DRF, `drf_spectacular`, `rest_framework_simplejwt`, and each project module.
- `DATABASES` defaults to SQLite using `db.sqlite3`.
- Static files are configured with `whitenoise` support.

## Data Model Schema

### `accounts.User`

Custom user model extending `AbstractUser` with:
- `email` (unique)
- `username` (unique)
- `role` (`super_admin`, `school_admin`, `teacher`, `student`, `parent`)
- `school` (text field)
- `is_active`
- `is_staff`
- `last_login`
- `date_joined`

### `schools.School`

Represents a school and includes:
- `name`
- `logo`
- `address`
- `phone`
- `email`
- `registration_number`
- `motto`
- `is_active`
- `created_at`, `updated_at`

### `schools.SchoolSettings`

Contains optional settings for each school:
- `grading_system_type`
- `max_score`
- `min_passing_score`
- `attendance_required_percentage`
- `allow_result_download`
- `allow_parent_access`

### `schools.AcademicSession`

Academic session model:
- `school`
- `name`
- `start_date`
- `end_date`
- `is_current`
- `created_at`, `updated_at`

### `schools.Term`

Term model linked to a session:
- `school`
- `academic_session`
- `name`
- `start_date`
- `end_date`
- `is_current`
- `created_at`, `updated_at`

### `students.Student`

Student record linked to a user:
- `user`
- `school`
- `admission_number`
- `admission_date`
- `current_class`
- `status` (`active`, `graduated`, `suspended`)
- `created_at`, `updated_at`

### `students.StudentProfile`

Optional student personal details:
- `student`
- `date_of_birth`
- `gender`
- `blood_group`
- `address`
- `guardian`

### `students.Guardian`

Guardian details for a student:
- `student`
- `name`
- `relationship`
- `contact_number`
- `email`
- `address`

## API Modules and Endpoint Schema

### Accounts
Base path: `/api/accounts/`
- `POST register/` — register a new user
- `POST token/` — obtain JWT tokens
- `POST token/refresh/` — refresh access token
- `GET users/` — list users
- `GET users/<user_id>/` — get a single user
- `PATCH users/<user_id>/update/` — update a user
- `POST users/change-password/` — change current user's password

### Schools
Base path: `/api/schools/`
- `POST add/` — create a school
- `GET view/<school_id>/` — view a school
- `PATCH update/<school_id>/` — update a school
- `GET view-all/` — list all schools
- `POST session/create/` — create an academic session
- `GET session/view/<school_id>/` — list sessions for a school
- `PATCH session/update/<session_id>/` — update a session
- `POST term/create/` — create a term
- `GET term/view/<school_id>/` — list terms for a school
- `PATCH term/update/<term_id>/` — update a term
- `GET term/current/<school_id>/` — get current term for a school

### Students
Base path: `/api/students/`
- `GET /` — list students
- `GET /<student_id>/` — get student details
- `POST bulk-upload/` — bulk upload student records
- `GET /<student_id>/profile/` — view student profile
- `POST /<student_id>/promote/` — promote a student

### Teachers / Staff
Base path: `/api/teachers/`
- `GET /` — list teachers
- `GET /<teacher_id>/` — get teacher details
- `POST /<teacher_id>/assign-subjects/` — assign subjects to a teacher
- `GET /<teacher_id>/classes/` — get classes assigned to a teacher

### Academics
Base path: `/api/academics/`
- `GET classes/` — list classes
- `POST arms/` — create a class arm
- `GET subjects/` — list subjects
- `POST subjects/assign/` — assign a subject to a class or teacher

### Attendance
Base path: `/api/attendance/`
- `POST mark/` — mark attendance
- `GET /` — view attendance records
- `GET summary/` — attendance summary
- `PATCH /<attendance_id>/` — update an attendance record

### Results
Base path: `/api/results/`
- `GET assessments/` — list assessments
- `POST scores/` — enter scores
- `PATCH scores/<score_id>/` — update a score
- `GET class/` — get class results
- `POST approve/` — approve results
- `GET student/<student_id>/` — get results for a student

### Fees
Base path: `/api/fees/`
- `POST categories/` — create a fee category
- `POST structures/` — assign fee structures
- `GET invoices/` — list invoices
- `GET invoices/<invoice_id>/` — invoice detail
- `POST payments/` — record a payment
- `GET payments/history/` — payment history

### Communications
Base path: `/api/communications/`
- `GET announcements/` — list announcements
- `POST announcements/create/` — create an announcement
- `PATCH announcements/<announcement_id>/update/` — update an announcement
- `GET notifications/` — list notifications
- `POST notifications/create/` — create a notification
- `PATCH notifications/<notification_id>/update/` — update a notification
- `POST notifications/<notification_id>/read/` — mark notification read

### Timetable
Base path: `/api/timetable/`
- `POST /` — create a timetable
- `GET class/<class_id>/` — view a class timetable
- `GET teacher/<teacher_id>/` — view a teacher timetable

### Reports
Base path: `/api/reports/`
- `GET attendance/` — attendance report
- `GET fees/` — fees report
- `GET academics/` — academics report

### Subscriptions
Base path: `/api/subscriptions/`
- `GET plans/` — list subscription plans
- `GET current/` — current subscription details
- `POST upgrade/` — upgrade subscription

### Audit
Base path: `/api/audit/`
- `GET logs/` — audit logs

## API Documentation

The project exposes API documentation and schema endpoints:
- `GET /api/schema/` — OpenAPI schema JSON
- `GET /` — Swagger UI
- `GET /api-docs-redoc/` — Redoc UI
- `GET /api-docs-static/` — static API docs page
- `GET /api-docs-fields/` — field-level API docs page

## Deployment and Run

The project entrypoint is `manage.py`.
- Run locally with `python manage.py runserver`.
- Use environment variables to configure `SECRET_KEY`, `DEBUG`, and Supabase settings.

## Admin and Templates

- Admin interface: `/admin-site/`
- Template-based docs pages are served from the `templates/` directory.

## Summary

This backend is a modular school management API that uses Django + DRF with JWT authentication and a custom user model. Each module exposes a dedicated REST namespace under `/api/`, and the data schema is anchored on schools, academic sessions, terms, students, users, and supporting modules for attendance, results, fees, communications, timetables, reports, subscriptions, and audit.
