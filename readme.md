<h1 align="center">
	<img width="400" src="media/flask.png" alt="Flask">
	<br>
	<br>
</h1>

[![Build Status](https://img.shields.io/travis/ZoranPandovski/flaskr-intro/master.svg?logo=travis)](https://travis-ci.org/ZoranPandovski/flaskr-intro)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/233b50af58204263b7f7424f660d02ff)](https://app.codacy.com/app/ZoranPandovski/flaskr-intro?utm_source=github.com&utm_medium=referral&utm_content=ZoranPandovski/flaskr-intro&utm_campaign=badger)
[![BCH compliance](https://bettercodehub.com/edge/badge/ZoranPandovski/flaskr-intro?branch=master)](https://bettercodehub.com/)
[![Coverage Status](https://coveralls.io/repos/github/ZoranPandovski/flaskr-intro/badge.svg?branch=master)](https://coveralls.io/github/ZoranPandovski/flaskr-intro?branch=master)
[![Known Vulnerabilities](https://snyk.io/test/github/ZoranPandovski/flaskr-intro/badge.svg?targetFile=requirements.txt)](https://snyk.io/test/github/ZoranPandovski/flaskr-intro?targetFile=requirements.txt)
[![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT)
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/ZoranPandovski/flaskr-intro/issues)

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

