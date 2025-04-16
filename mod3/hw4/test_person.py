import unittest
from person import Person

class TestPerson(unittest.TestCase):
    def setUp(self):
        self.person = Person('Artemy', 2000, 'Ekaterinburg')

    def test_get_age(self):
        self.assertEquals(self.person.get_age(), 25)

    def test_get_name(self):
        self.assertEquals(self.person.get_name(), 'Artemy')

    def test_set_name(self):
        self.person.set_name('Alex')
        self.assertEquals(self.person.get_name(), 'Alex')

    def test_set_address(self):
        self.person.set_address('London')
        self.assertEquals(self.person.get_address(), 'London')

    def test_is_homeless(self):
        self.person.set_address('')
        self.assertEquals(self.person.is_homeless(), True)
