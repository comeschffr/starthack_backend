from starthackapp import (
    app,
    db,
    models,
    tmdb,
    ig_client,
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


def find_US_trailer(videos):
    videos = videos['results']
    for video in videos:
        if video['iso_639_1'] == 'en':
            return video['key']
    else:
        return videos[0]['key']

def get_top3_cast(full_cast):
    top3_cast = []
    for i, actor in enumerate(full_cast):
        if i > 2: break
        top3_cast.append(actor['name'])
    return top3_cast

@app.route('/get_next_movies', methods=["GET"])
def get_next_movies():
    config = tmdb.Configuration()
    base_url = config.info()['images']['secure_base_url']

    # movies = [tmdb.Movies(movie_id) for movie_id in [603, 675, 604, 106646, 190859]]
    movies = [tmdb.Movies(movie_id) for movie_id in [603]]
    ig_shorts_list = []
    for movie in movies:
        movie.info()
        movie.credits()
        movie.images()
        ig_hashtag = ''.join(filter(str.isalpha, movie.title))+'edit'
        ig_shorts_list.append([str(media.dict()['video_url']) for media in ig_client.hashtag_medias_top(ig_hashtag, amount=3)])

    movies_dict = [
        {
            'movie_id': movie.id,
            'title': movie.title,
            'release_date': int(movie.release_date[:4]),
            'poster_url': base_url+'original'+movie.poster_path,
            'trailer_url': 'https://www.youtube.com/watch?v='+find_US_trailer(movie.videos()),
            'plot': movie.overview,
            'genres': [genre_obj['name'] for genre_obj in movie.genres],
            'rating': movie.vote_average,
            'nb_of_ratings': movie.vote_count,
            'top3_cast': get_top3_cast(movie.cast),
            'shorts_urls': ig_shorts,
        } for movie, ig_shorts in zip(movies, ig_shorts_list)
    ]

    return jsonify({'results': movies_dict})



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
