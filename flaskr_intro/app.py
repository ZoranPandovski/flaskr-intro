# imports
from flask import Flask, request, session, redirect, url_for, \
     abort, render_template, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
import models

# grabs the folder where the script runs
basedir = os.path.abspath(os.path.dirname(__file__))

# configuration
DATABASE = 'flaskr.db'
DEBUG = True
SECRET_KEY = 'my_precious'
USERNAME = 'admin'
PASSWORD = 'admin'

# defines the full path for the database
DATABASE_PATH = os.path.join(basedir, DATABASE)

# database config
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH
SQLALCHEMY_TRACK_MODIFICATIONS = False

# create app
app = Flask(__name__)
app.config.from_object(__name__)
db = SQLAlchemy(app)


@app.route('/')
def index():
    """Searches the database for entries, then displays them."""
    entries = db.session.query(models.Flaskr)
    return render_template('index.html', entries=entries)


@app.route('/add', methods=['POST'])
def add_entry():
    """Adds new post to the database."""
    if not session.get('logged_in'):
        abort(401)
    new_entry = models.Flaskr(request.form['title'], request.form['text'])
    db.session.add(new_entry)
    db.session.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('index'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    """User login/authentication/session management."""
    TEMPLATE = "login.html"
    if request.method != 'POST':
        return render_template(TEMPLATE, error=None)
    error = _validate_credentials(request.form)
    if error is not None:
        return render_template(TEMPLATE, error=error)

    session['logged_in'] = True
    flash('You were logged in')
    return redirect(url_for('index'))


def _validate_credentials(form_dict):
    error_msg = "Invalid username or password"
    username, password = form_dict['username'], form_dict['password']
    if (username != app.config['USERNAME'] or
            password != app.config['PASSWORD']):
        return error_msg


@app.route('/logout')
def logout():
    """User logout/authentication/session management."""
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('index'))


@app.route('/delete/<int:post_id>', methods=['GET'])
def delete_entry(post_id):
    """Deletes post from database"""
    result = {'status': 0, 'message': 'Error'}
    try:
        new_id = post_id
        db.session.query(models.Flaskr).filter_by(post_id=new_id).delete()
        db.session.commit()
        result = {'status': 1, 'message': "Post Deleted"}
        flash('The entry was deleted.')
    except Exception as e:
        result = {'status': 0, 'message': repr(e)}
    return jsonify(result)


@app.route('/search/', methods=['GET'])
def search():
    query = request.args.get("query")
    entries = db.session.query(models.Flaskr)
    if query:
        return render_template('search.html', entries=entries, query=query)
    return render_template('search.html')


if __name__ == '__main__':
    app.run()