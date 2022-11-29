import unittest

from fastapi.testclient import TestClient

from app.main import app
from tests.logic.mock_cache import delete_cache_file, mock_cache, empty_cache_data
from tests.mock_data.mock_calendar import *


class TestCalendar(unittest.TestCase):
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
            delete_cache_file(file)

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

        mock_cache(get_season_data, "get_calendar_by_season.2022")

        res = self.test_client.get("/calendar/2022").json()

        event_data = next(race for race in res["events"] if race["raceName"] == "Dutch Grand Prix")

        data = get_season_response()

        self.assertEqual(event_data, data)

    def test_calendar_by_season_404(self):
        """
        Test 404 response on /calendar/{season} endpoint with 0 as example
        """

        mock_cache(get_season_placeholder_data, "get_calendar_by_season.0")

        res = self.test_client.get("/calendar/0").status_code

        self.assertEqual(res, 404)

    def test_calendar_by_season_503(self):
        """
        Test 503 response on /calendar/{season} endpoint with 0 as example
        """

        mock_cache(empty_cache_data, "get_calendar_by_season.0")

        res = self.test_client.get("/calendar/0").status_code

        self.assertEqual(res, 503)

    ###############
    # /event/next #
    ###############

    def test_get_next_race(self):
        """
        Test 200 response on /event/next
        """

        timestamp = mock_cache(get_next_race_data, "get_next_race")

        res = self.test_client.get("/event/next").json()

        data = get_next_race_response(timestamp)

        self.assertEqual(res, data)

    def test_get_next_race_503(self):
        """
        Test 503 response on /event/next endpoint with 0 as example
        """

        mock_cache(empty_cache_data, "get_next_race")

        res = self.test_client.get("/event/next").status_code

        self.assertEqual(res, 503)

    ###################
    # /event/previous #
    ###################

    def test_get_previous_race(self):
        """
        Test 200 response on /event/previous
        """

        timestamp = mock_cache(get_previous_race_data, "get_previous_race")

        res = self.test_client.get("/event/previous").json()

        data = get_previous_race_response(timestamp)

        self.assertEqual(res, data)

    def test_get_previous_race_503(self):
        """
        Test 503 response on /event/previous endpoint with 0 as example
        """

        mock_cache(empty_cache_data, "get_previous_race")

        res = self.test_client.get("/event/previous").status_code

        self.assertEqual(res, 503)

        ###########################
        # /event/{season}/{round} #
        ###########################

    def test_get_event_details(self):
        """
        Test 200 response on /event/{season}/{round} endpoint with season 2022 round 15 as example
        """

        timestamp = mock_cache(get_event_details_data, "get_event_details.2022.15")

        res = self.test_client.get("/event/2022/15").json()

        data = get_event_details_response(timestamp)

        self.assertEqual(res, data)

    def test_get_event_details_404(self):
        """
        Test 404 response on /event/{season}/{round} endpoint with season 2022 round -1 as example
        """

        mock_cache(get_event_details_placeholder, "get_event_details.2022.-1")

        res = self.test_client.get("/event/2022/-1").status_code

        self.assertEqual(res, 404)

    def test_get_event_details_503(self):
        """
        Test 503 response on on /event/{season}/{round} endpoint with season 0 round 0 as example
        """

        mock_cache(empty_cache_data, "get_event_details.0.0")

        res = self.test_client.get("/event/0/0").status_code

        self.assertEqual(res, 503)
