# SMS Project — API Documentation

This document describes the API endpoints implemented so far in the project. It covers authentication and the `accounts` and `schools` APIs. Use the JWT token endpoints to authenticate where required.

**Base URL**: assume your server runs at `http://localhost:8000/` and the app routes are mounted at their app paths (for example, `/api/accounts/` or however you include them in the project URL configuration).

**Authentication**
- **Obtain token**: `POST /token/`
  - Body (JSON):
    - `email` (string)
    - `password` (string)
  - Response: JSON with `access` and `refresh` tokens.
  - Example:

```bash
curl -X POST http://localhost:8000/api/accounts/token/ \
  -H "Content-Type: application/json" \
  -d '{"email": "admin@example.com", "password": "secret"}'
```

- **Refresh token**: `POST /token/refresh/`
  - Body (JSON):
    - `refresh` (string)
  - Response: JSON with a new `access` token.

- **Authenticated requests**
  - Include header: `Authorization: Bearer <access_token>`


**Accounts API**

- Register a new user
  - Endpoint: `POST /register/`
  - Auth: Public (no token required)
  - Purpose: Create a new `User`. The project includes a `UserCreationForm` that lists the expected fields.
  - Request body (JSON):
    - `first_name` (string, optional)
    - `last_name` (string, optional)
    - `email` (string, required, unique)
    - `username` (string, optional — auto-derived from email if not provided)
    - `role` (string, required) — one of `super_admin`, `school_admin`, `teacher`, `student`, `parent`
    - `school` (string, optional)
    - `password1` (string, required)
    - `password2` (string, required)
  - Responses:
    - `201 Created` — returns created user representation (fields depend on serializer)
    - `400 Bad Request` — returns validation errors
  - Example request:

```bash
curl -X POST http://localhost:8000/api/accounts/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "first_name": "Jane",
    "last_name": "Doe",
    "email": "jane@example.com",
    "username": "jane",
    "role": "teacher",
    "school": "Springfield High",
    "password1": "StrongPass123",
    "password2": "StrongPass123"
  }'
```

- Obtain users list
  - Endpoint: `GET /users/`
  - Auth: Required (`Authorization: Bearer <token>`)
  - Permission: any authenticated user (view currently requires `IsAuthenticated`)
  - Response:
    - `200 OK` — list of user objects

- Get user detail
  - Endpoint: `GET /users/<user_id>/`
  - Auth: Required
  - Response:
    - `200 OK` — user object
    - `404 Not Found` — if user does not exist

- Update user
  - Endpoint: `PUT /users/<user_id>/update/` or `PATCH /users/<user_id>/update/`
  - Auth: Required
  - Purpose: Replace or partially update user attributes
  - Request body: fields to update (email, first_name, last_name, role, school, etc.)
  - Responses:
    - `200 OK` — updated user
    - `400 Bad Request` — validation errors
    - `404 Not Found` — user not found

- Change password
  - Endpoint: `POST /users/change-password/`
  - Auth: Required
  - Request body (JSON):
    - `old_password` (string, required)
    - `new_password` (string, required)
    - `confirm_new_password` (string, required)
  - Behavior: verifies `old_password`, ensures the new passwords match, sets the new password
  - Responses:
    - `200 OK` — password changed successfully
    - `400 Bad Request` — incorrect old password or validation errors


**Schools API**

- Add a school
  - Endpoint: `POST /add/`
  - Auth: Required
  - Permission: Only users with `role == "super_admin"` (the view enforces this)
  - Request body (JSON): fields depend on `AddSchoolSerializer` (typical fields: `name`, `address`, `phone`, etc.)
  - Responses:
    - `201 Created` — created school object
    - `400 Bad Request` — validation errors
    - `403 Forbidden` — user lacks `super_admin` role

- View a school
  - Endpoint: `GET /view/<school_id>/`
  - Auth: Required
  - Permission: Only `super_admin`
  - Responses:
    - `200 OK` — school object
    - `403 Forbidden` — if not `super_admin`
    - `404 Not Found` — school not found

- Update a school
  - Endpoint: `PUT /update/<school_id>/` or `PATCH /update/<school_id>/`
  - Auth: Required
  - Permission: Only `super_admin`
  - Request body: fields to update (as accepted by `UpdateSchoolSerializer`)
  - Responses:
    - `200 OK` — updated school object
    - `400 Bad Request` — validation errors
    - `403 Forbidden` — user lacks `super_admin` role
    - `404 Not Found` — school not found


**Notes & Implementation Details**
- The project uses JWT authentication via `rest_framework_simplejwt`. Endpoints for token obtain/refresh are exposed in `accounts/urls.py` as `/token/` and `/token/refresh/`.
- The `UserCreationForm` used by registration lists the fields in `accounts/forms.py`. The API expects the passwords as `password1` and `password2` just like Django's `UserCreationForm`.
- Some views import serializers such as `AllUsersSerializers`, `UserDetailSerializer`, `UpdateUserSerializer`, and `PasswordChangeSerializer`. Ensure these serializers exist and expose the fields expected by your frontend or API consumers.


**Quick Examples**

- Login and list users (example flow):

```bash
# 1) Obtain token
curl -X POST http://localhost:8000/api/accounts/token/ \
  -H "Content-Type: application/json" \
  -d '{"email":"admin@example.com","password":"adminpass"}'

# 2) Use the returned access token to list users
curl -X GET http://localhost:8000/api/accounts/users/ \
  -H "Authorization: Bearer <access_token>"
```


If you want, I can:
- Generate example request/response JSON payloads for each endpoint.
- Add the exact serializer field lists by updating or reading the serializer files and embedding them in this document.
- Wire the documentation into a `/docs/` route (Swagger/OpenAPI) by adding DRF schema generation and `drf-yasg` or `drf-spectacular`.

---
Generated from the current codebase: `accounts` and `schools` view and URL definitions. If you'd like, I can expand the document with exact serializer schemas by reading or creating the serializer files next.