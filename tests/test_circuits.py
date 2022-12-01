import unittest

from fastapi.testclient import TestClient

from app.main import app
from .logic.mock_cache import mock_cache, empty_cache_data, delete_cache_file
from .mock_data.mock_circuits import get_albert_park_data, get_albert_park_response, get_placeholder_data


class TestCircuits(unittest.TestCase):
    @classmethod
    def tearDownClass(cls):
        files = ["get_circuit_by_id.albert_park",
                 "get_circuit_by_id.placeholder",
                 "get_circuit_by_id.albert_park",
                 "get_circuits_by_season.2022",
                 "get_circuits"]

        for file in files:
            delete_cache_file(file)

    @classmethod
    def setUpClass(cls):
        cls.test_client = TestClient(app)

    #################
    # /circuit/{id} #
    #################

    def test_circuit_by_id(self):
        """
        Test 200 response on /circuit/{id} endpoint with albert_park as example
        """
        timestamp = mock_cache(get_albert_park_data, "get_circuit_by_id.albert_park")

        res = self.test_client.get("/circuit/albert_park").json()

        data = get_albert_park_response(timestamp)

        self.assertEqual(res, data)

    def test_circuit_by_id_404(self):
        """
        Test 404 response on /circuit/{id} endpoint with placeholder as example
        """
        mock_cache(get_placeholder_data, "get_circuit_by_id.placeholder")

        res = self.test_client.get("/circuit/placeholder").status_code

        self.assertEqual(res, 404)

    def test_circuit_by_id_503(self):
        """
        Test 503 response on /circuit/{id} endpoint with albert_park as example
        """

        mock_cache(empty_cache_data, "get_circuit_by_id.albert_park")

        res = self.test_client.get("/circuit/albert_park").status_code

        self.assertEqual(res, 503)

    ######################
    # /circuits/{season} #
    ######################

    def test_circuit_by_season(self):
        mock_cache(get_albert_park_data, "get_circuits_by_season.2022")

        res = self.test_client.get("/circuits/2022").json()

        circuit_data = next(circuit for circuit in res["circuits"] if circuit["circuitId"] == "albert_park")

        data = get_albert_park_response()

        self.assertEqual(circuit_data, data)

    def test_circuit_by_season_404(self):
        """
        Test 404 response on /circuits/{season} endpoint with 9999 as example
        """

        mock_cache(get_placeholder_data, "get_circuits_by_season.9999")

        res = self.test_client.get("/circuits/9999").status_code

        self.assertEqual(res, 404)

    def test_circuit_by_season_503(self):
        """
        Test 503 response on /circuit/{season} endpoint with 0 as example
        """

        mock_cache(empty_cache_data, "get_circuits_by_season.0")

        res = self.test_client.get("/circuits/0").status_code

        self.assertEqual(res, 503)

    #############
    # /circuits #
    #############

    def test_circuits(self):
        mock_cache(get_albert_park_data, "get_circuits")

        res = self.test_client.get("/circuits").json()

        circuit_data = next(circuit for circuit in res["circuits"] if circuit["circuitId"] == "albert_park")

        data = get_albert_park_response()

        self.assertEqual(circuit_data, data)

    def test_circuits_404(self):
        """
        Test 404 response on /circuitss endpoint
        """

        mock_cache(get_placeholder_data, "get_circuits")

        res = self.test_client.get("/circuits").status_code

        self.assertEqual(res, 404)

    def test_circuits_503(self):
        """
        Test 503 response on /circuits endpoint
        """

        mock_cache(empty_cache_data, "get_circuits")

        res = self.test_client.get("/circuits").status_code

        self.assertEqual(res, 503)
