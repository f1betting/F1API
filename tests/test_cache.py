import os
import unittest

from app.internal.logic.cache_init import get_cache


class TestCache(unittest.TestCase):
    @classmethod
    def setUp(cls):
        if os.path.exists("./app/cache/test.json"):
            os.remove("./app/cache/test.json")
            print("Deleted test.json")

    @classmethod
    def tearDownClass(cls):
        if os.path.exists("./app/cache/test.json"):
            os.remove("./app/cache/test.json")
            print("Deleted test.json")

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
