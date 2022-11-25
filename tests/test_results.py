import json
import os
import time
import unittest

from fastapi.testclient import TestClient

from app.main import app
from tests.mock_data.results import get_race_results_data, get_race_results_response, get_race_results_placeholder_data, \
    get_qualifying_results_data, get_qualifying_results_placeholder_data, get_qualifying_results_response, \
    get_driver_standings_response, get_driver_standings_data, get_driver_standings_placeholder_data, \
    get_constructor_standings_data, get_constructor_standings_placeholder_data, get_constructor_standings_response


class TestResults(unittest.TestCase):
    @classmethod
    def setUpRaceResults(cls):
        """
        Init ergast.com response for 2022 in cache (200)
        :return: timestamp
        """

        if os.path.exists("./app/cache/get_race_results.2022.15.json"):
            os.remove("./app/cache/get_race_results.2022.15.json")
            print("Deleted get_race_results.2022.15.json")

        timestamp = float(time.time())

        race_results_data = get_race_results_data(timestamp)

        full_path = "./app/cache/get_race_results.2022.15.json"

        cache_file = open(full_path, "w+")
        cache_file.write(json.dumps(race_results_data))
        cache_file.close()

        return timestamp

    @classmethod
    def setUpRaceResultsPlaceholder(cls, file_name: str):
        """
        Init ergast.com response for placeholder in cache (404)
        :return: timestamp
        """

        if os.path.exists(f"./app/cache/{file_name}.json"):
            os.remove(f"./app/cache/{file_name}.json")
            print(f"Deleted {file_name}.json")

        timestamp = float(time.time())

        placeholder_data = get_race_results_placeholder_data(timestamp)

        full_path = f"./app/cache/{file_name}.json"

        cache_file = open(full_path, "w+")
        cache_file.write(json.dumps(placeholder_data))
        cache_file.close()

        return timestamp

    @classmethod
    def setUpQualifyingResults(cls):
        """
        Init ergast.com response for 2022 in cache (200)
        :return: timestamp
        """

        if os.path.exists("./app/cache/get_qualifying_results.2022.15.json"):
            os.remove("./app/cache/get_qualifying_results.2022.15.json")
            print("Deleted get_qualifying_results.2022.15.json")

        timestamp = float(time.time())

        qualifying_results_data = get_qualifying_results_data(timestamp)

        full_path = "./app/cache/get_qualifying_results.2022.15.json"

        cache_file = open(full_path, "w+")
        cache_file.write(json.dumps(qualifying_results_data))
        cache_file.close()

        return timestamp

    @classmethod
    def setUpQualifyingResultsPlaceholder(cls, file_name: str):
        """
        Init ergast.com response for placeholder in cache (404)
        :return: timestamp
        """

        if os.path.exists(f"./app/cache/{file_name}.json"):
            os.remove(f"./app/cache/{file_name}.json")
            print(f"Deleted {file_name}.json")

        timestamp = float(time.time())

        placeholder_data = get_qualifying_results_placeholder_data(timestamp)

        full_path = f"./app/cache/{file_name}.json"

        cache_file = open(full_path, "w+")
        cache_file.write(json.dumps(placeholder_data))
        cache_file.close()

        return timestamp

    @classmethod
    def setUpDriverStandings(cls):
        """
        Init ergast.com response for 2022 in cache (200)
        :return: timestamp
        """

        if os.path.exists("./app/cache/get_driver_standings_by_season.2022.json"):
            os.remove("./app/cache/get_driver_standings_by_season.2022.json")
            print("Deleted get_driver_standings_by_season.2022.json")

        timestamp = float(time.time())

        driver_standings_data = get_driver_standings_data(timestamp)

        full_path = "./app/cache/get_driver_standings_by_season.2022.json"

        cache_file = open(full_path, "w+")
        cache_file.write(json.dumps(driver_standings_data))
        cache_file.close()

        return timestamp

    @classmethod
    def setUpDriverStandingsPlaceholder(cls, file_name: str):
        """
        Init ergast.com response for placeholder in cache (404)
        :return: timestamp
        """

        if os.path.exists(f"./app/cache/{file_name}.json"):
            os.remove(f"./app/cache/{file_name}.json")
            print(f"Deleted {file_name}.json")

        timestamp = float(time.time())

        placeholder_data = get_driver_standings_placeholder_data(timestamp)

        full_path = f"./app/cache/{file_name}.json"

        cache_file = open(full_path, "w+")
        cache_file.write(json.dumps(placeholder_data))
        cache_file.close()

        return timestamp

    @classmethod
    def setUpConstructorStandings(cls):
        """
        Init ergast.com response for 2022 in cache (200)
        :return: timestamp
        """

        if os.path.exists("./app/cache/get_constructor_standings_by_season.2022.json"):
            os.remove("./app/cache/get_constructor_standings_by_season.2022.json")
            print("Deleted get_constructor_standings_by_season.2022.json")

        timestamp = float(time.time())

        constructor_standings_data = get_constructor_standings_data(timestamp)

        full_path = "./app/cache/get_constructor_standings_by_season.2022.json"

        cache_file = open(full_path, "w+")
        cache_file.write(json.dumps(constructor_standings_data))
        cache_file.close()

        return timestamp

    @classmethod
    def setUpConstructorStandingsPlaceholder(cls, file_name: str):
        """
        Init ergast.com response for placeholder in cache (404)
        :return: timestamp
        """

        if os.path.exists(f"./app/cache/{file_name}.json"):
            os.remove(f"./app/cache/{file_name}.json")
            print(f"Deleted {file_name}.json")

        timestamp = float(time.time())

        placeholder_data = get_constructor_standings_placeholder_data(timestamp)

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
            "get_race_results.2022.15",
            "get_qualifying_results.2022.15",
            "get_driver_standings_by_season.2022",
            "get_constructor_standings_by_season.2022"
        ]

        for file in files:
            if os.path.exists(f"./app/cache/{file}.json"):
                os.remove(f"./app/cache/{file}.json")
                print(f"Deleted {file}.json")

    @classmethod
    def setUpClass(cls):
        cls.test_client = TestClient(app, base_url="http://127.0.0.1:8000")

    #################################
    # /results/race/{season}/{race} #
    #################################

    def test_race_results(self):
        """
        Test 200 response on /results/race/{season}/{race} endpoint with season 2022 race 15 as example
        """

        timestamp = self.setUpRaceResults()

        res = self.test_client.get("/results/race/2022/15").json()

        data = get_race_results_response(timestamp)

        self.assertEqual(res, data)

    def test_race_results_404(self):
        """
        Test 404 response on /results/race/{season}/{race} endpoint with season 2022 race -1 as example
        """

        self.setUpRaceResultsPlaceholder("get_race_results.2022.-1")

        res = self.test_client.get("/results/race/2022/-1").status_code

        self.assertEqual(res, 404)

    def test_race_results_503(self):
        """
        Test 503 response on /results/race/{season}/{race} endpoint with season 0 race 0 as example
        """

        self.setUpEmptyCache("get_race_results.0.0")

        res = self.test_client.get("/results/race/0/0").status_code

        self.assertEqual(res, 503)

    #######################################
    # /results/qualifying/{season}/{race} #
    #######################################

    def test_qualifying_results(self):
        """
        Test 200 response on /results/qualifying/{season}/{race} endpoint with season 2022 race 15 as example
        """

        timestamp = self.setUpQualifyingResults()

        res = self.test_client.get("/results/qualifying/2022/15").json()

        data = get_qualifying_results_response(timestamp)

        self.assertEqual(res, data)

    def test_qualifying_results_404(self):
        """
        Test 404 response on /results/qualifying/{season}/{race} endpoint with season 2022 race -1 as example
        """

        self.setUpQualifyingResultsPlaceholder("get_qualifying_results.2022.-1")

        res = self.test_client.get("/results/qualifying/2022/-1").status_code

        self.assertEqual(res, 404)

    def test_qualifying_results_503(self):
        """
        Test 503 response on /results/qualifying/{season}/{race} endpoint with season 0 race 0 as example
        """

        self.setUpEmptyCache("get_qualifying_results.0.0")

        res = self.test_client.get("/results/qualifying/0/0").status_code

        self.assertEqual(res, 503)

    #######################################
    # /results/standings/drivers/{season} #
    #######################################

    def test_driver_standings_by_season(self):
        """
        Test 200 response on /results/standings/drivers/{season} endpoint with season 2022 as example
        """

        timestamp = self.setUpDriverStandings()

        res = self.test_client.get("/results/standings/drivers/2022").json()

        data = get_driver_standings_response(timestamp)

        self.assertEqual(res, data)

    def test_driver_standings_by_season_404(self):
        """
        Test 404 response on /results/standings/drivers/{season} endpoint with season 0 as example
        """

        self.setUpDriverStandingsPlaceholder("get_driver_standings_by_season.0")

        res = self.test_client.get("/results/standings/drivers/0").status_code

        self.assertEqual(res, 404)

    def test_driver_standings_by_season_503(self):
        """
        Test 503 response on /results/standings/drivers/{season} endpoint with season 0 as example
        """

        self.setUpEmptyCache("get_driver_standings_by_season.0")

        res = self.test_client.get("/results/standings/drivers/0").status_code

        self.assertEqual(res, 503)

    ############################################
    # /results/standings/constructors/{season} #
    ############################################

    def test_constructor_standings_by_season(self):
        """
        Test 200 response on /results/standings/constructors/{season} endpoint with season 2022 as example
        """

        timestamp = self.setUpConstructorStandings()

        res = self.test_client.get("/results/standings/constructors/2022").json()

        data = get_constructor_standings_response(timestamp)

        self.assertEqual(res, data)

    def test_constructor_standings_by_season_404(self):
        """
        Test 404 response on /results/standings/constructor/{season} endpoint with season 0 as example
        """

        self.setUpConstructorStandingsPlaceholder("get_constructor_standings_by_season.0")

        res = self.test_client.get("/results/standings/constructors/0").status_code

        self.assertEqual(res, 404)

    def test_constructor_standings_by_season_503(self):
        """
        Test 503 response on /results/standings/constructor/{season} endpoint with season 0 as example
        """

        self.setUpEmptyCache("get_constructor_standings_by_season.0")

        res = self.test_client.get("/results/standings/constructors/0").status_code

        self.assertEqual(res, 503)
