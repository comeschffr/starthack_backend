from starthackapp import (
    app,
    db,
    models,
)
from flask import jsonify, request


@app.route('/')
def index():
    return jsonify('Welcome to my app bro (main branch)')


@app.route('/register', methods=["GET", "POST"])
def register():
    return jsonify('Just landed on the /register endpoint')


@app.route('/login', methods=["GET", "POST"])
def login():
    return jsonify('Just landed on the /login endpoint')


@app.route('/test', methods=["GET", "POST"])
def test():
    return jsonify('Test endpoint')


@app.route('/add_user', methods=["POST"])
def add_user():
    new_user = models.User(request.form.get('name'), request.form.get('email'))
    db.session.add(new_user)
    db.session.commit()
    return jsonify('Added a new user successfully!')


@app.route('/get_users', methods=["GET"])
def get_users():
    users = models.User.query.all()
    users = [
        {
            'id': user.id,
            'name': user.name,
            'email': user.email,
        } for user in users
    ]
    return jsonify(users)




