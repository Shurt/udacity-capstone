import os
import sys
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS, cross_origin
from database.models import db_drop_and_create_all, setup_db, Movie, Actor
from authentication.auth import AuthError, requires_auth

# API documentation is available in README.md.

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
    #db_drop_and_create_all()

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

        if "title" and "release_date" not in movie_data:
            abort(422)

        title = movie_data['title']
        release_date = movie_data['release_date']

        new_movie = Movie(title=title, release_date=release_date)
        new_movie.insert()

        return jsonify({
              "success": True,
              "new_movie": new_movie.format()
        })

    @app.route('/api/actors', methods=['POST'])
    @cross_origin()
    @requires_auth('post:actors')
    def new_actor(jwt):
        actor_data = request.get_json()

        if "name" and "age" and "gender" not in actor_data:
            abort(422)

        name = actor_data['name']
        age = actor_data['age']
        gender = actor_data['gender']

        new_actor = Actor(name=name, age=age, gender=gender)
        new_actor.insert()

        return jsonify({
            'success': True,
            'actors': new_actor.format()
        }), 200

    @app.route('/api/movies/<int:movie_id>', methods=['PATCH'])
    @cross_origin()
    @requires_auth('patch:movies')
    def patch_movie(jwt, movie_id):
        movie = Movie.query.get(movie_id)
        new_movie_data = request.get_json()

        if movie is None:
            abort(404)
        
        if 'title' in new_movie_data:
            movie.title = new_movie_data['title']
        
        if 'release_date' in new_movie_data:
            movie.release_date = new_movie_data['release_date']

        try:
            movie.update()

            return jsonify({
                'success': True,
                'movie': movie.format()
            }), 200
        except Exception:
            abort(422)

    @app.route('/api/actors/<int:actor_id>', methods=['PATCH'])
    @cross_origin()
    @requires_auth('patch:actors')
    def patch_actor(jwt, actor_id):
        actor = Actor.query.get(actor_id)
        new_actor_data = request.get_json()

        if actor is None:
            abort(404)

        if 'name' in new_actor_data:
            actor.name = new_actor_data['name']

        if 'age' in new_actor_data:
            actor.age = new_actor_data['age']

        if 'gender' in new_actor_data:
            actor.gender = new_actor_data['gender']
        try:
            actor.update()

            return jsonify({
                'success': True,
                'actors': actor.format()
            }), 200
        except Exception:
            abort(422)

    @app.route('/api/movies/<int:movie_id>', methods=['DELETE'])
    @cross_origin()
    @requires_auth('delete:movies')
    def delete_movie(jwt, movie_id):
        movie = Movie.query.get(movie_id)

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

    @app.route('/api/actors/<int:actor_id>', methods=['DELETE'])
    @cross_origin()
    @requires_auth('delete:actors')
    def delete_actor(jwt, actor_id):
        actor = Actor.query.get(actor_id)

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
