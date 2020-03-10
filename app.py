import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
from models import app, Movie, Actor
from auth import AuthError, requires_auth

@app.route('/movies')
@cross_origin()
@requires_auth('get:movies')
def get_movies(jwt):
      movies = Movie.query.all()
      print(movies)
      try:
            movies = [movie.format() for movie in movies]

            return jsonify({
                  'success': True,
                  'movies': movies
            }), 200
      
      except Exception:
            abort(500)

@app.route('/actors', methods=['GET'])
@requires_auth('get:actors')
def get_actors(jwt):
      actors = Actor.query.all()

      if len(actors) <= 0:
            abort(404)
      
      return jsonify({
      'success': True,
      'actors': actors
      }), 200

@app.route('/movies', methods=['POST'])
@requires_auth('post:movies')
def new_movie(jwt):
      movie_data = request.get_json()
      if "title" and "release_date" not in movie_data:
            abort(422)
      
      title = movie_data['title']
      release_date = movie_data['release_date']

      new_movie = Movie(title=title, release_date=release_date)
      new_movie.insert()

@app.route('/actors', methods=['POST'])
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

@app.route('/movies/<int:movie_id>', methods=['PATCH'])
@requires_auth('patch:movies')
def update_movie(jwt, movie_id):
      current_movie_data = Movie.query.get(movie_id)
      new_movie_data = request.get_json()

      if current_movie_data is None:
            abort(404)

      if "title" in new_movie_data:
            current_movie_data.title = new_movie_data['title']
      
      if "release_date" in new_movie_data:
            current_movie_data.release_date = new_movie_data['release_date']

      current_movie_data.update()

      return jsonify({
      'success': True
      })

@app.route('/actors/<int:actor_id>', methods=['PATCH'])
@requires_auth('patch:actors')
def update_actor(jwt, actor_id):
      current_actor_data = Actor.query.get(actor_id)
      new_actor_data = request.get_json()

      if "name" in new_actor_data:
            current_actor_data.name = new_actor_data['name']
      
      if "age" in new_actor_data:
            current_actor_data.age = new_actor_data['age']
      
      if "gender" in new_actor_data:
            current_actor_data.gender = new_actor_data['gender']

      current_actor_data.update()

      return jsonify({
      'success': True
      })

@app.route('/movies/<int:movie_id>', methods=['DELETE'])
@requires_auth('delete:movies')
def remove_movie(jwt, movie_id):
      movie = Movie.query.get(movie_id)

      if movie is None:
            abort(404)
      
      movie.delete()

      return jsonify({
      'success': True,
      'delete': movie_id
      })

@app.route('/actors/<int:actor_id>', methods=['DELETE'])
@requires_auth('delete:actors')
def remove_actor(jwt, actor_id):
      actor = Actor.query.get(actor_id)

      if actor is None:
            abort(404)
      
      actor.delete()

      return jsonify({
      'success': True,
      'delete': actor_id
      })

# Registering error handlers for the application. (204, 422, 404 and an AuthError)
@app.errorhandler(404)
def data_missing(error):
      return jsonify({
      "success": False,
      "error": 404,
      "message": "No data available."
      })

@app.errorhandler(422)
def invalid_data(error):
      return jsonify({
      "success": False,
      "error": 422,
      "message": "The data provided was not formatted correctly."
      })

@app.errorhandler(AuthError)
def authentication_error(error, status):
      return jsonify({
      'success': False,
      'error': error,
      'status': status
      })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)