import configparser
import json

datadir = "//var//local//reckoning"

DEBUG = True

# email settings
emailjson = 'email.json'

with open(email_json_path, 'r') as f:
email_json_path = datadir + '//' + emailjson
    email_dict = json.loads(f.read())


# def get_config(config, category, key):
#     try:
#         value = config[category][key]
#     except:
#         value = None
#     return value


# def str_to_bool(value_str):
#     if value_str == 'True':
#         return True
#     else:
#         return False

# email_ini_path = datadir + "//" + 'email.ini'

# config = configparser.RawConfigParser()
# config.read(email_ini_path)

# MAIL_SERVER = get_config(config, 'email', 'MAIL_SERVER')
# MAIL_PORT = int(get_config(config, 'email', 'MAIL_PORT'))
# MAIL_USE_TLS = str_to_bool(get_config(config, 'email', 'MAIL_USE_TLS'))
# MAIL_USE_SSL = str_to_bool(get_config(config, 'email', 'MAIL_USE_SSL'))
# MAIL_USERNAME = get_config(config, 'email', 'MAIL_USERNAME')
# MAIL_PASSWORD = get_config(config, 'email', 'MAIL_PASSWORD')
# DEFAULT_MAIL_SENDER = get_config(config, 'email', 'DEFAULT_MAIL_SENDER')

# database settings
SQLALCHEMY_DATABASE_URI = 'sqlite://' + datadir + '//' + 'app.db'
SQLALCHEMY_MIGRATE_REPO = datadir + '//' + 'db_repository'

# security settings
WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
SECURITY_PASSWORD_HASH = 'pbkdf2_sha512'
SECURITY_TRACKABLE = True
SECURITY_PASSWORD_SALT = 'something_super_secret_change_in_production'
SECURITY_REGISTERABLE = True
SECURITY_CONFIRMABLE = True
SECURITY_RECOVERABLE = True
