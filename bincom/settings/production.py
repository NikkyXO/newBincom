from bincom.settings.base import *
import os
from decouple import config

SECRET_KEY = config('SECRET_KEY')

DEBUG = False


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