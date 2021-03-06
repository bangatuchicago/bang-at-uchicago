from local_settings import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['bangatuchicago.com']

STATIC_ROOT = os.path.join(SITE_ROOT, 'static')

SESSION_ENGINE = "django.contrib.sessions.backends.cache"

BROKER_URL = "amqp://guest@localhost//bauc"

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
