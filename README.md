# Flaskr

Flaskr is a mini blog application that you are building following the official [Flask tutorial](http://flask.pocoo.org/docs/0.12/tutorial/introduction/). The app essentially, will do the following things:

* Let the user sign in and out with credentials specified in the configuration. Only one user is supported.
* When the user is logged in, they can add new entries to the page consisting of a text-only title and some HTML for the text.   This HTML is not sanitized because we trust the user here.
* The index page shows all entries so far in reverse chronological order (newest on top) and the user can add new ones from       there if logged in.

There is another great tutorial for flask and tdd at https://realpython.com/

To run the application, open up a command prompt (on Windows) and type in the following: 

1. `set FLASK_APP=server.py`
2. `set FLASK_DEBUG=1`
3. `flask initdb`
4. `flask run`

To test the application, from the root folder run: `python test_flaskr.py`

