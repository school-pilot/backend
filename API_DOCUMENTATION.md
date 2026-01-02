# SCHOOLPILOT SMS — Comprehensive API Documentation

**Base URL**: `http://localhost:8000/` (local) or your deployed domain

## Table of Contents
1. [Authentication](#authentication)
2. [Accounts Module](#accounts-module)
3. [Schools Module](#schools-module)
4. [Sessions & Terms Module](#sessions--terms-module)
5. [Students Module](#students-module)
6. [Teachers/Staff Module](#teachersstaff-module)
7. [Academics Module](#academics-module)
7. [Attendance Module](#attendance-module)
8. [Results Module](#results-module)
9. [Fees Module](#fees-module)
10. [Communications Module](#communications-module)
11. [Timetable Module](#timetable-module)
12. [Reports Module](#reports-module)
13. [Subscriptions Module](#subscriptions-module)
14. [Audit Module](#audit-module)

---

## Authentication

All endpoints except registration and token endpoints require JWT authentication.

### Obtain JWT Token
- **Endpoint**: `POST /api/accounts/token/`
- **Auth**: Public (no token required)
- **Body**:
  ```json
  {
    "email": "user@example.com",
    "password": "password123"
  }
  ```
- **Response** (200 OK):
  ```json
  {
    "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
  }
  ```

### Refresh Access Token
- **Endpoint**: `POST /api/accounts/token/refresh/`
- **Auth**: Public
- **Body**:
  ```json
  {
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
  }
  ```
- **Response** (200 OK):
  ```json
  {
    "access": "eyJ0eXAiOiJKV1QiLCJhbGc..."
  }
  ```

### Using JWT in Requests
Include the token in the Authorization header:
```
Authorization: Bearer <access_token>
```

---

## Accounts Module

### Register User
- **Endpoint**: `POST /api/accounts/register/`
- **Auth**: Public
- **Body**:
  ```json
  {
    "first_name": "John",
    "last_name": "Doe",
    "email": "john@example.com",
    "username": "johndoe",
    "role": "teacher",
    "school": "Springfield High",
    "password1": "SecurePass123!",
    "password2": "SecurePass123!"
  }
  ```
- **Response** (201 Created): User object

### List Users
- **Endpoint**: `GET /api/accounts/users/`
- **Auth**: Required (IsAuthenticated)
- **Response** (200 OK): List of user objects

### Get User Details
- **Endpoint**: `GET /api/accounts/users/<user_id>/`
- **Auth**: Required
- **Response** (200 OK): User object

### Update User
- **Endpoint**: `PATCH /api/accounts/users/<user_id>/update/`
- **Auth**: Required
- **Body**: Fields to update (email, first_name, last_name, role, etc.)
- **Response** (200 OK): Updated user object

### Change Password
- **Endpoint**: `POST /api/accounts/users/change-password/`
- **Auth**: Required
- **Body**:
  ```json
  {
    "old_password": "CurrentPass123!",
    "new_password": "NewPass456!",
    "confirm_new_password": "NewPass456!"
  }
  ```
- **Response** (200 OK): Success message

---

## Schools Module

### Create School
- **Endpoint**: `POST /api/schools/add/`
- **Auth**: Required
- **Permissions**: super_admin only
- **Body**: School details (name, address, phone, etc.)
- **Response** (201 Created): School object

### Get School Details
- **Endpoint**: `GET /api/schools/view/<school_id>/`
- **Auth**: Required
- **Permissions**: super_admin only
- **Response** (200 OK): School object

### Update School
- **Endpoint**: `PATCH /api/schools/update/<school_id>/`
- **Auth**: Required
- **Permissions**: super_admin only
- **Body**: Fields to update
- **Response** (200 OK): Updated school object

---

## Sessions & Terms Module

### Create Academic Session
- **Endpoint**: `POST /api/schools/session/create/`
- **Auth**: Required
- **Permissions**: school_admin or super_admin only
- **Body**:
  ```json
  {
    "school": 1,
    "name": "2025/2026",
    "start_date": "2025-09-01",
    "end_date": "2026-07-31",
    "is_current": true
  }
  ```
- **Response** (201 Created): Session object

### View Academic Sessions
- **Endpoint**: `GET /api/schools/session/view/<school_id>/`
- **Auth**: Required
- **Permissions**: school_admin or super_admin only
- **Response** (200 OK): List of academic sessions for the school

### Update Academic Session
- **Endpoint**: `PUT/PATCH /api/schools/session/update/<session_id>/`
- **Auth**: Required
- **Permissions**: school_admin or super_admin only
- **Body**: Fields to update (name, start_date, end_date, is_current, etc.)
- **Response** (200 OK): Updated session object

### Create Term
- **Endpoint**: `POST /api/schools/term/create/`
- **Auth**: Required
- **Permissions**: school_admin or super_admin only
- **Body**:
  ```json
  {
    "academic_session": 1,
    "school": 1,
    "name": "First Term",
    "start_date": "2025-09-01",
    "end_date": "2025-12-15",
    "is_current": true
  }
  ```
- **Response** (201 Created): Term object

### View Terms
- **Endpoint**: `GET /api/schools/term/view/<school_id>/`
- **Auth**: Required
- **Permissions**: school_admin or super_admin only
- **Response** (200 OK): List of all terms for the school

### Update Term
- **Endpoint**: `PUT/PATCH /api/schools/term/update/<term_id>/`
- **Auth**: Required
- **Permissions**: school_admin or super_admin only
- **Body**: Fields to update (name, start_date, end_date, is_current, etc.)
- **Response** (200 OK): Updated term object

### Get Current Term
- **Endpoint**: `GET /api/schools/term/current/<school_id>/`
- **Auth**: Required
- **Response** (200 OK): Current active term object
- **Response** (404 Not Found): If no current term is set

---

## Students Module

### List/Create Students
- **Endpoint**: `GET/POST /api/students/`
- **Auth**: Required
- **GET Response** (200 OK): List of students
- **POST Body**: Student details (enrollment_number, first_name, last_name, class, etc.)
- **POST Response** (201 Created): Created student object

### Get/Update/Delete Student
- **Endpoint**: `GET/PATCH/DELETE /api/students/<student_id>/`
- **Auth**: Required
- **GET Response** (200 OK): Student object
- **PATCH Body**: Fields to update
- **PATCH Response** (200 OK): Updated student object
- **DELETE Response** (204 No Content)

### Promote Student
- **Endpoint**: `POST /api/students/<student_id>/promote/`
- **Auth**: Required
- **Permissions**: admin only
- **Response** (200 OK): Success message with new class

### Get Student Profile
- **Endpoint**: `GET /api/students/<student_id>/profile/`
- **Auth**: Required
- **Response** (200 OK): Student profile with guardian information

### Bulk Upload Students
- **Endpoint**: `POST /api/students/bulk-upload/`
- **Auth**: Required
- **Permissions**: admin only
- **Body**: CSV file multipart upload
- **Response** (200 OK): Upload status with success/error count

---

## Teachers/Staff Module

### List/Create Teachers
- **Endpoint**: `GET/POST /api/teachers/`
- **Auth**: Required
- **GET Response** (200 OK): List of teachers
- **POST Body**: Teacher details (staff_id, first_name, last_name, subject, etc.)
- **POST Response** (201 Created): Created teacher object

### Get/Update Teacher
- **Endpoint**: `GET/PATCH /api/teachers/<teacher_id>/`
- **Auth**: Required
- **GET Response** (200 OK): Teacher object
- **PATCH Body**: Fields to update
- **PATCH Response** (200 OK): Updated teacher object

### Assign Subjects to Teacher
- **Endpoint**: `POST /api/teachers/<teacher_id>/assign-subjects/`
- **Auth**: Required
- **Permissions**: admin only
- **Body**:
  ```json
  {
    "subjects": [1, 2, 3]
  }
  ```
- **Response** (200 OK): Success message

### Get Teacher's Classes
- **Endpoint**: `GET /api/teachers/<teacher_id>/classes/`
- **Auth**: Required
- **Response** (200 OK): List of classes assigned to teacher

---

## Academics Module

### List Classes
- **Endpoint**: `GET /api/academics/classes/`
- **Auth**: Required
- **Response** (200 OK): List of classes

### Create Class Arm/Section
- **Endpoint**: `POST /api/academics/arms/`
- **Auth**: Required
- **Permissions**: admin only
- **Body**: Arm details (class_name, arm_name, etc.)
- **Response** (201 Created): Created arm object

### List Subjects
- **Endpoint**: `GET /api/academics/subjects/`
- **Auth**: Required
- **Response** (200 OK): List of subjects

### Assign Subjects to Class
- **Endpoint**: `POST /api/academics/subjects/assign/`
- **Auth**: Required
- **Permissions**: admin only
- **Body**:
  ```json
  {
    "class_id": 1,
    "subjects": [1, 2, 3]
  }
  ```
- **Response** (201 Created): Success message

---

## Attendance Module

### Mark Attendance
- **Endpoint**: `POST /api/attendance/mark/`
- **Auth**: Required
- **Permissions**: teacher only
- **Body**:
  ```json
  {
    "class_id": 1,
    "date": "2025-01-02",
    "students": [
      {"student_id": 1, "status": "present"},
      {"student_id": 2, "status": "absent"}
    ]
  }
  ```
- **Response** (201 Created): Attendance records created

### Update Attendance
- **Endpoint**: `PATCH /api/attendance/<attendance_id>/`
- **Auth**: Required
- **Permissions**: teacher only
- **Body**: Updated attendance status
- **Response** (200 OK): Updated record

### View Attendance
- **Endpoint**: `GET /api/attendance/`
- **Auth**: Required
- **Response** (200 OK): List of attendance records

### Get Attendance Summary
- **Endpoint**: `GET /api/attendance/summary/`
- **Auth**: Required
- **Permissions**: admin only
- **Response** (200 OK): Attendance summary report

---

## Results Module

### List Assessments
- **Endpoint**: `GET /api/results/assessments/`
- **Auth**: Required
- **Response** (200 OK): List of assessments

### Enter Scores
- **Endpoint**: `POST /api/results/scores/`
- **Auth**: Required
- **Permissions**: teacher only
- **Body**:
  ```json
  {
    "assessment_id": 1,
    "class_id": 1,
    "scores": [
      {"student_id": 1, "score": 85},
      {"student_id": 2, "score": 92}
    ]
  }
  ```
- **Response** (201 Created): Scores created

### Update Score
- **Endpoint**: `PATCH /api/results/scores/<score_id>/`
- **Auth**: Required
- **Permissions**: teacher only
- **Body**: Updated score value
- **Response** (200 OK): Updated score

### Get Class Results
- **Endpoint**: `GET /api/results/class/`
- **Auth**: Required
- **Query Params**: class_id, assessment_id
- **Response** (200 OK): Class results

### Approve Class Results
- **Endpoint**: `POST /api/results/approve/`
- **Auth**: Required
- **Permissions**: admin only
- **Body**:
  ```json
  {
    "class_id": 1,
    "assessment_id": 1
  }
  ```
- **Response** (200 OK): Success message

### Get Student Results
- **Endpoint**: `GET /api/results/student/<student_id>/`
- **Auth**: Required
- **Response** (200 OK): Student's result records

---

## Fees Module

### Create Fee Category
- **Endpoint**: `POST /api/fees/categories/`
- **Auth**: Required
- **Permissions**: admin only
- **Body**:
  ```json
  {
    "name": "Tuition",
    "description": "Monthly tuition fee"
  }
  ```
- **Response** (201 Created): Category object

### Assign Fees to Class
- **Endpoint**: `POST /api/fees/structures/`
- **Auth**: Required
- **Permissions**: admin only
- **Body**:
  ```json
  {
    "class_id": 1,
    "category_id": 1,
    "amount": 5000
  }
  ```
- **Response** (201 Created): Fee structure object

### List Invoices
- **Endpoint**: `GET /api/fees/invoices/`
- **Auth**: Required
- **Permissions**: admin only
- **Response** (200 OK): List of invoices

### Get Invoice Details
- **Endpoint**: `GET /api/fees/invoices/<invoice_id>/`
- **Auth**: Required
- **Permissions**: admin only
- **Response** (200 OK): Invoice object

### Record Payment
- **Endpoint**: `POST /api/fees/payments/`
- **Auth**: Required
- **Permissions**: admin only
- **Body**:
  ```json
  {
    "invoice_id": 1,
    "amount_paid": 5000,
    "payment_method": "bank_transfer"
  }
  ```
- **Response** (201 Created): Payment record

### Get Payment History
- **Endpoint**: `GET /api/fees/payments/history/`
- **Auth**: Required
- **Permissions**: admin only
- **Response** (200 OK): Payment history

---

## Communications Module

### List/Create Announcements
- **Endpoint**: `GET/POST /api/communications/announcements/`
- **Auth**: Required for GET; admin required for POST
- **GET Response** (200 OK): List of announcements
- **POST Body**: Announcement content (title, message, target_audience, etc.)
- **POST Response** (201 Created): Created announcement

### Get Notifications
- **Endpoint**: `GET /api/communications/notifications/`
- **Auth**: Required
- **Response** (200 OK): User's notifications

### Mark Notification as Read
- **Endpoint**: `PATCH /api/communications/notifications/<notification_id>/read/`
- **Auth**: Required
- **Response** (200 OK): Updated notification

---

## Timetable Module

### Create Timetable
- **Endpoint**: `POST /api/timetable/`
- **Auth**: Required
- **Permissions**: admin only
- **Body**: Timetable details (class_id, day, period, subject, teacher, etc.)
- **Response** (201 Created): Timetable entry

### Get Class Timetable
- **Endpoint**: `GET /api/timetable/class/<class_id>/`
- **Auth**: Required
- **Response** (200 OK): Class schedule

### Get Teacher Timetable
- **Endpoint**: `GET /api/timetable/teacher/<teacher_id>/`
- **Auth**: Required
- **Permissions**: teacher only
- **Response** (200 OK): Teacher's schedule

---

## Reports Module

### Get Attendance Report
- **Endpoint**: `GET /api/reports/attendance/`
- **Auth**: Required
- **Permissions**: admin only
- **Query Params**: class_id, date_from, date_to (optional)
- **Response** (200 OK): Attendance report

### Get Fees Report
- **Endpoint**: `GET /api/reports/fees/`
- **Auth**: Required
- **Permissions**: admin only
- **Query Params**: class_id, month, year (optional)
- **Response** (200 OK): Fees collection report

### Get Academics Report
- **Endpoint**: `GET /api/reports/academics/`
- **Auth**: Required
- **Permissions**: admin only
- **Query Params**: class_id, term, year (optional)
- **Response** (200 OK): Academic performance report

---

## Subscriptions Module

### Get Subscription Plans
- **Endpoint**: `GET /api/subscriptions/plans/`
- **Auth**: Required
- **Response** (200 OK):
  ```json
  {
    "plans": [
      {"id": 1, "name": "Basic", "price": 100, "features": ["Students", "Teachers"]},
      {"id": 2, "name": "Pro", "price": 250, "features": ["Students", "Teachers", "Results", "Attendance"]},
      {"id": 3, "name": "Enterprise", "price": 500, "features": ["All"]}
    ]
  }
  ```

### Get Current Subscription
- **Endpoint**: `GET /api/subscriptions/current/`
- **Auth**: Required
- **Permissions**: school_admin only
- **Response** (200 OK): Current subscription details

### Upgrade Subscription
- **Endpoint**: `POST /api/subscriptions/upgrade/`
- **Auth**: Required
- **Permissions**: school_admin only
- **Body**:
  ```json
  {
    "plan_id": 2
  }
  ```
- **Response** (200 OK): Success message

---

## Audit Module

### Get Audit Logs
- **Endpoint**: `GET /api/audit/logs/`
- **Auth**: Required
- **Permissions**: super_admin only
- **Query Params**: user_id, action, date_from, date_to (optional)
- **Response** (200 OK): System audit logs

---

## Response Codes

- **200 OK**: Successful GET, PATCH request
- **201 Created**: Successful POST request
- **204 No Content**: Successful DELETE request
- **400 Bad Request**: Invalid request body or parameters
- **403 Forbidden**: User lacks required permissions
- **404 Not Found**: Resource not found
- **500 Internal Server Error**: Server error

## User Roles

- **super_admin**: Full system access, manage schools and administrators
- **school_admin**: School-level administration, manage staff and students
- **admin**: School administrator with broad access
- **teacher**: Teaching staff with access to classes, attendance, results
- **student**: Student access to own profile and academic records
- **parent**: Parent/guardian access to student records

---

## Example Workflow

1. Register or obtain JWT token
2. Use token in Authorization header for subsequent requests
3. Call appropriate endpoints based on user role
4. Handle responses with appropriate error handling

For interactive API documentation, visit `/api-docs/` endpoint.
