import unittest
from datetime import datetime
from freezegun import freeze_time

from hello_word_with_day import app
from hello_word_with_day import GREETINGS

class TestHelloWorld(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.base_url = '/hello-world/'

    def test_can_get_correct_username_with_weekdate(self):
        username = 'username'
        weekday = datetime.today().weekday()
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        self.assertTrue(username in response_text)
        self.assertNotEqual(username, GREETINGS[weekday])

    @freeze_time("2025-04-14")
    def test_monday(self):
        weekday = datetime.today().weekday()
        response = self.app.get(self.base_url + 'username')
        response_text = response.data.decode()
        self.assertTrue(GREETINGS[weekday] in response_text)

    @freeze_time("2025-04-15")
    def test_tuesday(self):
        weekday = datetime.today().weekday()
        response = self.app.get(self.base_url + 'username')
        response_text = response.data.decode()
        self.assertTrue(GREETINGS[weekday] in response_text)

    @freeze_time("2025-04-16")
    def test_wednesday(self):
        weekday = datetime.today().weekday()
        response = self.app.get(self.base_url + 'username')
        response_text = response.data.decode()
        self.assertTrue(GREETINGS[weekday] in response_text)

    @freeze_time("2025-04-17")
    def test_thursday(self):
        weekday = datetime.today().weekday()
        response = self.app.get(self.base_url + 'username')
        response_text = response.data.decode()
        self.assertTrue(GREETINGS[weekday] in response_text)

    @freeze_time("2025-04-18")
    def test_friday(self):
        weekday = datetime.today().weekday()
        response = self.app.get(self.base_url + 'username')
        response_text = response.data.decode()
        self.assertTrue(GREETINGS[weekday] in response_text)

    @freeze_time("2025-04-19")
    def test_saturday(self):
        weekday = datetime.today().weekday()
        response = self.app.get(self.base_url + 'username')
        response_text = response.data.decode()
        self.assertTrue(GREETINGS[weekday] in response_text)

    @freeze_time("2025-04-20")
    def test_sunday(self):
        weekday = datetime.today().weekday()
        response = self.app.get(self.base_url + 'username')
        response_text = response.data.decode()
        self.assertTrue(GREETINGS[weekday] in response_text)
