from starthackapp import (
    app,
    db,
    models,
    tmdb,
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


def find_US_title(alternative_titles):
    titles = alternative_titles['titles']
    for title in titles:
        if title['iso_3166_1'] == 'US':
            return title['title']
    else:
        return titles[0]['title']

def find_US_release_date(release_dates):
    dates = release_dates['results']
    for date in dates:
        if date['iso_3166_1'] == 'US':
            return int(date['release_dates'][0]['release_date'][:4])
    else:
        return int(dates[0]['release_dates'][0]['release_date'][:4])

def find_US_best_poster(posters):
    for poster in posters:
        if poster['iso_639_1'] == 'en':
            return poster['file_path']
    else:
        return posters[0]['file_path']

def find_US_trailer(videos):
    videos = videos['results']
    for video in videos:
        if video['iso_639_1'] == 'en':
            return video['key']
    else:
        return videos[0]['key']


@app.route('/get_next_movie', methods=["GET"])
def get_next_movie():
    config = tmdb.Configuration()
    base_url = config.info()['images']['secure_base_url']

    movie = tmdb.Movies(603)
    movie.images()
    print(movie)
    movie_dict = {
        'movie_id': movie.id,
        'title': find_US_title(movie.alternative_titles()),
        'release_date': find_US_release_date(movie.release_dates()),
        'poster_url': base_url+'original'+find_US_best_poster(movie.posters),
        'trailer_url': 'https://www.youtube.com/watch?v='+find_US_trailer(movie.videos()),
        # 'shorts_urls': shorts_urls,
    }

    return jsonify(movie_dict)



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


# @app.route('/get_heros', methods=["GET"])
# def get_heros():
#     heros = models.Hero.query.all()
#     heros = [
#         {
#             'id': hero.id,
#             'name': hero.name,
#             'world': hero.world,
#             'likeness': str(hero.likeness),
#             'profile_pic_url': hero.profile_pic_url,
#         } for hero in heros
#     ]
#     return jsonify({'results': heros})


# @app.route('/add_hero', methods=["POST"])
# def add_hero():
#     new_hero = models.Hero(request.form.get('name'), request.form.get('world'), request.form.get('profile_pic_url'))
#     db.session.add(new_hero)
#     db.session.commit()
#     return jsonify('Added a new hero successfully!')


# @app.route('/add_profile_pic', methods=["POST"])
# def add_pp_to_hero():
#     form_data = request.form
#     hero_id = form_data.get('hero_id')
#     pp_url = form_data.get('profile_pic_url')

#     hero = models.Hero.query.get(hero_id)

#     hero.profile_pic_url = pp_url
#     db.session.commit()
#     return jsonify(f'Added a new pp to ({hero.id}, {hero.name}) successfully!')


# @app.route('/swipe', methods=["POST"])
# def swipe():
#     form_data = request.form
#     hero_id = form_data.get('hero_id')
#     swipe_dir = form_data.get('swipe_dir')

#     hero = models.Hero.query.get(hero_id)
#     if swipe_dir == 'right':
#         hero.likeness = models.Likeness.LIKE
#     elif swipe_dir == 'left':
#         hero.likeness = models.Likeness.UNLIKE
#     elif swipe_dir == 'up':
#         hero.likeness = models.Likeness.SUPER_LIKE

#     db.session.commit()
#     return jsonify('Swiped successfully!')
