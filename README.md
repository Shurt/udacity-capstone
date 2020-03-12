# Getting Started

Below are the URLs associated with the project:

**Heroku URL: https://udacitycapstone.herokuapp.com/**
**Auth0 URL: https://udacity-capstone.auth0.com**

## Project Motivation

This project serves as the culmination of the Udacity Full-Stack Nanodegree program. I've utilized the suggested 'Casting Agency' project. Through this, I've utilized the following tools/concepts:
* Database modeling, using SQLAlchemy to interface to the PostgreSQL database.
* Basic API implemented to perform CRUD operations against the PostgreSQL database.
* Role-Based access control implemented with Auth0.
* Project successfully deployed to Heroku.
* Unit tests (via ```unittest```) and API tests (via [Postman](https://getpostman.com))

## Local setup

1) Firstly, clone the repo:
```bash
git clone https://github.com/Shurt/udacity-capstone
cd udacity-capstone
```

2) Initialize a new virtual environment:
```bash
python3 -m venv .env
source .env/bin/activate
```

3) Install the dependencies:
```bash
pip install -r requirements.txt
```

4) Replace the 'user name', 'password', 'database', and 'port' fields in the command below and execute it with bash:
```bash
psql [DATABASE] < capstone_init_db.psql
export DATABASE_URL="postgres://[USERNAME]:[PASSWORD]@localhost:[PORT]/[DATABASE]"
export TEST_DB="postgres://[USERNAME]:[PASSWORD]@localhost:[PORT]/[DEVELOPMENT DATABASE]"
```

## Running the server

From within the root directory first ensure you are working using your created virtual environment.

Each time you open a new terminal session, run:

```bash
chmod +x setup.sh
./setup.sh
```

To run the Flask server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

## Testing

Run unit tests with `python app_test.py`

The API endpoints can be tested using [Postman](https://getpostman.com). A Postman collection is included, which can be imported into Postman.

While testing, you can log in ([via Auth0](udacity-capstone.auth0.com)) with the following accounts:
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

