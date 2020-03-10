## Getting Started

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

If operating locally, you can use the following command to restore an initial database to get started:

```bash
psql [YOUR DATABASE NAME] < capstone_init_db.psql
```

If operating off of the Heroku server, this is not necessary.

## Running the server

From within the root directory first ensure you are working using your created virtual environment.

Each time you open a new terminal session, run:

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
```

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

## Testing

Run unit tests with `python app_test.py`

The API endpoints can be tested using [Postman](https://getpostman.com). A Postman collection is included, which can be imported into Postman.

# API Documentation:

### /movies:
* Endpoint: '/api/movies'
* Arguments: None
* Method: 'GET'
* Authentication: Casting Assistant, Casting Director, Executive Producer
* Returns: Status 200, list of movies

### /actors:
* Endpoint: '/api/actors'
* Arguments: None
* Method: 'GET'
* Authentication: Casting Assistant, Casting Director, Executive Producer
* Returns: Status 200, list of actors