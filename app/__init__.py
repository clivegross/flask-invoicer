from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security
from flask_mail import Mail
from config import email

app = Flask(__name__)

# import configuration settings
app.config.from_object('config')
app.config.update(email)

# setup database
db = SQLAlchemy(app)

# Setup mail
mail = Mail(app)

from app import views, models
from app.models import user_datastore

# setup security
security = Security(app, user_datastore)

if __name__ == "__main__":
    app.run()

