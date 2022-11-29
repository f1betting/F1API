import unittest

from fastapi.testclient import TestClient

from app.main import app
from tests.logic.mock_cache import mock_cache, empty_cache_data, delete_cache_file
from tests.mock_data.constructors import get_red_bull_data, get_placeholder_data, get_red_bull_response


class TestConstructors(unittest.TestCase):
    @classmethod
    def tearDownClass(cls):
        files = [
            "get_constructor_by_id.placeholder",
            "get_constructor_by_id.red_bull",
            "get_constructors",
            "get_constructors_by_season.0",
            "get_constructors_by_season.2022",
            "get_constructors_by_season.9999"
        ]

        for file in files:
            delete_cache_file(file)

    @classmethod
    def setUpClass(cls):
        cls.test_client = TestClient(app, base_url="http://127.0.0.1:8000")

    #####################
    # /constructor/{id} #
    #####################

    def test_constructor_by_id(self):
        """
        Test 200 response on /constructor/{id} endpoint with red_bull as example
        """

        timestamp = mock_cache(get_red_bull_data, "get_constructor_by_id.red_bull")

        res = self.test_client.get("/constructor/red_bull").json()

        data = get_red_bull_response(timestamp)

        self.assertEqual(res, data)

    def test_constructor_by_id_404(self):
        """
        Test 404 response on /constructor/{id} endpoint with placeholder as example
        """

        mock_cache(get_placeholder_data, "get_constructor_by_id.placeholder")

        res = self.test_client.get("/constructor/placeholder").status_code

        self.assertEqual(res, 404)

    def test_constructor_by_id_503(self):
        """
        Test 503 response on /constructor/{id} endpoint with red_bull as example
        """

        mock_cache(empty_cache_data, "get_constructor_by_id.red_bull")

        res = self.test_client.get("/constructor/red_bull").status_code

        self.assertEqual(res, 503)

    ########################
    # /constructors/{season} #
    ########################

    def test_constructors_by_season(self):
        mock_cache(get_red_bull_data, "get_constructors_by_season.2022")

        res = self.test_client.get("/constructors/2022").json()

        constructors_data = next(
            constructor for constructor in res["constructors"] if constructor["constructorId"] == "red_bull"
        )

        data = get_red_bull_response()

        self.assertEqual(constructors_data, data)

    def test_constructors_by_season_404(self):
        """
        Test 404 response on /constructors/{season} endpoint with 9999 as example
        """

        mock_cache(get_placeholder_data, "get_constructors_by_season.9999")

        res = self.test_client.get("/constructors/9999").status_code

        self.assertEqual(res, 404)

    def test_constructor_by_season_503(self):
        """
        Test 503 response on /constructors/{season} endpoint with 0 as example
        """

        mock_cache(empty_cache_data, "get_constructors_by_season.0")

        res = self.test_client.get("/constructors/0").status_code

        self.assertEqual(res, 503)

    #############
    # /constructors #
    #############

    def test_constructors(self):
        mock_cache(get_red_bull_data, "get_constructors")

        res = self.test_client.get("/constructors").json()

        constructor_data = next(
            constructor for constructor in res["constructors"] if constructor["constructorId"] == "red_bull"
        )

        data = get_red_bull_response()

        self.assertEqual(constructor_data, data)

    def test_constructors_404(self):
        """
        Test 404 response on /constructors
        """

        mock_cache(get_placeholder_data, "get_constructors")

        res = self.test_client.get("/constructors").status_code

        self.assertEqual(res, 404)

    def test_constructors_503(self):
        """
        Test 503 response on /constructors
        """

        mock_cache(empty_cache_data, "get_constructors")

        res = self.test_client.get("/constructors").status_code

        self.assertEqual(res, 503)
