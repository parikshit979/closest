import unittest
from app import app


class TestIntegrations(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_thing(self):
        response = self.app.get('/')


if __name__ == '__main__':
    unittest.main()
