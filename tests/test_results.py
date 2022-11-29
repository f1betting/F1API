import unittest

from fastapi.testclient import TestClient

from app.main import app
from tests.logic.mock_cache import delete_cache_file, mock_cache, empty_cache_data
from tests.mock_data.results import get_race_results_data, get_race_results_response, get_race_results_placeholder_data, \
    get_qualifying_results_data, get_qualifying_results_placeholder_data, get_qualifying_results_response, \
    get_driver_standings_response, get_driver_standings_data, get_driver_standings_placeholder_data, \
    get_constructor_standings_data, get_constructor_standings_placeholder_data, get_constructor_standings_response


class TestResults(unittest.TestCase):
    @classmethod
    def tearDownClass(cls):
        files = [
            "get_race_results.2022.15",
            "get_qualifying_results.2022.15",
            "get_driver_standings_by_season.2022",
            "get_constructor_standings_by_season.2022"
        ]

        for file in files:
            delete_cache_file(file)

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

        timestamp = mock_cache(get_race_results_data, "get_race_results.2022.15")

        res = self.test_client.get("/results/race/2022/15").json()

        data = get_race_results_response(timestamp)

        self.assertEqual(res, data)

    def test_race_results_404(self):
        """
        Test 404 response on /results/race/{season}/{race} endpoint with season 2022 race -1 as example
        """

        mock_cache(get_race_results_placeholder_data, "get_race_results.2022.-1")

        res = self.test_client.get("/results/race/2022/-1").status_code

        self.assertEqual(res, 404)

    def test_race_results_503(self):
        """
        Test 503 response on /results/race/{season}/{race} endpoint with season 0 race 0 as example
        """

        mock_cache(empty_cache_data, "get_race_results.0.0")

        res = self.test_client.get("/results/race/0/0").status_code

        self.assertEqual(res, 503)

    #######################################
    # /results/qualifying/{season}/{race} #
    #######################################

    def test_qualifying_results(self):
        """
        Test 200 response on /results/qualifying/{season}/{race} endpoint with season 2022 race 15 as example
        """

        timestamp = mock_cache(get_qualifying_results_data, "get_qualifying_results.2022.15")

        res = self.test_client.get("/results/qualifying/2022/15").json()

        data = get_qualifying_results_response(timestamp)

        self.assertEqual(res, data)

    def test_qualifying_results_404(self):
        """
        Test 404 response on /results/qualifying/{season}/{race} endpoint with season 2022 race -1 as example
        """

        mock_cache(get_qualifying_results_placeholder_data, "get_qualifying_results.2022.-1")

        res = self.test_client.get("/results/qualifying/2022/-1").status_code

        self.assertEqual(res, 404)

    def test_qualifying_results_503(self):
        """
        Test 503 response on /results/qualifying/{season}/{race} endpoint with season 0 race 0 as example
        """

        mock_cache(empty_cache_data, "get_qualifying_results.0.0")

        res = self.test_client.get("/results/qualifying/0/0").status_code

        self.assertEqual(res, 503)

    #######################################
    # /results/standings/drivers/{season} #
    #######################################

    def test_driver_standings_by_season(self):
        """
        Test 200 response on /results/standings/drivers/{season} endpoint with season 2022 as example
        """

        timestamp = mock_cache(get_driver_standings_data, "get_driver_standings_by_season.2022")

        res = self.test_client.get("/results/standings/drivers/2022").json()

        data = get_driver_standings_response(timestamp)

        self.assertEqual(res, data)

    def test_driver_standings_by_season_404(self):
        """
        Test 404 response on /results/standings/drivers/{season} endpoint with season 0 as example
        """

        mock_cache(get_driver_standings_placeholder_data, "get_driver_standings_by_season.0")

        res = self.test_client.get("/results/standings/drivers/0").status_code

        self.assertEqual(res, 404)

    def test_driver_standings_by_season_503(self):
        """
        Test 503 response on /results/standings/drivers/{season} endpoint with season 0 as example
        """

        mock_cache(empty_cache_data, "get_driver_standings_by_season.0")

        res = self.test_client.get("/results/standings/drivers/0").status_code

        self.assertEqual(res, 503)

    ############################################
    # /results/standings/constructors/{season} #
    ############################################

    def test_constructor_standings_by_season(self):
        """
        Test 200 response on /results/standings/constructors/{season} endpoint with season 2022 as example
        """

        timestamp = mock_cache(get_constructor_standings_data, "get_constructor_standings_by_season.2022")

        res = self.test_client.get("/results/standings/constructors/2022").json()

        data = get_constructor_standings_response(timestamp)

        self.assertEqual(res, data)

    def test_constructor_standings_by_season_404(self):
        """
        Test 404 response on /results/standings/constructor/{season} endpoint with season 0 as example
        """

        mock_cache(get_constructor_standings_placeholder_data, "get_constructor_standings_by_season.0")

        res = self.test_client.get("/results/standings/constructors/0").status_code

        self.assertEqual(res, 404)

    def test_constructor_standings_by_season_503(self):
        """
        Test 503 response on /results/standings/constructor/{season} endpoint with season 0 as example
        """

        mock_cache(empty_cache_data, "get_constructor_standings_by_season.0")

        res = self.test_client.get("/results/standings/constructors/0").status_code

        self.assertEqual(res, 503)
