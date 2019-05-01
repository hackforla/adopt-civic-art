import os

from .base import *  # noqa

import environ
env = environ.Env()

DEBUG = False

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']

DATABASES = {"default": env.db("DATABASE_URL")}
DATABASES["default"]["ATOMIC_REQUESTS"] = True

AWS_QUERYSTRING_AUTH = False
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = os.environ['S3_BUCKET']
MEDIA_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
