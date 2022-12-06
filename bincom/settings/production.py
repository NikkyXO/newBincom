from bincom.settings.base import *
import os
from decouple import config

SECRET_KEY = config('SECRET_KEY')

DEBUG = False


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST':'localhost',
        'PORT':'3306',
    }
}