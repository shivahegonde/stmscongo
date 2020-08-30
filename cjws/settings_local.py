from .settings import *

DEBUG = os.getenv('DEBUG', False)

ALLOWED_HOSTS = ['127.0.0.1', '*']

MIDDLEWARE=[ 'django.contrib.messages.context_processors.messages',
             'django.contrib.auth.middleware.AuthenticationMiddleware',
             'django.contrib.messages.middleware.MessageMiddleware',
             'django.contrib.sessions.middleware.SessionMiddleware',
             ]
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                "django.contrib.auth.context_processors.auth",
"django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'sqlite3.db',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}