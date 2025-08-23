from unittest import TestCase
from mission_01_hello_world.solution import hello_world

class TestHelloWorld(TestCase):
    def test_hello_world(self):
        expected_output = "Hello, World!"
        self.assertEqual(hello_world(), expected_output)