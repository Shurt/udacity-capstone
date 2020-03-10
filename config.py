import os
'''

Use the below variables to configure the application's connection to the database.

'''

SECRET_KEY = os.urandom(32)
DEBUG = True

'''

=== Shouldn't need to edit below this line ===

'''

#SQLALCHEMY_DATABASE_URI = "postgres://{}:{}@{}/{}".format(DB_USER, DB_PASS, DB_HOST_PORT, DB_NAME)
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
SQLALCHEMY_TRACK_MODIFICATIONS = False 
#