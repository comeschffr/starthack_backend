from starthackapp import app, db
from flask import jsonify


@app.route('/')
def index():
    return jsonify('Welcome to my app bro (main branch)')


@app.route('/register', methods=["GET", "POST"])
def register():
    return jsonify('Just landed on the /register endpoint')


@app.route('/login', methods=["GET", "POST"])
def login():
    return jsonify('Just landed on the /login endpoint')
