from flask import Flask

counting = Flask(__name__)
from counting import views
