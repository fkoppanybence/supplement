from app import home
from flask import render_template, Flask
app = Flask(__name__)

@app.route('/')
def test_home():
    with app.app_context():
        assert home() == render_template('home.html',val='')