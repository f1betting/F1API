import os
import unittest

from fastapi.testclient import TestClient

from app.main import app
from tests.logic.mock_cache import mock_cache
from tests.mock_data.mock_general import get_test_data


class TestGeneral(unittest.TestCase):
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
        cls.test_client = TestClient(app)

    #########
    # /test #
    #########

    def test_test(self):
        """
        Test 200 response on /test endpoint
        """

        timestamp = mock_cache(get_test_data, "test")

        res = self.test_client.get("/test").json()

        data = get_test_data(timestamp)

        self.assertEqual(res, data)
