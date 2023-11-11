from models import db, User
from app import app
from werkzeug.security import generate_password_hash

admin = User(name = "admin", email = "admin@gmail.com", password = generate_password_hash("sirius"), role = 1)
with app.app_context():
    db.session.add(admin)
    db.session.commit()