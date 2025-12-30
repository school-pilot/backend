# SMS Project - Database Setup Guide

## Database Configuration

This project supports two database configurations:

### 1. **SQLite (Default - Local Development)**
- No additional setup required
- Database file: `db.sqlite3`
- Best for: Local development and testing
- Setup: Already configured, just run migrations

### 2. **Supabase PostgreSQL (Production & Hosted)**
- Cloud-hosted PostgreSQL database
- Best for: Production deployments
- Requires network connectivity to Supabase servers

## Quick Start

### Using SQLite (Recommended for local development)

```bash
# Environment variables are already configured for SQLite
# (USE_SUPABASE=False in .env)

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Start development server
python manage.py runserver
```

### Using Supabase PostgreSQL

#### Step 1: Get Supabase Credentials
1. Go to https://supabase.com and sign in
2. Create or select your project
3. Go to **Settings** > **Database**
4. Copy:
   - Host: `db.{project-ref}.supabase.co`
   - Port: `5432`
   - Database name: `postgres`
   - User: `postgres`
   - Password: (from Database settings)

#### Step 2: Update Environment Variables

Edit `.env` file:

```env
USE_SUPABASE=True
HOST=db.your-project-ref.supabase.co
PORT=5432
DB_USER=postgres
PASSWORD=your_supabase_password
DB_NAME=postgres
SUPABASE_URL=https://your-project-ref.supabase.co
SUPABASE_KEY=your_public_anon_key
```

#### Step 3: Install PostgreSQL Driver

```bash
pip install psycopg2-binary
# or for development
pip install psycopg2
```

#### Step 4: Run Migrations

```bash
python manage.py migrate
```

#### Step 5: Create Superuser

```bash
python manage.py createsuperuser
```

#### Step 6: Start Server

```bash
python manage.py runserver
```

## Troubleshooting

### "Network is unreachable" Error

**Cause**: Your environment cannot reach the Supabase server (firewall, network issues, or DNS resolution)

**Solution**: 
1. Check if Supabase is set to the correct host
2. Test connectivity:
   ```bash
   nc -zv db.your-project.supabase.co 5432
   ```
3. Fall back to SQLite:
   ```bash
   # In .env
   USE_SUPABASE=False
   ```

### "Password authentication failed"

**Cause**: Incorrect Supabase credentials in `.env`

**Solution**:
1. Double-check your password in Supabase dashboard
2. Ensure no trailing spaces in `.env`
3. Test the connection manually:
   ```bash
   psql -h db.your-project.supabase.co -U postgres -d postgres
   ```

### Django Shell Database Issues

Clear shell environment before running Django commands if you see stale env vars:

```bash
unset USE_SUPABASE HOST PASSWORD PORT DB_USER DB_NAME
python manage.py migrate
```

## Using Supabase API Client

The project includes a helper module for Supabase API access:

```python
from sms_prj.supabase import supabase

# Get Supabase client
client = supabase()

# Use Supabase API
response = client.table('your_table').select('*').execute()
```

**Requirements**:
- Install: `pip install supabase`
- Set environment variables: `SUPABASE_URL` and `SUPABASE_KEY`

## Environment Variable Reference

| Variable | Required | Example | Purpose |
|----------|----------|---------|---------|
| `USE_SUPABASE` | Yes | `True`/`False` | Switch between Supabase and SQLite |
| `SECRET_KEY` | Yes | `django-insecure-...` | Django secret key |
| `DEBUG` | Yes | `True`/`False` | Debug mode |
| `HOST` | If Supabase | `db.xyz.supabase.co` | Supabase host |
| `PORT` | If Supabase | `5432` | Supabase port |
| `DB_USER` | If Supabase | `postgres` | Database user |
| `PASSWORD` | If Supabase | `password123` | Database password |
| `DB_NAME` | If Supabase | `postgres` | Database name |
| `SUPABASE_URL` | Optional | `https://xyz.supabase.co` | Supabase API URL |
| `SUPABASE_KEY` | Optional | `eyJ...` | Supabase public key |

## File Structure

```
sms_project/
├── .env                    # Environment variables (USE_SUPABASE, DB credentials)
├── .env.example            # Example template for .env
├── db.sqlite3              # SQLite database (when USE_SUPABASE=False)
├── manage.py               # Django management
├── requirements.txt        # Python dependencies
└── sms_prj/
    ├── settings.py         # Database configuration logic
    └── supabase.py         # Supabase client helper
```

## Next Steps

1. **Configure your database**: Update `.env` with your chosen database settings
2. **Run migrations**: `python manage.py migrate`
3. **Create superuser**: `python manage.py createsuperuser`
4. **Access admin panel**: `python manage.py runserver` then visit `http://localhost:8000/admin`
