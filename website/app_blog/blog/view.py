from app_blog import app
from flask import render_template

@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generic')
def generic():
    return render_template('generic.html')

@app.route('/elements')
def elements():
    return render_template('elements.html')

@app.route('/djshow')
def djshow():
    return render_template('djshow.html')