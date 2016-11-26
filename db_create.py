from app import db, models
from app.models import user_datastore, User, Role
from app import security

db.create_all()

user_datastore.create_user(email="clive@jaglogic.com", password='testing123')
db.session.commit()

print(User.query.first())
