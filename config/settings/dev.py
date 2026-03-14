from datetime import timedelta
import os
from django.core.management.utils import get_random_secret_key
from dotenv import load_dotenv


# Import base settings first
from .base import *  # noqa: F401, F403

# Load .env for local development
load_dotenv()

# SECURITY
SECRET_KEY = os.getenv('SECRET_KEY', get_random_secret_key())
DEBUG = os.getenv('DEBUG', 'True').lower() in ('true', '1', 'yes')

# Local development hosts
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost,127.0.0.1,0.0.0.0').split(',')

# CORS: allow all local dev if explicitly requested
if os.getenv('CORS_ALLOW_ALL', 'True').lower() in ('true', '1', 'yes'):
    CORS_ALLOW_ALL_ORIGINS = True
    CORS_ALLOW_CREDENTIALS = True
else:
    CORS_ALLOW_ALL_ORIGINS = False
    CORS_ALLOW_CREDENTIALS = os.getenv('CORS_ALLOW_CREDENTIALS', 'True').lower() in ('true', '1', 'yes')

# Security relaxation for development
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
CSRF_COOKIE_HTTPONLY = True

# Database (defaults to sqlite, can use Postgres via env)
USE_SUPABASE = os.getenv('USE_SUPABASE', 'False').lower() in ('true', '1', 'yes')

if USE_SUPABASE:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv('DB_NAME', 'postgres'),
            'USER': os.getenv('DB_USER', 'postgres'),
            'PASSWORD': os.getenv('PASSWORD', ''),
            'HOST': os.getenv('HOST', 'localhost'),
            'PORT': os.getenv('PORT', '5432'),
            'CONN_MAX_AGE': 600,
            'OPTIONS': {'connect_timeout': 10},
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }


# MEDIA stored on Supabase S3
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
AWS_S3_REGION_NAME = os.getenv('AWS_S3_REGION_NAME')
AWS_S3_ENDPOINT_URL = os.getenv('AWS_S3_ENDPOINT_URL')
AWS_QUERYSTRING_AUTH = False
AWS_DEFAULT_ACL = None  # Supabase does not support ACLs


if USE_SUPABASE:
    STORAGES = {
        "default": {
            "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",  # media files
        },
        "staticfiles": {
            "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",  # Static from repo
        },
    }
    MEDIA_URL = f"{AWS_S3_ENDPOINT_URL}/{AWS_STORAGE_BUCKET_NAME}/media/"
    MEDIA_ROOT = None
else:
    # Local file storage for development without Supabase / S3 backend
    DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
    STORAGES = {
        "default": {
            "BACKEND": "django.core.files.storage.FileSystemStorage",
        },
        "staticfiles": {
            "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
        },
    }
    MEDIA_URL = '/media/'
    MEDIA_ROOT = BASE_DIR / 'media'

# Supabase / AWS media values for local selects
SUPABASE_URL = os.getenv('SUPABASE_URL', SUPABASE_URL if 'SUPABASE_URL' in globals() else None)
SUPABASE_SERVICE_KEY = os.getenv('SUPABASE_SERVICE_KEY', SUPABASE_SERVICE_KEY if 'SUPABASE_SERVICE_KEY' in globals() else None)

# JWT config (development defaults)
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=int(os.getenv('JWT_ACCESS_LIFETIME_MINUTES', '1440'))),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=int(os.getenv('JWT_REFRESH_LIFETIME_DAYS', '7'))),
    'AUTH_HEADER_TYPES': ('Bearer',),
}
