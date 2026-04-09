from .base import *
from decouple import Config, RepositoryEnv
from pathlib import Path

DEBUG = False

ADMINS = [
    ('Ron', 'autodesk0914@icloud.com'),
]

ALLOWED_HOSTS = ['educaproject.com', 'www.educaproject.com', '127.0.0.1', 'localhost', '.educaproject.com']

SETTINGS_DIR = Path(__file__).resolve().parent
ENV_FILE = SETTINGS_DIR / '.env'
config = Config(RepositoryEnv(str(ENV_FILE)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('POSTGRES_DB'),
        'USER': config('POSTGRES_USER'),
        'PASSWORD': config('POSTGRES_PASSWORD'),
        'HOST': 'db',
        'PORT': 5432,
    }
}

REDIS_URL = 'redis://cache:6379'
CACHES['default']['LOCATION'] = REDIS_URL
CHANNEL_LAYERS['default']['CONFIG']['hosts'] = [REDIS_URL]

# Security
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.resend.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'resend'
EMAIL_HOST_PASSWORD = config('RESEND_API_KEY', default='')
DEFAULT_FROM_EMAIL = 'onboarding@resend.dev'