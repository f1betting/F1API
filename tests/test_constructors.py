import json
import os
import time
import unittest

from fastapi.testclient import TestClient

from app.main import app


class TestConstructors(unittest.TestCase):
    @classmethod
    def setUpRedBull(cls):
        """
        Init ergast.com response for red_bull in cache (200)
        :return: timestamp
        """

        if os.path.exists("./app/cache/get_constructor_by_id.red_bull.json"):
            os.remove("./app/cache/get_constructor_by_id.red_bull.json")
            print("Deleted get_constructor_by_id.red_bull.json")

        timestamp = float(time.time())

        red_bull_data = {
            "MRData": {
                "xmlns": "http://ergast.com/mrd/1.5",
                "series": "f1",
                "url": "http://ergast.com/api/f1/constructors/red_bull.json",
                "limit": "30",
                "offset": "0",
                "total": "1",
                "ConstructorTable": {
                    "constructorId": "red_bull",
                    "Constructors": [
                        {
                            "constructorId": "red_bull",
                            "url": "http://en.wikipedia.org/wiki/Red_Bull_Racing",
                            "name": "Red Bull",
                            "nationality": "Austrian"
                        }
                    ]
                }
            },
            "timestamp": timestamp
        }

        full_path = "./app/cache/get_constructor_by_id.red_bull.json"

        cache_file = open(full_path, "w+")
        cache_file.write(json.dumps(red_bull_data))
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
                "url": "http://ergast.com/api/f1/constructors/placeholder.json",
                "limit": "30",
                "offset": "0",
                "total": "1",
                "ConstructorTable": {
                    "constructorId": "placeholder",
                    "Constructors": []
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
            "get_constructor_by_id.placeholder",
            "get_constructor_by_id.red_bull",
            "get_constructors",
            "get_constructors_by_season.0",
            "get_constructors_by_season.2022",
            "get_constructors_by_season.9999"
        ]

        for file in files:
            if os.path.exists(f"./app/cache/{file}.json"):
                os.remove(f"./app/cache/{file}.json")
                print(f"Deleted {file}.json")

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

        timestamp = self.setUpRedBull()

        res = self.test_client.get("/constructor/red_bull").json()

        data = {
            "timestamp": timestamp,
            "constructorId": "red_bull",
            "url": "http://en.wikipedia.org/wiki/Red_Bull_Racing",
            "name": "Red Bull",
            "nationality": "Austrian"
        }

        self.assertEqual(res, data)

    def test_constructor_by_id_404(self):
        """
        Test 404 response on /constructor/{id} endpoint with placeholder as example
        """

        self.setUpPlaceholder("get_constructor_by_id.placeholder")

        res = self.test_client.get("/constructor/placeholder").status_code

        self.assertEqual(res, 404)

    def test_constructor_by_id_503(self):
        """
        Test 503 response on /constructor/{id} endpoint with red_bull as example
        """

        self.setUpEmptyCache("get_constructor_by_id.red_bull")

        res = self.test_client.get("/constructor/red_bull").status_code

        self.assertEqual(res, 503)

    ########################
    # /constructors/{season} #
    ########################

    def test_constructors_by_season(self):
        self.setUpRedBull()

        res = self.test_client.get("/constructors/2022").json()

        constructors_data = next(
            constructor for constructor in res["constructors"] if constructor["constructorId"] == "red_bull"
        )

        data = {
            "timestamp": None,
            "constructorId": "red_bull",
            "url": "http://en.wikipedia.org/wiki/Red_Bull_Racing",
            "name": "Red Bull",
            "nationality": "Austrian"
        }

        self.assertEqual(constructors_data, data)

    def test_constructors_by_season_404(self):
        """
        Test 404 response on /constructors/{season} endpoint with 9999 as example
        """

        self.setUpPlaceholder("get_constructors_by_season.9999")

        res = self.test_client.get("/constructors/9999").status_code

        self.assertEqual(res, 404)

    def test_constructor_by_season_503(self):
        """
        Test 503 response on /constructors/{season} endpoint with 0 as example
        """

        self.setUpEmptyCache("get_constructors_by_season.0")

        res = self.test_client.get("/constructors/0").status_code

        self.assertEqual(res, 503)

    #############
    # /constructors #
    #############

    def test_constructors(self):
        self.setUpRedBull()

        res = self.test_client.get("/constructors").json()

        constructor_data = next(
            constructor for constructor in res["constructors"] if constructor["constructorId"] == "red_bull"
        )

        data = {
            "timestamp": None,
            "constructorId": "red_bull",
            "url": "http://en.wikipedia.org/wiki/Red_Bull_Racing",
            "name": "Red Bull",
            "nationality": "Austrian"
        }

        self.assertEqual(constructor_data, data)

    def test_constructors_404(self):
        """
        Test 404 response on /constructors
        """

        self.setUpPlaceholder("get_constructors")

        res = self.test_client.get("/constructors").status_code

        self.assertEqual(res, 404)

    def test_constructors_503(self):
        """
        Test 503 response on /constructors
        """

        self.setUpEmptyCache("get_constructors")

        res = self.test_client.get("/constructors").status_code

        self.assertEqual(res, 503)
