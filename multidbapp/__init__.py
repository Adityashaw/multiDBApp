"""
Flask main Module
DB Connection is established here
Routes are defined in views.py
"""

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session  # helps to store session at back-end
from sassutils.wsgi import SassMiddleware


app = Flask(__name__)

# Only for development
# Do NOT use at production
# This will automatically convert sass file to equivalent css file whenever file changes
app.wsgi_app = SassMiddleware(app.wsgi_app, {
    'multidbapp': ('static/sass', 'static/css', 'static/css')
    })  # noqa: E123


# DB URL will be in env
# No need to change every time here
# Check for environment variable
if not os.getenv("DATABASE_URL_MYSQL"):
    raise RuntimeError("DATABASE_URL_MYSQL is not set")
if not os.getenv("DATABASE_URL_POSTGRESQL"):
    raise RuntimeError("DATABASE_URL_POSTGRESQL is not set")

# Configure session to use filesystem
# app.config["SESSION_PERMANENT"] = False  # I don't remember what this does
app.config["SESSION_TYPE"] = "filesystem"

# Cookies older than 15min is rejected
app.config['PERMANENT_SESSION_LIFETIME'] = 15 * 60

# db url from env
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL_MYSQL")
app.config['SQLALCHEMY_BINDS'] = {
    'students': os.getenv("DATABASE_URL_POSTGRESQL")
}
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# for sql debug only
app.config['SQLALCHEMY_ECHO'] = bool(os.getenv("SQLALCHEMY_ECHO", default=False))

# initialize SQLAlchemy db
db = SQLAlchemy(app)


# This key is committed and is unsecure. Get key from env.
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

# Session will be stored in back-end, less data to transfer
Session(app)

import multidbapp.views  # noqa: E402, F401
# app.run(host='127.0.0.1', port=5000, debug=True)
