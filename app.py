import os
import sys
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS, cross_origin
from database.models import db_drop_and_create_all, setup_db, Movie, Actor
from authentication.auth import AuthError, requires_auth

# API documentation is available in README.md

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    setup_db(app)
    # Setting up CORS.
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,POST,PATCH,PUT,DELETE,OPTIONS')
        return response

    '''
      The below function call will reset the database.
    '''
    # db_drop_and_create_all()

    @app.route('/api/movies')
    @cross_origin()
    @requires_auth('get:movies')
    def get_movies(jwt):
        movies = Movie.query.all()
        
        try:
            all_movies = [movie.format() for movie in movies]

            return jsonify({
                'success': True,
                'movies': all_movies
            }), 200
        except Exception:
            abort(500)

    @app.route('/api/actors')
    @cross_origin()
    @requires_auth('get:actors')
    def get_actors(jwt):
        actors = Actor.query.all()
        try:
            all_actors = [actor.format() for actor in actors]

            return jsonify({
                'success': True,
                'actors': all_actors
            }), 200
        except Exception:
            abort(500)

    @app.route('/api/movies', methods=['POST'])
    @cross_origin()
    @requires_auth('post:movies')
    def new_movie(jwt):
        movie_data = request.get_json()
        print(json.dumps(movie_data), file=sys.stdout)

        #movie = movie_data.get('movie')

        movie = Movie(
            title=movie_data.get('title'),
            release_date=movie_data.get('release_date')
        )

        try:
            movie.insert()
        except:
            abort(400)
        
        movies = Movie.query.all()
        try:
            movies = [movie.format() for movie in movies]

            return jsonify({
                'success': True,
                'movies': movies
            }), 200
        except Exception:
            abort(500)

    @app.route('/api/actors', methods=['POST'])
    @cross_origin()
    @requires_auth('post:actors')
    def post_actor(jwt):
        actor_data = request.get_json()

        actor = actor_data.get('actor')

        actor = Actor(
            name=actor_data.get('name'),
            age=actor_data.get('age'),
            gender=actor_data.get('gender')
        )
        # Problem seems to be here. When executing a POST request, I receive the 400 error.
        try:
            actor.insert()

            actors = Actor.query.all()
            actors = [actor.format() for actor in actors]

            return jsonify({
                'success': True,
                'actors': actors
            }), 200
        except Exception:
            abort(400)

    @app.route('/api/movies/<int:id>', methods=['PATCH'])
    @cross_origin()
    @requires_auth('patch:movies')
    def patch_movie(jwt, id):
        movie = Movie.query.filter(Movie.id == id)

        if movie is None:
            abort(404)

        new_movie_data = request.get_json()

        title = new_movie_data.get('title')
        release_date = new_movie_data.get('release_date')

        try:
            movie.title = title
            movie.release_date = release_date
            movie.update()

            movies = Movie.query.all()
            movies = [movie.format() for movie in movies]

            return jsonify({
                'success': True,
                'movies': movies
            }), 200
        except Exception:
            abort(422)

    @app.route('/api/actors/<int:id>', methods=['PATCH'])
    @cross_origin()
    @requires_auth('patch:actors')
    def patch_actor(jwt, id):
        actor = Actor.query.filter(Actor.id == id)

        if actor is None:
            abort(404)

        new_actor_data = request.get_json()

        name = new_actor_data.get('name')
        age = new_actor_data.get('age')
        gender = new_actor_data.get('gender')

        try:
            actor.name = name
            actor.age = age
            actor.gender = gender
            actor.update()

            actors = Actor.query.all()
            actors = [actor.format() for actor in actors]

            return jsonify({
                'success': True,
                'actors': actors
            }), 200
        except Exception:
            abort(422)

    @app.route('/api/movies/<int:id>', methods=['DELETE'])
    @cross_origin()
    @requires_auth('delete:movies')
    def delete_movie(jwt, id):
        movie = Movie.query.filter(Movie.id == id)

        if movie is None:
            abort(404)

        try:
            movie.delete()

            movies = Movie.query.all()
            movies = [movie.format() for movie in movies]

            return jsonify({
                'success': True,
                'movies': movies
            }), 200
        except Exception:
            abort(422)

    @app.route('/api/actors/<int:id>', methods=['DELETE'])
    @cross_origin()
    @requires_auth('delete:actors')
    def delete_actor(jwt, id):
        actor = Actor.query.filter(Actor.id == id)

        if actor is None:
            abort(404)

        try:
            actor.delete()

            actors = Actor.query.all()
            actors = [actor.format() for actor in actors]

            return jsonify({
                'success': True,
                'actors': actors
            }), 200
        except Exception:
            abort(422)

    # All available error handlers:
    @app.errorhandler(400)
    def failed_req(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "request failed",
        }), 400

    @app.errorhandler(AuthError)
    def unauthorized_request(error):
        return jsonify({
            "success": False,
            "error": 401,
            "message": "Unauthorized client error",
        }), 401

    @app.errorhandler(401)
    def unauthorized_req(error):
        return jsonify({
            "success": False,
            "error": 401,
            "message": "Unauthorized client error",
        }), 401

    @app.errorhandler(403)
    def forbidden_req(error):
        return jsonify({
            "success": False,
            "error": 403,
            "message": "Forbidden request. Please contact your administrator.",
        }), 403

    @app.errorhandler(404)
    def notfound(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found",
        }), 404
        
    @app.errorhandler(422)
    def unprocessable_req(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable request",
        }), 422

    @app.errorhandler(500)
    def server_err(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "Internal server error.",
        }), 500

    return app


app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
