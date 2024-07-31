from os import getenv
from os.path import join, dirname, abspath
from dotenv import load_dotenv

basedir = abspath(dirname(__name__))
load_dotenv(join(basedir, '.env'))

SOCIAL_AUTH_FACEBOOK_KEY = str(getenv('SOCIAL_AUTH_FACEBOOK_KEY'))
SOCIAL_AUTH_FACEBOOK_SECRET = str(getenv('SOCIAL_AUTH_FACEBOOK_SECRET'))

SECRET_KEY = "dVu9jfC1PPVGRkq-X5nKaP_vDHC63CxQ2K4W0QVpFJo"