from market import db
from models import User


user = User.query.get(2)
user.budget = 20000
db.session.commit()