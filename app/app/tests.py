from django.test import TestCase
from app.test_example import add, subtract


class ExampleTest(TestCase):

    def test_add_numbers(self):
        """ Test example :: add function """
        self.assertEqual(add(1, 3), 4)

    def test_substract_numbers(self):
        """ Test example :: subtract function """
        self.assertEqual(subtract(11, 5), 6)
