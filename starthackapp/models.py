from starthackapp import app, db


class User(db.Model):
	# Defines the Table Name user
	__tablename__ = "user"

	# Makes three columns into the table id, name, email
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(100), nullable=False)
	email = db.Column(db.String(100), nullable=False)

	# A constructor function where we will pass the name and email of a user and it gets add as a new entry in the table.
	def __init__(self, name, email):
		self.name = name
		self.email = email
