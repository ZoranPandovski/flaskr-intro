import os
import unittest

from unittest.mock import patch, Mock

from flask import json

from flaskr_intro import app, db
from flaskr_intro.models import Flaskr

TEST_DB = 'test.db'
basedir = os.path.abspath(os.path.dirname(__file__))
APP_NAME = "flaskr_intro"
APP_DB = "flaskr.db"
DB_PATH = os.path.join(basedir, APP_NAME, APP_DB)


class FlaskrModelTestCase(unittest.TestCase):

    def test_can_create_a_model(self):
        model = Flaskr('a title', 'some text')

        self.assertEqual(model.title, 'a title')
        self.assertEqual(model.text, 'some text')
        self.assertEqual(str(model), '<title: a title>')


class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        """Set up a blank temp database before each test"""
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
                                                os.path.join(basedir, TEST_DB)
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        """Destroy blank temp database after each test"""
        db.drop_all()

    def login(self, username, password):
        """Login helper function"""
        return self.app.post('/login', data=dict(
            username=username,
            password=password
        ), follow_redirects=True)

    def logout(self):
        """Logout helper function"""
        return self.app.get('/logout', follow_redirects=True)

    # assert functions

    def test_index(self):
        """initial test. ensure flask was set up correctly"""
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_database(self):
        """initial test. ensure that the database exists"""
        tester = os.path.exists("test.db")
        self.assertTrue(tester)

    def test_empty_db(self):
        """Ensure database is blank"""
        rv = self.app.get('/')
        self.assertIn(b'No entries yet. Add some!', rv.data)

    def test_login_logout(self):
        """Test login and logout using helper functions"""
        rv = self.login(app.config['USERNAME'], app.config['PASSWORD'])
        self.assertIn(b'You were logged in', rv.data)
        rv = self.logout()
        self.assertIn(b'You were logged out', rv.data)
        rv = self.login(app.config['USERNAME'] + 'x', app.config['PASSWORD'])
        self.assertIn(b'Invalid username', rv.data)
        rv = self.login(app.config['USERNAME'], app.config['PASSWORD'] + 'x')
        self.assertIn(b'Invalid username or password', rv.data)

    def test_messages(self):
        """Ensure that user can post messages"""
        self.login(app.config['USERNAME'], app.config['PASSWORD'])
        rv = self.app.post('/add', data=dict(
            title='<Hello>',
            text='<strong>HTML</strong> allowed here'
        ), follow_redirects=True)
        self.assertNotIn(b'No entries here so far', rv.data)
        self.assertIn(b'&lt;Hello&gt;', rv.data)
        self.assertIn(b'<strong>HTML</strong> allowed here', rv.data)

    def test_delete_message(self):
        """Ensure the messages are being deleted"""
        rv = self.app.get('/delete/1')
        data = json.loads(rv.data)
        self.assertEqual(data['status'], 1)
        self.assertEqual(data['message'], 'Post Deleted')

    @patch('flaskr_intro.views.db')
    def test_delete_message_can_fail(self, db_mock):
        """Ensure the messages are being deleted"""
        db_mock.session.query = Mock(side_effect=Exception('Some message'))

        rv = self.app.get('/delete/1')
        data = json.loads(rv.data)
        self.assertEqual(data['status'], 0)
        self.assertEqual(data['message'], "Exception('Some message',)")

    def test_post_fail_without_login(self):
        """Ensure anonymous users can't make blog post"""
        rv = self.app.post('/add', data=dict(
            title='<Hello>',
            text='<strong>HTML</strong> allowed here'
        ), follow_redirects=True)
        self.assertIn(b'Unauthorized', rv.data)

    def test_post_fail_with_invalid_login(self):
        """Ensure anonymous users can't make blog post"""
        self.login(app.config['USERNAME'] + 'x', app.config['PASSWORD'])
        rv = self.app.post('/add', data=dict(
            title='<Hello>',
            text='<strong>HTML</strong> allowed here'
        ), follow_redirects=True)
        self.assertIn(b'Unauthorized', rv.data)

    @patch('flaskr_intro.views.db')
    def test_search_message(self, mock_db):
        """Ensure the messages are being deleted"""
        entries = [
            Flaskr('entry1', 'text'),
            Flaskr('entry2', 'text')
        ]
        mock_db.session.query = Mock(return_value=entries)

        rv = self.app.get('/search/')

        mock_db.session.query.assert_called_once()

        self.assertIn(b'<!DOCTYPE html>', rv.data)

    @patch('flaskr_intro.views.db')
    def test_search_message_with_query(self, mock_db):
        """Ensure the messages are being deleted"""
        entries = [
            Flaskr('entry1', 'text'),
            Flaskr('entry2', 'text')
        ]
        mock_db.session.query = Mock(return_value=entries)

        rv = self.app.get('/search/?query=Hello')

        mock_db.session.query.assert_called_once()

        self.assertIn(b'<!DOCTYPE html>', rv.data)


if __name__ == '__main__':
    unittest.main()
