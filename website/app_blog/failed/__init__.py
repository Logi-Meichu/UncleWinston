from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from config import Config
import os
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config.from_object(Config)

bootstrap = Bootstrap(app)
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)

from app_blog.blog import view