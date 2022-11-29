import json
import os
import time
import unittest

from fastapi.testclient import TestClient

from app.main import app
from tests.mock_data.mock_general import get_test_data


class TestGeneral(unittest.TestCase):
    @classmethod
    def setUpTest(cls):
        """
        Init hello world response
        :return: timestamp
        """

        if os.path.exists("./app/cache/test.json"):
            os.remove("./app/cache/test.json")
            print("Deleted test.json")

        timestamp = float(time.time())

        max_verstappen_data = get_test_data(timestamp)

        full_path = "./app/cache/test.json"

        cache_file = open(full_path, "w+")
        cache_file.write(json.dumps(max_verstappen_data))
        cache_file.close()

        return timestamp

    @classmethod
    def tearDownClass(cls):
        files = [
            "test"
        ]

        for file in files:
            if os.path.exists(f"./app/cache/{file}.json"):
                os.remove(f"./app/cache/{file}.json")
                print(f"Deleted {file}.json")

    @classmethod
    def setUpClass(cls):
        cls.test_client = TestClient(app, base_url="http://127.0.0.1:8000")

    #########
    # /test #
    #########

    def test_test(self):
        """
        Test 200 response on /test endpoint
        """

        timestamp = self.setUpTest()

        res = self.test_client.get("/test").json()

        data = get_test_data(timestamp)

        self.assertEqual(res, data)
