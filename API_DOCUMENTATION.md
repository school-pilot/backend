# SCHOOLPILOT SMS — Complete API Documentation with Required Fields

**Base URL**: `http://localhost:8000/` (local) or your deployed domain

## Table of Contents
1. [Authentication](#authentication)
2. [Accounts Module](#accounts-module)
3. [Schools Module](#schools-module)
4. [Sessions & Terms Module](#sessions--terms-module)
5. [Students Module](#students-module)
6. [Teachers/Staff Module](#teachersstaff-module)
7. [Academics Module](#academics-module)
8. [Attendance Module](#attendance-module)
9. [Results Module](#results-module)
10. [Fees Module](#fees-module)
11. [Communications Module](#communications-module)
12. [Timetable Module](#timetable-module)
13. [Reports Module](#reports-module)
14. [Subscriptions Module](#subscriptions-module)
15. [Audit Module](#audit-module)

---

## Authentication

All endpoints except registration and token endpoints require JWT authentication.

### Obtain JWT Token
- **Endpoint**: `POST /api/accounts/token/`
- **Auth**: Public (no token required)
- **Required Fields**: `email`, `password`
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
- **Required Fields**: `refresh`
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
- **Required Fields**: `first_name`, `last_name`, `email`, `username`, `password`
- **Optional Fields**: None
- **Body**:
  ```json
  {
    "first_name": "John",
    "last_name": "Doe",
    "email": "john@example.com",
    "username": "johndoe",
    "password": "SecurePass123!"
  }
  ```
- **Response** (201 Created):
  ```json
  {
    "first_name": "John",
    "last_name": "Doe",
    "email": "john@example.com",
    "username": "johndoe"
  }
  ```

### List Users
- **Endpoint**: `GET /api/accounts/users/`
- **Auth**: Required (IsAuthenticated)
- **Response** (200 OK): Array of user objects with all fields

### Get User Details
- **Endpoint**: `GET /api/accounts/users/<user_id>/`
- **Auth**: Required
- **Response** (200 OK):
  ```json
  {
    "id": 1,
    "first_name": "John",
    "last_name": "Doe",
    "email": "john@example.com",
    "username": "johndoe",
    "role": "teacher",
    "school": 1,
    "is_active": true,
    "is_staff": false,
    "date_joined": "2025-01-01T10:00:00Z",
    "last_login": "2025-01-13T15:30:00Z"
  }
  ```

### Update User
- **Endpoint**: `PATCH /api/accounts/users/<user_id>/update/`
- **Auth**: Required
- **Editable Fields**: `first_name`, `last_name`, `role`, `school`, `is_active`, `is_staff`, `email`, `username`
- **Read-only Fields**: None - all listed fields are editable
- **Body** (send only fields you want to update):
  ```json
  {
    "first_name": "Jane",
    "last_name": "Smith",
    "role": "admin",
    "school": 2,
    "is_active": true,
    "is_staff": true,
    "email": "jane@example.com",
    "username": "janesmith"
  }
  ```
- **Response** (200 OK): Updated user object

### Change Password
- **Endpoint**: `POST /api/accounts/users/change-password/`
- **Auth**: Required
- **Required Fields**: `old_password`, `new_password`, `confirm_new_password`
- **Validation**: 
  - `new_password` must equal `confirm_new_password`
  - `old_password` must be correct (will validate against current user's password)
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
- **Required Fields**: `name`, `logo`, `address`, `phone`, `email`, `registration_number`, `motto`
- **Optional Fields**: None - all fields are required
- **Body**:
  ```json
  {
    "name": "Springfield High School",
    "logo": "https://example.com/logo.png",
    "address": "123 Main Street",
    "phone": "555-1234",
    "email": "school@example.com",
    "registration_number": "REG123456",
    "motto": "Excellence in Education"
  }
  ```
- **Response** (201 Created): School object

### Get School Details
- **Endpoint**: `GET /api/schools/view/<school_id>/`
- **Auth**: Required
- **Permissions**: super_admin only
- **Response** (200 OK):
  ```json
  {
    "id": 1,
    "name": "Springfield High School",
    "logo": "https://example.com/logo.png",
    "address": "123 Main Street",
    "phone": "555-1234",
    "email": "school@example.com",
    "registration_number": "REG123456",
    "motto": "Excellence in Education",
    "is_active": true,
    "created_at": "2025-01-01T10:00:00Z",
    "updated_at": "2025-01-13T15:30:00Z"
  }
  ```

### Update School
- **Endpoint**: `PATCH /api/schools/update/<school_id>/`
- **Auth**: Required
- **Permissions**: super_admin only
- **Editable Fields**: `name`, `logo`, `address`, `phone`, `email`, `registration_number`, `motto`
- **Read-only Fields**: `is_active`, `created_at`, `updated_at`
- **Body** (send only fields you want to update):
  ```json
  {
    "name": "Springfield High School",
    "logo": "https://example.com/logo.png",
    "address": "456 Oak Avenue",
    "phone": "555-5678",
    "email": "newemail@school.com",
    "registration_number": "REG123456",
    "motto": "Excellence in Education"
  }
  ```
- **Response** (200 OK): Updated school object

---

## Sessions & Terms Module

### Create Academic Session
- **Endpoint**: `POST /api/schools/session/create/`
- **Auth**: Required
- **Permissions**: school_admin or super_admin only
- **Required Fields**: `school`, `name`, `start_date`, `end_date`, `is_current`
- **Optional Fields**: None - all fields are required
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
- **Response** (200 OK):
  ```json
  [
    {
      "id": 1,
      "school": {
        "id": 1,
        "name": "Springfield High School",
        "logo": "https://example.com/logo.png"
      },
      "name": "2025/2026",
      "start_date": "2025-09-01",
      "end_date": "2026-07-31",
      "is_current": true,
      "created_at": "2025-01-01T10:00:00Z",
      "updated_at": "2025-01-13T15:30:00Z"
    }
  ]
  ```

### Update Academic Session
- **Endpoint**: `PUT/PATCH /api/schools/session/update/<session_id>/`
- **Auth**: Required
- **Permissions**: school_admin or super_admin only
- **Editable Fields**: `school`, `name`, `start_date`, `end_date`, `is_current`
- **Read-only Fields**: `created_at`, `updated_at`
- **Body** (send only fields you want to update):
  ```json
  {
    "school": 1,
    "name": "2025/2026",
    "start_date": "2025-09-01",
    "end_date": "2026-07-31",
    "is_current": true
  }
  ```
- **Response** (200 OK): Updated session object

### Create Term
- **Endpoint**: `POST /api/schools/term/create/`
- **Auth**: Required
- **Permissions**: school_admin or super_admin only
- **Required Fields**: `school`, `academic_session`, `name`, `start_date`, `end_date`, `is_current`
- **Optional Fields**: None - all fields are required
- **Body**:
  ```json
  {
    "school": 1,
    "academic_session": 1,
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
- **Response** (200 OK): Array of term objects with nested school and session details

### Update Term
- **Endpoint**: `PUT/PATCH /api/schools/term/update/<term_id>/`
- **Auth**: Required
- **Permissions**: school_admin or super_admin only
- **Editable Fields**: `school`, `academic_session`, `name`, `start_date`, `end_date`, `is_current`
- **Read-only Fields**: `created_at`, `updated_at`
- **Body** (send only fields you want to update):
  ```json
  {
    "school": 1,
    "academic_session": 1,
    "name": "First Term",
    "start_date": "2025-09-01",
    "end_date": "2025-12-15",
    "is_current": true
  }
  ```
- **Response** (200 OK): Updated term object

### Get Current Term
- **Endpoint**: `GET /api/schools/term/current/<school_id>/`
- **Auth**: Required
- **Response** (200 OK):
  ```json
  {
    "id": 1,
    "name": "First Term"
  }
  ```
- **Response** (404 Not Found): If no current term is set

---

## Students Module

### List/Create Students
- **Endpoint**: `GET/POST /api/students/`
- **Auth**: Required
- **GET Response** (200 OK):
  ```json
  [
    {
      "id": 1,
      "user": 5,
      "user_name": "John Doe",
      "user_email": "john@example.com",
      "admission_number": "ADM001",
      "admission_date": "2025-01-01",
      "current_class": "JSS1",
      "status": "active",
      "created_at": "2025-01-01T10:00:00Z"
    }
  ]
  ```
- **POST Required Fields**: `first_name`, `last_name`, `email`, `password`, `school`, `admission_number`, `admission_date`, `current_class`
- **POST Optional Fields**: None - all fields are required
- **POST Body**:
  ```json
  {
    "first_name": "John",
    "last_name": "Doe",
    "email": "john@example.com",
    "password": "SecurePass123!",
    "school": 1,
    "admission_number": "ADM001",
    "admission_date": "2025-01-01",
    "current_class": "JSS1"
  }
  ```
- **POST Response** (201 Created): Created student object

### Get/Update/Delete Student
- **Endpoint**: `GET/PATCH/DELETE /api/students/<student_id>/`
- **Auth**: Required
- **GET Response** (200 OK): Student object with full details including profile and guardians
- **PATCH Editable Fields**: `current_class`, `status`, `school`
- **PATCH Read-only Fields**: All other fields
- **PATCH Body** (send only fields you want to update):
  ```json
  {
    "current_class": "JSS2",
    "status": "active",
    "school": 1
  }
  ```
- **PATCH Response** (200 OK): Updated student object
- **DELETE Response** (204 No Content)

### Promote Student
- **Endpoint**: `POST /api/students/<student_id>/promote/`
- **Auth**: Required
- **Permissions**: admin only
- **Body**: Empty or minimal payload
- **Response** (200 OK): Success message with new class

### Get Student Profile
- **Endpoint**: `GET /api/students/<student_id>/profile/`
- **Auth**: Required
- **Response** (200 OK):
  ```json
  {
    "id": 1,
    "student": 1,
    "date_of_birth": "2010-05-15",
    "gender": "M",
    "blood_group": "O+",
    "address": "123 Main St",
    "guardian": {
      "id": 1,
      "name": "Jane Doe",
      "relationship": "Mother",
      "contact_number": "555-1234",
      "email": "jane@example.com",
      "address": "123 Main St"
    }
  }
  ```

### Bulk Upload Students
- **Endpoint**: `POST /api/students/bulk-upload/`
- **Auth**: Required
- **Permissions**: admin only
- **Content-Type**: `multipart/form-data`
- **Required Fields**: CSV file with student data
- **Response** (200 OK): Upload status with success/error count

---

## Teachers/Staff Module

### List/Create Teachers
- **Endpoint**: `GET/POST /api/teachers/`
- **Auth**: Required
- **GET Response** (200 OK):
  ```json
  [
    {
      "id": 1,
      "user": 10,
      "user_name": "Jane Smith",
      "user_email": "jane@example.com",
      "employee_id": "EMP001",
      "qualification": "B.Sc. Education",
      "specialization": "Mathematics",
      "created_at": "2025-01-01T10:00:00Z"
    }
  ]
  ```
- **POST Required Fields**: `first_name`, `last_name`, `email`, `password`, `employee_id`, `qualification`, `specialization`, `department`
- **POST Optional Fields**: None - all fields are required
- **POST Body**:
  ```json
  {
    "first_name": "Jane",
    "last_name": "Smith",
    "email": "jane@example.com",
    "password": "SecurePass123!",
    "employee_id": "EMP001",
    "qualification": "B.Sc. Education",
    "specialization": "Mathematics",
    "department": "Science"
  }
  ```
- **POST Response** (201 Created): Created teacher object

### Get/Update Teacher
- **Endpoint**: `GET/PATCH /api/teachers/<teacher_id>/`
- **Auth**: Required
- **GET Response** (200 OK): Teacher object with user details
- **PATCH Editable Fields**: `qualification`, `specialization`, `department`
- **PATCH Read-only Fields**: `id`, `user`, `user_details`, `created_at`, `updated_at`
- **PATCH Body** (send only fields you want to update):
  ```json
  {
    "qualification": "M.Sc. Education",
    "specialization": "Advanced Mathematics",
    "department": "Science"
  }
  ```
- **PATCH Response** (200 OK): Updated teacher object

### Assign Subjects to Teacher
- **Endpoint**: `POST /api/teachers/<teacher_id>/assign-subjects/`
- **Auth**: Required
- **Permissions**: admin only
- **Required Fields**: `subjects`
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
- **Response** (200 OK): Array of classes assigned to teacher

---

## Academics Module

### List Classes
- **Endpoint**: `GET /api/academics/classes/`
- **Auth**: Required
- **Response** (200 OK): Array of class objects

### Create Class Arm/Section
- **Endpoint**: `POST /api/academics/arms/`
- **Auth**: Required
- **Permissions**: admin only
- **Body**: Class arm details
- **Response** (201 Created): Created arm object

### List Subjects
- **Endpoint**: `GET /api/academics/subjects/`
- **Auth**: Required
- **Response** (200 OK): Array of subject objects

### Assign Subjects to Class
- **Endpoint**: `POST /api/academics/subjects/assign/`
- **Auth**: Required
- **Permissions**: admin only
- **Required Fields**: `class_id`, `subjects`
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
- **Body**: Attendance details
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
- **Response** (200 OK): Array of attendance records

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
- **Response** (200 OK): Array of assessments

### Enter Scores
- **Endpoint**: `POST /api/results/scores/`
- **Auth**: Required
- **Permissions**: teacher only
- **Body**: Score details
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
- **Query Parameters**: `class_id`, `assessment_id` (optional)
- **Response** (200 OK): Class results

### Approve Class Results
- **Endpoint**: `POST /api/results/approve/`
- **Auth**: Required
- **Permissions**: admin only
- **Body**: Class and assessment IDs
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
- **Body**: Category details
- **Response** (201 Created): Category object

### Assign Fees to Class
- **Endpoint**: `POST /api/fees/structures/`
- **Auth**: Required
- **Permissions**: admin only
- **Body**: Fee structure details
- **Response** (201 Created): Fee structure object

### List Invoices
- **Endpoint**: `GET /api/fees/invoices/`
- **Auth**: Required
- **Permissions**: admin only
- **Response** (200 OK): Array of invoices

### Get Invoice Details
- **Endpoint**: `GET /api/fees/invoices/<invoice_id>/`
- **Auth**: Required
- **Permissions**: admin only
- **Response** (200 OK): Invoice object

### Record Payment
- **Endpoint**: `POST /api/fees/payments/`
- **Auth**: Required
- **Permissions**: admin only
- **Body**: Payment details
- **Response** (201 Created): Payment record

### Get Payment History
- **Endpoint**: `GET /api/fees/payments/history/`
- **Auth**: Required
- **Permissions**: admin only
- **Response** (200 OK): Payment history array

---

## Communications Module

### List/Create Announcements
- **Endpoint**: `GET/POST /api/communications/announcements/`
- **Auth**: Required for GET; admin required for POST
- **GET Response** (200 OK): Array of announcements
- **POST Body**: Announcement content
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
- **Body**: Timetable details
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
- **Query Parameters**: `class_id`, `date_from`, `date_to` (optional)
- **Response** (200 OK): Attendance report

### Get Fees Report
- **Endpoint**: `GET /api/reports/fees/`
- **Auth**: Required
- **Permissions**: admin only
- **Query Parameters**: `class_id`, `month`, `year` (optional)
- **Response** (200 OK): Fees collection report

### Get Academics Report
- **Endpoint**: `GET /api/reports/academics/`
- **Auth**: Required
- **Permissions**: admin only
- **Query Parameters**: `class_id`, `term`, `year` (optional)
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
- **Required Fields**: `plan_id`
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
- **Query Parameters**: `user_id`, `action`, `date_from`, `date_to` (optional)
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

---

## User Roles

- **super_admin**: Full system access, manage schools and administrators
- **school_admin**: School-level administration, manage staff and students
- **admin**: School administrator with broad access
- **teacher**: Teaching staff with access to classes, attendance, results
- **student**: Student access to own profile and academic records
- **parent**: Parent/guardian access to student records

---

## Notes

- **Field Validation**: All required fields must be provided in the request body
- **Editable vs Read-only Fields**: Read-only fields are auto-generated or should not be modified by the client
- **Error Responses**: Use the appropriate HTTP status code and include error details in the response body
- **Pagination**: Some list endpoints may support pagination parameters (not documented here - check specific endpoint)
- **Timestamps**: All datetime fields use ISO 8601 format (YYYY-MM-DDTHH:mm:ssZ)

For interactive API documentation, visit `/api-docs/` endpoint.
