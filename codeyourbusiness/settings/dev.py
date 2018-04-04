from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2v2h^ose%h*)n!*$92(eswxg21*5sbl^iozw6#yvqw36j6-)-@'



ALLOWED_HOSTS = ['codeyourbusiness.pythonanywhere.com', '127.0.0.1', 'cyb.eu-gb.mybluemix.net', '173.249.43.147','codeyourbusiness.com',  ]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass
