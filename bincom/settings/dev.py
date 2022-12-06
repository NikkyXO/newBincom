from bincom.settings.base import *


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/ 

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-v5i1eqi*rf!mkdd^y&&=bim(^fitk1(9knfi7a6(5j2xn@jvzk"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

import os
from decouple import config
#Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": config("DB_NAME"),
        "USER": "root",
        "PASSWORD": config('DB_PASSWORD'),
        "HOST": config('DB_HOST'),
        "PORT": "3306"
    }
}