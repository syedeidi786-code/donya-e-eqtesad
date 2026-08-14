"""
Django settings for news_land project.
"""

from pathlib import Path
import os

from dotenv import load_dotenv
import dj_database_url
import cloudinary


# ============================================================
# BASE
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")


# ============================================================
# SECURITY
# ============================================================

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")

if not SECRET_KEY:
    raise ValueError("DJANGO_SECRET_KEY is not set")


DEBUG = os.environ.get("DEBUG", "False") == "True"


ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    ".onrender.com",
]


if os.environ.get("ALLOWED_HOST"):
    ALLOWED_HOSTS.append(
        os.environ.get("ALLOWED_HOST")
    )


# ============================================================
# APPLICATIONS
# ============================================================

INSTALLED_APPS = [

    # Cloudinary
    "cloudinary",
    "cloudinary_storage",

    # Django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Your apps
    "accounts",
    "articles",

    # Extensions
    "django_extensions",
]


# ============================================================
# MIDDLEWARE
# ============================================================

MIDDLEWARE = [

    "django.middleware.security.SecurityMiddleware",

    # WhiteNoise
    "whitenoise.middleware.WhiteNoiseMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",

    "django.middleware.common.CommonMiddleware",

    "django.middleware.csrf.CsrfViewMiddleware",

    "django.contrib.auth.middleware.AuthenticationMiddleware",

    "django.contrib.messages.middleware.MessageMiddleware",

    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# ============================================================
# URL / WSGI
# ============================================================

ROOT_URLCONF = "news_land.urls"

WSGI_APPLICATION = "news_land.wsgi.application"


# ============================================================
# TEMPLATES
# ============================================================

TEMPLATES = [

    {
        "BACKEND":
            "django.template.backends.django.DjangoTemplates",

        "DIRS": [
            BASE_DIR / "templates"
        ],

        "APP_DIRS": True,

        "OPTIONS": {

            "context_processors": [

                "django.template.context_processors.request",

                "django.contrib.auth.context_processors.auth",

                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# ============================================================
# DATABASE
# ============================================================

DATABASE_URL = os.environ.get("DATABASE_URL")


if DATABASE_URL:

    # Render / PostgreSQL
    DATABASES = {

        "default": dj_database_url.parse(
            DATABASE_URL,
            conn_max_age=600,
            ssl_require=True,
        )

    }

else:

    # Local development
    DATABASES = {

        "default": {

            "ENGINE":
                "django.db.backends.sqlite3",

            "NAME":
                BASE_DIR / "db.sqlite3",
        }
    }


# ============================================================
# PASSWORD VALIDATION
# ============================================================

AUTH_PASSWORD_VALIDATORS = [

    {
        "NAME":
            "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },

    {
        "NAME":
            "django.contrib.auth.password_validation.MinimumLengthValidator",
    },

    {
        "NAME":
            "django.contrib.auth.password_validation.CommonPasswordValidator",
    },

    {
        "NAME":
            "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# ============================================================
# INTERNATIONALIZATION
# ============================================================

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# ============================================================
# STATIC FILES
# ============================================================

STATIC_URL = "/static/"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

STATIC_ROOT = BASE_DIR / "staticfiles"


# ============================================================
# STORAGE
# ============================================================

# Required by django-cloudinary-storage
STATICFILES_STORAGE = (
    "django.contrib.staticfiles.storage.StaticFilesStorage"
)

STORAGES = {
    "default": {
        "BACKEND": (
            "cloudinary_storage.storage.MediaCloudinaryStorage"
        ),
    },
    "staticfiles": {
        "BACKEND": (
            "django.contrib.staticfiles.storage.StaticFilesStorage"
        ),
    },
}

# ============================================================
# CLOUDINARY
# ============================================================

cloudinary.config(

    cloud_name=os.environ.get(
        "CLOUDINARY_CLOUD_NAME"
    ),

    api_key=os.environ.get(
        "CLOUDINARY_API_KEY"
    ),

    api_secret=os.environ.get(
        "CLOUDINARY_API_SECRET"
    ),
)


# ============================================================
# AUTHENTICATION
# ============================================================

LOGIN_URL = "login"

LOGIN_REDIRECT_URL = "dashboard"

LOGOUT_REDIRECT_URL = "/"


# ============================================================
# EMAIL
# ============================================================

EMAIL_BACKEND = (
    "django.core.mail.backends.smtp.EmailBackend"
)


DEFAULT_FROM_EMAIL = "syedeidi786@gmail.com"

SERVER_EMAIL = "syedeidi786@gmail.com"


EMAIL_HOST = "smtp-relay.brevo.com"

EMAIL_HOST_USER = os.environ.get(
    "EMAIL_HOST_USER"
)

EMAIL_HOST_PASSWORD = os.environ.get(
    "EMAIL_HOST_PASSWORD"
)


EMAIL_PORT = 587

EMAIL_USE_TLS = True