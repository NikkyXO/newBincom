from bincom.settings.base import *
import os
from decouple import config

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/ 

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


#Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": config("DB_NAME"),
        "USER": "Olanike",
        "PASSWORD": config('DB_PASSWORD'),
        "HOST": 'Olanike.mysql.pythonanywhere-services.com',
        "PORT": "3306"
    }
}