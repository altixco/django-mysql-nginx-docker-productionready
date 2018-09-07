from .common import *

# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

ALLOWED_HOSTS = ['.project_name.com']

with open(os.environ.get('DJANGO_SECRET_KEY_FILE')) as f:
    SECRET_KEY = f.read().strip()

with open(os.environ.get('MYSQL_USER_FILE')) as f:
    MYSQL_USER = f.read().strip()

with open(os.environ.get('MYSQL_PASSWORD_FILE')) as f:
    MYSQL_PASSWORD = f.read().strip()

with open(os.environ.get('EMAIL_PASSWORD_FILE')) as f:
    EMAIL_PASSWORD = f.read().strip()

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'project_name',
        'USER': MYSQL_USER,
        'PASSWORD': MYSQL_PASSWORD,
        'HOST': 'db',
        'PORT': 3306,
    }
}

# PROD_MIDDLEWARE = [
#    'main.middleware.middleware_name.NameMiddleware'
# ]

# MIDDLEWARE = MIDDLEWARE + PROD_MIDDLEWARE

# Email Config
# EMAIL_HOST = 'smtp.host.com'
# EMAIL_HOST_USER = 'project_name'
# EMAIL_HOST_PASSWORD = EMAIL_PASSWORD

# ADMINS = [('Altix', 'email@gmail.com')]
# MANAGERS = [('Altix', 'email@gmail.com')]
