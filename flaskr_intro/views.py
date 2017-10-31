from flask import request, session, redirect, url_for, \
    abort, render_template, flash, jsonify

from flaskr_intro import app, db
from .models import Flaskr


@app.route('/')
def index():
    """Searches the database for entries, then displays them."""
    entries = db.session.query(Flaskr)
    return render_template('index.html', entries=entries)


@app.route('/add', methods=['POST'])
def add_entry():
    """Adds new post to the database."""
    if not session.get('logged_in'):
        abort(401)
    new_entry = Flaskr(request.form['title'], request.form['text'])
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
        db.session.query(Flaskr).filter_by(post_id=new_id).delete()
        db.session.commit()
        result = {'status': 1, 'message': "Post Deleted"}
        flash('The entry was deleted.')
    except Exception as e:
        result = {'status': 0, 'message': repr(e)}
    return jsonify(result)


@app.route('/search/', methods=['GET'])
def search():
    query = request.args.get("query")
    entries = db.session.query(Flaskr)
    if query:
        return render_template('search.html', entries=entries, query=query)
    return render_template('search.html')
