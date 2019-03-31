from .base import *


INSTALLED_APPS += [
    'insights.apps.InsightsConfig',
    'insights_instagram.apps.InsightsInstagramConfig',
    'insights_twitter.apps.InsightsTwitterConfig',
]

'''
-- Create database
CREATE DATABASE insights WITH ENCODING 'UTF-8' LC_COLLATE 'en_US.UTF-8' LC_CTYPE 'en_US.UTF-8' TEMPLATE template0;

-- Create user and assign database
CREATE USER insights WITH ENCRYPTED PASSWORD 'gRp&3aSGS&^d-9B7';
GRANT ALL PRIVILEGES ON DATABASE insights TO insights;
-- For running tests
ALTER USER insights CREATEDB;

-- Destroy database
-- DROP DATABASE insights;
'''

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'insights',
#         'USER': 'insights',
#         'PASSWORD': 'gRp&3aSGS&^d-9B7',
#         'HOST': 'ocupa2.lxd',
#         'PORT': 5432,
#     },
# }


###############################################################################
# Instagram
INSTAGRAM_API_URL = 'http://hackathon.ocupa2.com/instagram'


###############################################################################
# Twitter
TWITTER_API_URL = 'http://hackathon.ocupa2.com/twitter/1.1'
