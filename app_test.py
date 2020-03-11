import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from database.models import setup_db, Movie, Actor

# Using the basic testing template from the Trivia app previously built for this course.

class CapstoneTestCase(unittest.TestCase):
    """This class represents the capstone test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "capstone_dev"
        self.database_path = os.getenv('TEST_DB')
        setup_db(self.app, self.database_path)

        self.new_movie = {
            "title": "Doctor Strange",
            "release_date": "20-Oct-2016",
        }

        self.new_actor = {
            "name": "Benedict Cumberbatch",
            "gender": "male",
            "age": "43"
        }

        self.assistant_headers = {
            "Content-Type": "application/json",
            "Authorization": os.getenv('CASTING_ASST')
        }

        self.director_headers = {
            "Content-Type": "application/json",
            "Authorization":  os.getenv('CASTING_DIR')
        }

        self.producer_headers = {
            "Content-Type": "application/json",
            "Authorization":  os.getenv('EXEC_PROD')
        }

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)

    def tearDown(self):
        pass

    # Testing the GET requests.
    def test_get_movies(self):
        res = self.client().get('/api/movies', headers=self.producer_headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_get_actors(self):
        res = self.client().get('/api/actors', headers=self.producer_headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    # Testing the POST requests.
    def test_add_movie(self):
        res = self.client().post(
            '/api/movies', headers=self.producer_headers, json=self.new_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_add_actor(self):
        res = self.client().post(
            '/api/actors', headers=self.producer_headers, json=self.new_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    # Testing the PATCH requests.
    def test_edit_movie(self):
        movie = {
            "title": "The Avengers",
            "release_date": "4-May-2012",
        }
        res = self.client().patch('/api/movies/1',
                                  headers=self.producer_headers, json=movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_edit_actor(self):
        actor = {
            "name": "Robert Downey Jr",
            "gender": "male",
            "age": "54"
        }
        res = self.client().patch('/api/actors/1',
                                  headers=self.producer_headers, json=actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    # Testing the DELETE requests.
    def test_remove_movie(self):
        res = self.client().delete('/api/movies/2',
                                   headers=self.producer_headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_remove_actor(self):
        res = self.client().delete('/api/actors/2',
                                   headers=self.producer_headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    # Error testing.

    # Testing errors with GET requests.

    def test_fail_get_movies(self):
        res = self.client().get('/api/movies')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['message'], "Unauthorized client error")
        self.assertEqual(data['success'], False)

    def test_fail_get_actors(self):
        res = self.client().get('/api/actors')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['message'], "Unauthorized client error")
        self.assertEqual(data['success'], False)

    # Testing errors with POST requests.
    def test_fail_add_movie(self):
        res = self.client().post('/api/movies', json=self.new_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['message'], "Unauthorized client error")
        self.assertEqual(data['success'], False)

    def test_fail_add_actor(self):
        res = self.client().post('/api/actors', json=self.new_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['message'], "Unauthorized client error")
        self.assertEqual(data['success'], False)

    # Testing errors with PATCH requests.
    def test_fail_edit_movie(self):
        movie = {
            "title": "Not a Real Movie",
            "release_date": "11-Mar-2020",
        }
        res = self.client().patch('/api/movies/1', json=movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['message'], "Unauthorized client error")
        self.assertEqual(data['success'], False)

    def test_fail_edit_actor(self):
        actor = {
            "name": "Not Anactor",
            "gender": "male",
            "age": "29"
        }
        res = self.client().patch('/api/actors/1', json=actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['message'], "Unauthorized client error")
        self.assertEqual(data['success'], False)

    # Testing errors with DELETE requests.
    def test_fail_remove_movie(self):
        res = self.client().delete('/api/movies/2')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['message'], "Unauthorized client error")
        self.assertEqual(data['success'], False)

    def test_fail_remove_actor(self):
        res = self.client().delete('/api/actors/2')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['message'], "Unauthorized client error")
        self.assertEqual(data['success'], False)

    # Role-based access control testing

    # Casting Assistant
    # Testing GET requests
    def test_get_movies(self):
        res = self.client().get('/api/movies',
                                headers=self.assistant_headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_get_actors(self):
        res = self.client().get('/api/actors',
                                headers=self.assistant_headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    # Casting Director
    # Testing error on PATCH requests.
    def test_error_edit_a_movie(self):
        movie = {
            "title": "Not a Real Movie",
            "release_date": "11-Mar-2020",
        }
        res = self.client().patch('/api/movies/100',
                                  headers=self.director_headers, json=movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['message'], "resource not found")
        self.assertEqual(data['success'], False)

    def test_error_edit_an_actor(self):
        actor = {
            "name": "Not Anactor",
            "gender": "male",
            "age": "29"
        }
        res = self.client().patch('/api/actors/100',
                                  headers=self.director_headers, json=actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['message'], "resource not found")
        self.assertEqual(data['success'], False)

    # Executive Producer
    # Testing error on DELETE requests.
    def test_error_remove_movie(self):
        res = self.client().delete('/api/movies/500',
                                   headers=self.producer_headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['message'], "resource not found")
        self.assertEqual(data['success'], False)

    def test_error_remove_an_actor(self):
        res = self.client().delete('/api/actors/200',
                                   headers=self.producer_headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['message'], "resource not found")
        self.assertEqual(data['success'], False)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
