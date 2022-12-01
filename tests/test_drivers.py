import unittest

from fastapi.testclient import TestClient

from app.main import app
from tests.logic.mock_cache import mock_cache, delete_cache_file, empty_cache_data
from tests.mock_data.mock_drivers import get_max_verstappen_data, get_placeholder_data, get_max_verstappen_response


class TestDrivers(unittest.TestCase):
    @classmethod
    def tearDownClass(cls):
        files = [
            "get_driver_by_id.max_verstappen",
            "get_driver_by_id.placeholder",
            "get_drivers",
            "get_drivers_by_season.0",
            "get_drivers_by_season.2022",
            "get_drivers_by_season.9999"
        ]

        for file in files:
            delete_cache_file(file)

    @classmethod
    def setUpClass(cls):
        cls.test_client = TestClient(app)

    ################
    # /driver/{id} #
    ################

    def test_driver_by_id(self):
        """
        Test 200 response on /driver/{id} endpoint with max_verstappen as example
        """

        timestamp = mock_cache(get_max_verstappen_data, "get_driver_by_id.max_verstappen")

        res = self.test_client.get("/driver/max_verstappen").json()

        data = get_max_verstappen_response(timestamp)

        self.assertEqual(res, data)

    def test_driver_by_id_404(self):
        """
        Test 404 response on /driver/{id} endpoint with placeholder as example
        """

        mock_cache(get_placeholder_data, "get_driver_by_id.placeholder")

        res = self.test_client.get("/driver/placeholder").status_code

        self.assertEqual(res, 404)

    def test_driver_by_id_503(self):
        """
        Test 503 response on /driver/{id} endpoint with max_verstappen as example
        """

        mock_cache(empty_cache_data, "get_driver_by_id.max_verstappen")

        res = self.test_client.get("/driver/max_verstappen").status_code

        self.assertEqual(res, 503)

    #####################
    # /drivers/{season} #
    #####################

    def test_drivers_by_season(self):
        mock_cache(get_max_verstappen_data, "get_drivers_by_season.2022")

        res = self.test_client.get("/drivers/2022").json()

        driver_data = next(driver for driver in res["drivers"] if driver["driverId"] == "max_verstappen")

        data = get_max_verstappen_response()

        self.assertEqual(driver_data, data)

    def test_drivers_by_season_404(self):
        """
        Test 404 response on /drivers/{season} endpoint with 9999 as example
        """

        mock_cache(get_placeholder_data, "get_drivers_by_season.9999")

        res = self.test_client.get("/drivers/9999").status_code

        self.assertEqual(res, 404)

    def test_drivers_by_season_503(self):
        """
        Test 503 response on /drivers/{season} endpoint with 0 as example
        """

        mock_cache(empty_cache_data, "get_drivers_by_season.0")

        res = self.test_client.get("/drivers/0").status_code

        self.assertEqual(res, 503)

    #############
    # /drivers #
    #############

    def test_drivers(self):
        mock_cache(get_max_verstappen_data, "get_drivers")

        res = self.test_client.get("/drivers").json()

        driver_data = next(driver for driver in res["drivers"] if driver["driverId"] == "max_verstappen")

        data = get_max_verstappen_response()

        self.assertEqual(driver_data, data)

    def test_drivers_404(self):
        """
        Test 404 response on /drivers
        """

        mock_cache(get_placeholder_data, "get_drivers")

        res = self.test_client.get("/drivers").status_code

        self.assertEqual(res, 404)

    def test_drivers_503(self):
        """
        Test 503 response on /drivers
        """

        mock_cache(empty_cache_data, "get_drivers")

        res = self.test_client.get("/drivers").status_code

        self.assertEqual(res, 503)
