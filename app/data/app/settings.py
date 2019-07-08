ALLOWED_HOSTS = [
    'localhost',            # Add Your IP Or URL in production
]


DATABASES = {               # Modify for Postgres
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'put-your-password-here',
        'HOST': 'db',
        'PORT': 5432,
    }
}


STATIC_URL = '/static/'     # Add you static address mask

STATIC_ROOT = os.path.join(BASE_DIR, "static/")   # collectstatics folder
