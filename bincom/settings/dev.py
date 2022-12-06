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
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sql8582000',
        'USER': 'sql8582000',
        'PASSWORD': ' YTyl3z4HAW',
        'HOST':'sql8.freemysqlhosting.net',
        'PORT':'3306',
    }
}