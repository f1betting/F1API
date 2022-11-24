import json
import os
import time
import unittest

from fastapi.testclient import TestClient

from app.main import app


class TestCircuits(unittest.TestCase):
    @classmethod
    def setUpAlbertPark(cls):
        """
        Init ergast.com response for albert_park in cache (200)
        :return: timestamp
        """

        if os.path.exists("./app/cache/get_circuit_by_id.albert_park.json"):
            os.remove("./app/cache/get_circuit_by_id.albert_park.json")
            print("Deleted get_circuit_by_id.albert_park.json")

        timestamp = float(time.time())

        albert_park_data = {
            "MRData": {
                "xmlns": "http://ergast.com/mrd/1.5",
                "series": "f1",
                "url": "http://ergast.com/api/f1/circuits/albert_park.json",
                "limit": "30",
                "offset": "0",
                "total": "1",
                "CircuitTable": {
                    "circuitId": "albert_park",
                    "Circuits": [
                        {
                            "circuitId": "albert_park",
                            "url": "http://en.wikipedia.org/wiki/Melbourne_Grand_Prix_Circuit",
                            "circuitName": "Albert Park Grand Prix Circuit",
                            "Location": {
                                "lat": "-37.8497",
                                "long": "144.968",
                                "locality": "Melbourne",
                                "country": "Australia"
                            }
                        }
                    ]
                }
            },
            "timestamp": timestamp
        }

        full_path = "./app/cache/get_circuit_by_id.albert_park.json"

        cache_file = open(full_path, "w+")
        cache_file.write(json.dumps(albert_park_data))
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
                "url": "http://ergast.com/api/f1/circuits/placeholder.json",
                "limit": "30",
                "offset": "0",
                "total": "1",
                "CircuitTable": {
                    "circuitId": "placeholder",
                    "Circuits": []
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
        files = ["get_circuit_by_id.albert_park",
                 "get_circuit_by_id.placeholder",
                 "get_circuit_by_id.albert_park",
                 "get_circuits_by_season.2022",
                 "get_circuits"]

        for file in files:
            if os.path.exists(f"./app/cache/{file}.json"):
                os.remove(f"./app/cache/{file}.json")
                print(f"Deleted {file}.json")

    @classmethod
    def setUpClass(cls):
        cls.test_client = TestClient(app, base_url="http://127.0.0.1:8000")

    #################
    # /circuit/{id} #
    #################

    def test_circuit_by_id(self):
        """
        Test 200 response on /circuit/{id} endpoint with albert_park as example
        """

        timestamp = self.setUpAlbertPark()

        res = self.test_client.get("/circuit/albert_park").json()

        data = {
            "timestamp": timestamp,
            "circuitId": "albert_park",
            "url": "http://en.wikipedia.org/wiki/Melbourne_Grand_Prix_Circuit",
            "circuitName": "Albert Park Grand Prix Circuit",
            "Location": {
                "lat": -37.8497,
                "long": 144.968,
                "locality": "Melbourne",
                "country": "Australia"
            }
        }

        self.assertEqual(res, data)

    def test_circuit_by_id_404(self):
        """
        Test 404 response on /circuit/{id} endpoint with placeholder as example
        """

        self.setUpPlaceholder("get_circuit_by_id.placeholder")

        res = self.test_client.get("/circuit/placeholder").status_code

        self.assertEqual(res, 404)

    def test_circuit_by_id_503(self):
        """
        Test 503 response on /circuit/{id} endpoint with albert_park as example
        """

        self.setUpEmptyCache("get_circuit_by_id.albert_park")

        res = self.test_client.get("/circuit/albert_park").status_code

        self.assertEqual(res, 503)

    ######################
    # /circuits/{season} #
    ######################

    def test_circuit_by_season(self):
        self.setUpAlbertPark()

        res = self.test_client.get("/circuits/2022").json()

        circuit_data = next(circuit for circuit in res["circuits"] if circuit["circuitId"] == "albert_park")

        data = {
            "timestamp": None,
            "circuitId": "albert_park",
            "url": "http://en.wikipedia.org/wiki/Melbourne_Grand_Prix_Circuit",
            "circuitName": "Albert Park Grand Prix Circuit",
            "Location": {
                "lat": -37.8497,
                "long": 144.968,
                "locality": "Melbourne",
                "country": "Australia"
            }
        }

        self.assertEqual(circuit_data, data)

    def test_circuit_by_season_404(self):
        """
        Test 404 response on /circuits/{season} endpoint with 9999 as example
        """

        self.setUpPlaceholder("get_circuits_by_season.9999")

        res = self.test_client.get("/circuits/9999").status_code

        self.assertEqual(res, 404)

    def test_circuit_by_season_503(self):
        """
        Test 503 response on /circuit/{season} endpoint with 0 as example
        """

        self.setUpEmptyCache("get_circuits_by_season.0")

        res = self.test_client.get("/circuits/0").status_code

        self.assertEqual(res, 503)

    #############
    # /circuits #
    #############

    def test_circuits(self):
        self.setUpAlbertPark()

        res = self.test_client.get("/circuits").json()

        circuit_data = next(circuit for circuit in res["circuits"] if circuit["circuitId"] == "albert_park")

        data = {
            "timestamp": None,
            "circuitId": "albert_park",
            "url": "http://en.wikipedia.org/wiki/Melbourne_Grand_Prix_Circuit",
            "circuitName": "Albert Park Grand Prix Circuit",
            "Location": {
                "lat": -37.8497,
                "long": 144.968,
                "locality": "Melbourne",
                "country": "Australia"
            }
        }

        self.assertEqual(circuit_data, data)

    def test_circuits_404(self):
        """
        Test 404 response on /circuitss endpoint
        """

        self.setUpPlaceholder("get_circuits")

        res = self.test_client.get("/circuits").status_code

        self.assertEqual(res, 404)

    def test_circuits_503(self):
        """
        Test 503 response on /circuits endpoint
        """

        self.setUpEmptyCache("get_circuits")

        res = self.test_client.get("/circuits").status_code

        self.assertEqual(res, 503)
