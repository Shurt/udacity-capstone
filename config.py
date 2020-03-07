'''

Use the below variables to configure the application's connection to the database.

'''

DB_NAME = 'casting-agency'
DB_HOST_PORT = 'localhost:5433'
DB_USER = "capstone"
DB_PASS = "test123"

DEBUG = True

'''

=== Shouldn't need to edit below this line ===

'''

SQLALCHEMY_DATABASE_URI = "postgres://{}:{}@{}/{}".format(DB_USER, DB_PASS, DB_HOST_PORT, DB_NAME)
SQLALCHEMY_TRACK_MODIFICATIONS = False 