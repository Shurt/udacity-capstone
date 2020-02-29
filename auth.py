import json
from flask import request, _request_ctx_stack, abort
from functools import wraps
from jose import jwt
from urllib.request import urlopen
import logging
from logging import FileHandler, Formatter
import sys

AUTH0_DOMAIN = 'udacity-capstone.auth0.com'
ALGORITHMS = ['RS256']
API_AUDIENCE = 'udacity-capstone'
CLIENT_ID = '01FyP6UAoNkj0ecDPd4q6acM4FPlU1RI'

