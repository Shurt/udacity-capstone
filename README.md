## Getting Started

Heroku URL: https://udacitycapstone.herokuapp.com/

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

I recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the root directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

## Database Setup

If operating locally, you can use the following commands to restore an initial database to get started:

```bash
psql [YOUR DATABASE NAME] < capstone_init_db.psql
export DATABASE_URL="postgres://[POSTGRES USERNAME HERE]:[POSTGRES PASSWORD HERE]@127.0.0.1:5432/[YOUR DATABASE NAME]"
export TEST_DB="postgres://[POSTGRES USERNAME HERE]:[POSTGRES PASSWORD HERE]@127.0.0.1:5432/[YOUR DATABASE NAME]"
```

Alternatively, if you create two empty databases, "capstone_prod" and "capstone_dev", you can run the following script (you must first update the username/password for psql):

```bash
chmod +x database_setup.sh
./database_setup.sh
export DATABASE_URL="postgres://[POSTGRES USERNAME HERE]:[POSTGRES PASSWORD HERE]@127.0.0.1:5432/capstone_prod"
export TEST_DB="postgres://[POSTGRES USERNAME HERE]:[POSTGRES PASSWORD HERE]@127.0.0.1:5432/capstone_dev"
```

If operating off of the Heroku server, this is not necessary.

## Running the server

From within the root directory first ensure you are working using your created virtual environment.

Each time you open a new terminal session, run:

```bash
chmod +x setup.sh
./setup.sh
```

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

## Testing

Run unit tests with `python app_test.py`

The API endpoints can be tested using [Postman](https://getpostman.com). A Postman collection is included, which can be imported into Postman.

While testing, you can log in (via Auth0) with the following accounts:
casting_asst@shurt.net / Blah123!
casting_dir@shurt.net / Blah123!
exec_prod@shurt.net / Blah123!

# API Documentation:

### /api/movies:
* Endpoint: '/api/movies'
* Arguments: None
* Method: 'GET'
* Authentication: Casting Assistant, Casting Director, Executive Producer
* Returns: Status 200, list of movies

### /api/actors:
* Endpoint: '/api/actors'
* Arguments: None
* Method: 'GET'
* Authentication: Casting Assistant, Casting Director, Executive Producer
* Returns: Status 200, list of actors

### /api/movies:
* Endpoint: '/api/movies'
* Arguments: JSON (title, release_date) of new movie.
* Method: 'POST'
* Authentication: Casting Director, Executive Producer
* Returns: Status 200, list of movies

### /api/actors:
* Endpoint: '/api/actors'
* Arguments: JSON (name, age, gender) of new actor.
* Method: 'POST'
* Authentication: Casting Director, Executive Producer
* Returns: Status 200, list of actors

### /api/movies/<int: movie_id>:
* Endpoint: '/api/movies/[movie_id]'
* Arguments: JSON (title, release_date) of updated movie.
* Method: 'PATCH'
* Authentication: Casting Director, Executive Producer
* Returns: Status 200, list of movies

### /api/actors/<int: actor_id>:
* Endpoint: '/api/actors/[actor_id]'
* Arguments: JSON (name, age, gender) of updated actor.
* Method: 'PATCH'
* Authentication: Casting Director, Executive Producer
* Returns: Status 200, list of actors

### /api/movies/<int: movie_id>:
* Endpoint: '/api/movies/[movie_id]'
* Arguments: JSON (movie_id) of movie to be deleted.
* Method: 'DELETE'
* Authentication: Executive Producer
* Returns: Status 200, list of movies

### /api/actors/<int: actor_id>:
* Endpoint: '/api/actors/[actor_id]'
* Arguments: JSON (actor_id) of actor to be deleted.
* Method: 'DELETE'
* Authentication: Executive Producer
* Returns: Status 200, list of actors

