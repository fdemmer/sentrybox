# ~/.sentry/sentry.conf.py

# for more information on DATABASES, see the Django configuration at:
# https://docs.djangoproject.com/en/1.6/ref/databases/
DATABASES = {
    'default': {
        # We suggest PostgreSQL for optimal performance
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sentry',
        'USER': 'sentry',
        'PASSWORD': 'ceec4eif7ya',
        'HOST': 'localhost',
        'PORT': '',
    }
}


EMAIL_HOST = 'localhost'
EMAIL_HOST_PASSWORD = ''
EMAIL_HOST_USER = ''
EMAIL_PORT = 25
EMAIL_USE_TLS = False


SENTRY_ADMIN_EMAIL = 'root@localhost'


SENTRY_REDIS_OPTIONS = {
    'hosts': {
        0: {
            'host': '127.0.0.1',
            'port': 6379,
        }
    }
}


# No trailing slash!
SENTRY_URL_PREFIX = 'http://localhost'

SENTRY_WEB_HOST = '0.0.0.0'
SENTRY_WEB_PORT = 9000
SENTRY_WEB_OPTIONS = {
    'workers': 3,  # the number of gunicorn workers
    'secure_scheme_headers': {'X-FORWARDED-PROTO': 'https'},  # detect HTTPS mode from X-Forwarded-Proto header
}

