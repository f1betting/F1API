import json
import os
import time
import unittest

from fastapi.testclient import TestClient

from app.main import app
from tests.mock_data.calendar import get_season_data, get_season_placeholder_data, get_season_response, \
    get_next_race_data, get_next_race_response, get_previous_race_data, get_previous_race_response, \
    get_event_details_data, get_event_details_response, get_event_details_placeholder


class TestCalendar(unittest.TestCase):
    @classmethod
    def setUpSeason(cls):
        """
        Init ergast.com response for 2022 in cache (200)
        :return: timestamp
        """

        if os.path.exists("./app/cache/get_calendar_by_season.2022.json"):
            os.remove("./app/cache/get_calendar_by_season.2022.json")
            print("Deleted get_calendar_by_season.2022.json")

        timestamp = float(time.time())

        season_data = get_season_data(timestamp)

        full_path = "./app/cache/get_calendar_by_season.2022.json"

        cache_file = open(full_path, "w+")
        cache_file.write(json.dumps(season_data))
        cache_file.close()

        return timestamp

    @classmethod
    def setUpSeasonPlaceholder(cls, file_name: str):
        """
        Init ergast.com response for placeholder in cache (404)
        :return: timestamp
        """

        if os.path.exists(f"./app/cache/{file_name}.json"):
            os.remove(f"./app/cache/{file_name}.json")
            print(f"Deleted {file_name}.json")

        timestamp = float(time.time())

        placeholder_data = get_season_placeholder_data(timestamp)

        full_path = f"./app/cache/{file_name}.json"

        cache_file = open(full_path, "w+")
        cache_file.write(json.dumps(placeholder_data))
        cache_file.close()

        return timestamp

    @classmethod
    def setUpNextRace(cls):
        """
        Init ergast.com response for 2022 in cache (200)
        :return: timestamp
        """

        if os.path.exists("./app/cache/get_next_race.json"):
            os.remove("./app/cache/get_next_race.json")
            print("Deleted get_next_race.json")

        timestamp = float(time.time())

        next_race_data = get_next_race_data(timestamp)

        full_path = "./app/cache/get_next_race.json"

        cache_file = open(full_path, "w+")
        cache_file.write(json.dumps(next_race_data))
        cache_file.close()

        return timestamp

    @classmethod
    def setUpPreviousRace(cls):
        """
        Init ergast.com response for 2022 in cache (200)
        :return: timestamp
        """

        if os.path.exists("./app/cache/get_previous_race.json"):
            os.remove("./app/cache/get_previous_race.json")
            print("Deleted get_previous_race.json")

        timestamp = float(time.time())

        next_race_data = get_previous_race_data(timestamp)

        full_path = "./app/cache/get_previous_race.json"

        cache_file = open(full_path, "w+")
        cache_file.write(json.dumps(next_race_data))
        cache_file.close()

        return timestamp

    @classmethod
    def setUpEventDetails(cls):
        """
        Init ergast.com response for 2022 in cache (200)
        :return: timestamp
        """

        if os.path.exists("./app/cache/get_event_details.2022.15.json"):
            os.remove("./app/cache/get_event_details.2022.15.json")
            print("Deleted get_event_details.2022.15.json")

        timestamp = float(time.time())

        season_data = get_event_details_data(timestamp)

        full_path = "./app/cache/get_event_details.2022.15.json"

        cache_file = open(full_path, "w+")
        cache_file.write(json.dumps(season_data))
        cache_file.close()

        return timestamp

    @classmethod
    def setUpEventDetailsPlaceholder(cls, file_name: str):
        """
        Init ergast.com response for placeholder in cache (404)
        :return: timestamp
        """

        if os.path.exists(f"./app/cache/{file_name}.json"):
            os.remove(f"./app/cache/{file_name}.json")
            print(f"Deleted {file_name}.json")

        timestamp = float(time.time())

        placeholder_data = get_event_details_placeholder(timestamp)

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
            "get_calendar_by_season.0",
            "get_calendar_by_season.2022",
            "get_next_race",
            "get_previous_race",
            "get_event_details.2022.0",
            "get_event_details.2022.15"
        ]

        for file in files:
            if os.path.exists(f"./app/cache/{file}.json"):
                os.remove(f"./app/cache/{file}.json")
                print(f"Deleted {file}.json")

    @classmethod
    def setUpClass(cls):
        cls.test_client = TestClient(app, base_url="http://127.0.0.1:8000")

    ######################
    # /calendar/{season} #
    ######################

    def test_calendar_by_season(self):
        """
        Test 200 response on /calendar/{season} endpoint with 2022 as example
        """

        self.setUpSeason()

        res = self.test_client.get("/calendar/2022").json()

        event_data = next(race for race in res["events"] if race["raceName"] == "Dutch Grand Prix")

        data = get_season_response()

        self.assertEqual(event_data, data)

    def test_calendar_by_season_404(self):
        """
        Test 404 response on /calendar/{season} endpoint with 0 as example
        """

        self.setUpSeasonPlaceholder("get_calendar_by_season.0")

        res = self.test_client.get("/calendar/0").status_code

        self.assertEqual(res, 404)

    def test_calendar_by_season_503(self):
        """
        Test 503 response on /calendar/{season} endpoint with 0 as example
        """

        self.setUpEmptyCache("get_calendar_by_season.0")

        res = self.test_client.get("/calendar/0").status_code

        self.assertEqual(res, 503)

    ###############
    # /event/next #
    ###############

    def test_get_next_race(self):
        """
        Test 200 response on /event/next
        """

        timestamp = self.setUpNextRace()

        res = self.test_client.get("/event/next").json()

        data = get_next_race_response(timestamp)

        self.assertEqual(res, data)

    def test_get_next_race_503(self):
        """
        Test 503 response on /event/next endpoint with 0 as example
        """

        self.setUpEmptyCache("get_next_race")

        res = self.test_client.get("/event/next").status_code

        self.assertEqual(res, 503)

    ###################
    # /event/previous #
    ###################

    def test_get_previous_race(self):
        """
        Test 200 response on /event/previous
        """

        timestamp = self.setUpPreviousRace()

        res = self.test_client.get("/event/previous").json()

        data = get_previous_race_response(timestamp)

        self.assertEqual(res, data)

    def test_get_previous_race_503(self):
        """
        Test 503 response on /event/previous endpoint with 0 as example
        """

        self.setUpEmptyCache("get_previous_race")

        res = self.test_client.get("/event/previous").status_code

        self.assertEqual(res, 503)

        ###########################
        # /event/{season}/{round} #
        ###########################

    def test_get_event_details(self):
        """
        Test 200 response on /event/{season}/{round} endpoint with season 2022 round 15 as example
        """

        timestamp = self.setUpEventDetails()

        res = self.test_client.get("/event/2022/15").json()

        data = get_event_details_response(timestamp)

        self.assertEqual(res, data)

    def test_get_event_details_404(self):
        """
        Test 404 response on /event/{season}/{round} endpoint with season 2022 round -1 as example
        """

        self.setUpEventDetailsPlaceholder("get_event_details.2022.-1")

        res = self.test_client.get("/event/2022/-1").status_code

        self.assertEqual(res, 404)

    def test_get_event_details_503(self):
        """
        Test 503 response on on /event/{season}/{round} endpoint with season 0 round 0 as example
        """

        self.setUpEmptyCache("get_event_details.0.0")

        res = self.test_client.get("/event/0/0").status_code

        self.assertEqual(res, 503)
