from starthackapp import app, db
import enum


class Swipe(enum.Enum):
	LIKE = 'LIKE'
	DISLIKE = 'DISLIKE'
	SUPER_LIKE = 'SUPER_LIKE'


class InstagramShort(db.Model):
	__tablename__ = "instagram_short"
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	movie_id = db.Column(db.Integer)
	short_url = db.Column(db.String(1000))

	def __init__(self, movie_id, short_url):
		self.movie_id = movie_id
		self.short_url = short_url


class Movie(db.Model):
	__tablename__ = "movies"
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	movie_id = db.Column(db.Integer)

	def __init__(self, movie_id):
		self.movie_id = movie_id


class MovieSwipe(db.Model):
	__tablename__ = "movie_swipe"
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	movie_id = db.Column(db.Integer)
	swipe = db.Column(db.Enum(Swipe))

	def __init__(self, movie_id, swipe):
		self.movie_id = movie_id
		self.swipe = swipe
