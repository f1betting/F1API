import json
import os
import time
import unittest

from fastapi.testclient import TestClient

from app.main import app


class TestCalendar(unittest.TestCase):
    @classmethod
    def setUp2022(cls):
        """
        Init ergast.com response for 2022 in cache (200)
        :return: timestamp
        """

        if os.path.exists("./app/cache/get_calendar_by_season.2022.json"):
            os.remove("./app/cache/get_calendar_by_season.2022.json")
            print("Deleted get_calendar_by_season.2022.json")

        timestamp = float(time.time())

        season_data = {
            "MRData": {
                "xmlns": "http://ergast.com/mrd/1.5",
                "series": "f1",
                "url": "http://ergast.com/api/f1/2022.json",
                "limit": "30",
                "offset": "0",
                "total": "22",
                "RaceTable": {
                    "season": "2022",
                    "Races": [
                        {
                            "season": "2022",
                            "round": "15",
                            "url": "http://en.wikipedia.org/wiki/2022_Dutch_Grand_Prix",
                            "raceName": "Dutch Grand Prix",
                            "Circuit": {
                                "circuitId": "zandvoort",
                                "url": "http://en.wikipedia.org/wiki/Circuit_Zandvoort",
                                "circuitName": "Circuit Park Zandvoort",
                                "Location": {
                                    "lat": "52.3888",
                                    "long": "4.54092",
                                    "locality": "Zandvoort",
                                    "country": "Netherlands"
                                }
                            },
                            "date": "2022-09-04",
                            "time": "13:00:00Z",
                            "FirstPractice": {
                                "date": "2022-09-02",
                                "time": "10:30:00Z"
                            },
                            "SecondPractice": {
                                "date": "2022-09-02",
                                "time": "14:00:00Z"
                            },
                            "ThirdPractice": {
                                "date": "2022-09-03",
                                "time": "10:00:00Z"
                            },
                            "Qualifying": {
                                "date": "2022-09-03",
                                "time": "13:00:00Z"
                            }
                        }
                    ]
                }
            },
            "timestamp": timestamp
        }

        full_path = "./app/cache/get_calendar_by_season.2022.json"

        cache_file = open(full_path, "w+")
        cache_file.write(json.dumps(season_data))
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

        placeholder_data = {
            "MRData": {
                "xmlns": "http://ergast.com/mrd/1.5",
                "series": "f1",
                "url": "http://ergast.com/api/f1/placeholder.json",
                "limit": "30",
                "offset": "0",
                "total": "0",
                "RaceTable": {
                    "season": "placeholder",
                    "Races": []
                }
            },
            "timestamp": timestamp
        }

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
            "get_calendar_by_season.2022"
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

        self.setUp2022()

        res = self.test_client.get("/calendar/2022").json()

        event_data = next(race for race in res["events"] if race["raceName"] == "Dutch Grand Prix")

        data = {
            "timestamp": None,
            "season": 2022,
            "round": 15,
            "url": "http://en.wikipedia.org/wiki/2022_Dutch_Grand_Prix",
            "raceName": "Dutch Grand Prix",
            "Circuit": {
                "timestamp": None,
                "circuitId": "zandvoort",
                "url": "http://en.wikipedia.org/wiki/Circuit_Zandvoort",
                "circuitName": "Circuit Park Zandvoort",
                "Location": {
                    "lat": 52.3888,
                    "long": 4.54092,
                    "locality": "Zandvoort",
                    "country": "Netherlands"
                }
            },
            "date": "2022-09-04",
            "time": "13:00:00Z",
            "FirstPractice": {
                "date": "2022-09-02",
                "time": "10:30:00Z"
            },
            "SecondPractice": {
                "date": "2022-09-02",
                "time": "14:00:00Z"
            },
            "ThirdPractice": {
                "date": "2022-09-03",
                "time": "10:00:00Z"
            },
            "Qualifying": {
                "date": "2022-09-03",
                "time": "13:00:00Z"
            }
        }

        self.assertEqual(event_data, data)

    def test_calendar_by_season_404(self):
        """
        Test 404 response on /calendar/{season} endpoint with 0 as example
        """

        self.setUpPlaceholder("get_calendar_by_season.0")

        res = self.test_client.get("/calendar/0").status_code

        self.assertEqual(res, 404)

    def test_calendar_by_season_503(self):
        """
        Test 503 response on /calendar/{season} endpoint with 0 as example
        """

        self.setUpEmptyCache("get_calendar_by_season.0")

        res = self.test_client.get("/calendar/0").status_code

        self.assertEqual(res, 503)
