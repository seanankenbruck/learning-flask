from flask_sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash
# Create db variable as instance of SQLAlchemy class
db = SQLAlchemy()
# Create python class to model user attributes (same as database)
class User(db.Model):
	__tablename__ = 'users'
	uid = db.Column(db.Integer, primary_key=True)
	firstname = db.Column(db.String(100))
	lastname = db.Column(db.String(100))
	email = db.Column(db.String(120), unique=True)
	pwdhash = db.Column(db.String(54))
	# Initialize function to construct user objects
	def __init__(self, firstname, lastname, email, password):
		self.firstname = firstname.title() # First letter capitalized
		self.lastname = lastname.title()
		self.email = email.lower() # Lowercase for standardization
		self.set_password(password) # Use encrypted password, function below
	# Creates a hash of the password, ensures that passwords are not stored in the db
	def set_password(self, password):
		self.pwdhash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.pwdhash, password)