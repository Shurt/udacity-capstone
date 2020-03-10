import os
'''

Use the below variables to configure the application's connection to the database.

'''

SECRET_KEY = os.urandom(32)

DB_NAME = 'de4k836bjguseh'
DB_HOST_PORT = 'ec2-52-203-160-194.compute-1.amazonaws.com:5432/'
DB_USER = "capstone"
DB_PASS = "test123"

DEBUG = True

'''

=== Shouldn't need to edit below this line ===

'''

#SQLALCHEMY_DATABASE_URI = "postgres://{}:{}@{}/{}".format(DB_USER, DB_PASS, DB_HOST_PORT, DB_NAME)
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
SQLALCHEMY_TRACK_MODIFICATIONS = False 
#