import unittest

from app.internal.logic.cache_init import get_cache
from tests.logic.mock_cache import delete_cache_file


class TestCache(unittest.TestCase):
    # pylint: disable=arguments-differ
    @classmethod
    def setUp(cls):
        delete_cache_file("test")

    @classmethod
    def tearDownClass(cls):
        delete_cache_file("test")

    def test_new_cache(self):
        data, _ = get_cache("https://sandbox.api.service.nhs.uk/hello-world/hello/world", "test")
        self.assertEqual(data["message"], "Hello World!")

    def test_existing_new_cache(self):
        get_cache("https://sandbox.api.service.nhs.uk/hello-world/hello/world", "test")
        data, _ = get_cache("https://sandbox.api.service.nhs.uk/hello-world/hello/world", "test")
        self.assertEqual(data["message"], "Hello World!")

    def test_existing_old_cache(self):
        with open("./app/cache/test.json", "w", encoding="utf-8") as cache_file:
            cache_file.write('{"message": "Hello World!", "timestamp": 669283135.9517488}')

        _, timestamp = get_cache("https://sandbox.api.service.nhs.uk/hello-world/hello/world", "test")
        self.assertNotEqual(timestamp, 669283135.9517488)
