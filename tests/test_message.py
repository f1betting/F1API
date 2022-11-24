import unittest

from app.internal.models.general.message import create_message


class TestModels(unittest.TestCase):
    def test_message(self):
        data = create_message("test")
        self.assertEqual(data, {"message": "test"})
