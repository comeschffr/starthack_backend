from starthackapp import app, db
import enum


class Likeness(enum.Enum):
	LIKE = 'LIKE'
	UNLIKE = 'UNLIKE'
	SUPER_LIKE = 'SUPER_LIKE'


class Hero(db.Model):
	# Defines the Table Name user
	__tablename__ = "hero"

	# Makes three columns into the table id, name, email
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(100), nullable=False)
	world = db.Column(db.String(100))
	profile_pic_url = db.Column(db.String(500))
	likeness = db.Column(db.Enum(Likeness))

	# A constructor function where we will pass the name and email of a user and it gets add as a new entry in the table.
	def __init__(self, name, world=None, profile_pic_url=None):
		self.name = name
		self.world = world
		self.profile_pic_url = profile_pic_url
