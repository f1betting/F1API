import json
import os
import time
import unittest

from fastapi.testclient import TestClient

from app.main import app
from tests.mock_data.drivers import get_max_verstappen_data, get_placeholder_data, get_max_verstappen_response


class TestDrivers(unittest.TestCase):
    @classmethod
    def setUpDriver(cls):
        """
        Init ergast.com response for max_verstappen in cache (200)
        :return: timestamp
        """

        if os.path.exists("./app/cache/get_driver_by_id.max_verstappen.json"):
            os.remove("./app/cache/get_driver_by_id.max_verstappen.json")
            print("Deleted get_driver_by_id.max_verstappen.json")

        timestamp = float(time.time())

        max_verstappen_data = get_max_verstappen_data(timestamp)

        full_path = "./app/cache/get_driver_by_id.max_verstappen.json"

        cache_file = open(full_path, "w+")
        cache_file.write(json.dumps(max_verstappen_data))
        cache_file.close()

        return timestamp

    @classmethod
    def setUpPlaceholder(cls, file_name: str):
        """
        Init ergast.com response for placeholder in cache (404)
        :return: timestamp
        """

        if os.path.exists(f"./app/cache/{file_name}.json"):
            os.remove(f"./app/cache/{file_name}.json")
            print(f"Deleted {file_name}.json")

        timestamp = float(time.time())

        placeholder_data = get_placeholder_data(timestamp)

        full_path = f"./app/cache/{file_name}.json"

        cache_file = open(full_path, "w+")
        cache_file.write(json.dumps(placeholder_data))
        cache_file.close()

        return timestamp

    @classmethod
    def setUpEmptyCache(cls, file_name: str):
        timestamp = float(time.time())

        full_path = f"./app/cache/{file_name}.json"

        cache_file = open(full_path, "w+")
        cache_file.write(json.dumps({"timestamp": timestamp}))
        cache_file.close()

        return timestamp

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
            if os.path.exists(f"./app/cache/{file}.json"):
                os.remove(f"./app/cache/{file}.json")
                print(f"Deleted {file}.json")

    @classmethod
    def setUpClass(cls):
        cls.test_client = TestClient(app, base_url="http://127.0.0.1:8000")

    ################
    # /driver/{id} #
    ################

    def test_driver_by_id(self):
        """
        Test 200 response on /driver/{id} endpoint with max_verstappen as example
        """

        timestamp = self.setUpDriver()

        res = self.test_client.get("/driver/max_verstappen").json()

        data = get_max_verstappen_response(timestamp)

        self.assertEqual(res, data)

    def test_driver_by_id_404(self):
        """
        Test 404 response on /driver/{id} endpoint with placeholder as example
        """

        self.setUpPlaceholder("get_driver_by_id.placeholder")

        res = self.test_client.get("/driver/placeholder").status_code

        self.assertEqual(res, 404)

    def test_driver_by_id_503(self):
        """
        Test 503 response on /driver/{id} endpoint with max_verstappen as example
        """

        self.setUpEmptyCache("get_driver_by_id.max_verstappen")

        res = self.test_client.get("/driver/max_verstappen").status_code

        self.assertEqual(res, 503)

    #####################
    # /drivers/{season} #
    #####################

    def test_drivers_by_season(self):
        self.setUpDriver()

        res = self.test_client.get("/drivers/2022").json()

        driver_data = next(driver for driver in res["drivers"] if driver["driverId"] == "max_verstappen")

        data = get_max_verstappen_response()

        self.assertEqual(driver_data, data)

    def test_drivers_by_season_404(self):
        """
        Test 404 response on /drivers/{season} endpoint with 9999 as example
        """

        self.setUpPlaceholder("get_drivers_by_season.9999")

        res = self.test_client.get("/drivers/9999").status_code

        self.assertEqual(res, 404)

    def test_drivers_by_season_503(self):
        """
        Test 503 response on /drivers/{season} endpoint with 0 as example
        """

        self.setUpEmptyCache("get_drivers_by_season.0")

        res = self.test_client.get("/drivers/0").status_code

        self.assertEqual(res, 503)

    #############
    # /drivers #
    #############

    def test_drivers(self):
        self.setUpDriver()

        res = self.test_client.get("/drivers").json()

        driver_data = next(driver for driver in res["drivers"] if driver["driverId"] == "max_verstappen")

        data = get_max_verstappen_response()

        self.assertEqual(driver_data, data)

    def test_drivers_404(self):
        """
        Test 404 response on /drivers
        """

        self.setUpPlaceholder("get_drivers")

        res = self.test_client.get("/drivers").status_code

        self.assertEqual(res, 404)

    def test_drivers_503(self):
        """
        Test 503 response on /drivers
        """

        self.setUpEmptyCache("get_drivers")

        res = self.test_client.get("/drivers").status_code

        self.assertEqual(res, 503)
