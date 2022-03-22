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


# @app.route('/add_user', methods=["POST"])
# def add_user():
#     new_user = models.User(request.form.get('name'), request.form.get('email'))
#     db.session.add(new_user)
#     db.session.commit()
#     return jsonify('Added a new user successfully!')


# @app.route('/get_users', methods=["GET"])
# def get_users():
#     users = models.User.query.all()
#     users = [
#         {
#             'id': user.id,
#             'name': user.name,
#             'email': user.email,
#         } for user in users
#     ]
#     return jsonify(users)


@app.route('/add_hero', methods=["POST"])
def add_hero():
    new_hero = models.Hero(request.form.get('name'), request.form.get('world'))
    db.session.add(new_hero)
    db.session.commit()
    return jsonify('Added a new hero successfully!')



@app.route('/swipe', methods=["POST"])
def swipe():
    form_data = request.form
    hero_id = form_data.get('hero_id')
    swipe_dir = form_data.get('swipe_dir')

    hero = models.User.query.get(hero_id)
    if swipe_dir == 'right':
        hero.likeness = models.Likeness.LIKE
    elif swipe_dir == 'left':
        hero.likeness = models.Likeness.NO_LIKE
    elif swipe_dir == 'up':
        hero.likeness = models.Likeness.SUPER_LIKE

    db.session.commit()
    return jsonify('Swiped successfully!')


