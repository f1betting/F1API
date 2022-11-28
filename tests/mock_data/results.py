#####################
# RACE RESULTS DATA #
#####################

def get_race_results_data(timestamp):
    return {
        "MRData": {
            "xmlns": "https://://ergast.com/mrd/1.5",
            "series": "f1",
            "url": "https://://ergast.com/api/f1/2022/15/results.json",
            "limit": "30",
            "offset": "0",
            "total": "20",
            "RaceTable": {
                "season": "2022",
                "round": "15",
                "Races": [
                    {
                        "season": "2022",
                        "round": "15",
                        "url": "https://://en.wikipedia.org/wiki/2022_Dutch_Grand_Prix",
                        "raceName": "Dutch Grand Prix",
                        "Circuit": {
                            "circuitId": "zandvoort",
                            "url": "https://://en.wikipedia.org/wiki/Circuit_Zandvoort",
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
                        "Results": [
                            {
                                "number": "1",
                                "position": "1",
                                "positionText": "1",
                                "points": "26",
                                "Driver": {
                                    "driverId": "max_verstappen",
                                    "permanentNumber": "33",
                                    "code": "VER",
                                    "url": "https://://en.wikipedia.org/wiki/Max_Verstappen",
                                    "givenName": "Max",
                                    "familyName": "Verstappen",
                                    "dateOfBirth": "1997-09-30",
                                    "nationality": "Dutch"
                                },
                                "Constructor": {
                                    "constructorId": "red_bull",
                                    "url": "https://://en.wikipedia.org/wiki/Red_Bull_Racing",
                                    "name": "Red Bull",
                                    "nationality": "Austrian"
                                },
                                "grid": "1",
                                "laps": "72",
                                "status": "Finished",
                                "Time": {
                                    "millis": "5802773",
                                    "time": "1:36:42.773"
                                },
                                "FastestLap": {
                                    "rank": "1",
                                    "lap": "62",
                                    "Time": {
                                        "time": "1:13.652"
                                    },
                                    "AverageSpeed": {
                                        "units": "kph",
                                        "speed": "208.173"
                                    }
                                }
                            }
                        ],
                    }
                ]
            }
        },
        "timestamp": timestamp
    }


def get_race_results_response(timestamp=None):
    return {
        "timestamp": timestamp,
        "results": [
            {
                "timestamp": None,
                "number": 1,
                "position": 1,
                "positionText": "1",
                "points": 26,
                "Driver": {
                    "timestamp": None,
                    "driverId": "max_verstappen",
                    "url": "https://://en.wikipedia.org/wiki/Max_Verstappen",
                    "givenName": "Max",
                    "familyName": "Verstappen",
                    "dateOfBirth": "1997-09-30",
                    "nationality": "Dutch",
                    "permanentNumber": 33,
                    "code": "VER"
                },
                "Constructor": {
                    "timestamp": None,
                    "constructorId": "red_bull",
                    "url": "https://://en.wikipedia.org/wiki/Red_Bull_Racing",
                    "name": "Red Bull",
                    "nationality": "Austrian"
                },
                "grid": 1,
                "laps": 72,
                "status": "Finished",
                "Time": {
                    "time": "1:36:42.773",
                    "millis": "5802773"
                },
                "FastestLap": {
                    "rank": 1,
                    "lap": 62,
                    "Time": {
                        "time": "1:13.652",
                        "millis": None
                    },
                    "AverageSpeed": {
                        "units": "kph",
                        "speed": 208.173
                    }
                }
            }
        ]
    }


def get_race_results_placeholder_data(timestamp):
    return {
        "MRData": {
            "xmlns": "https://://ergast.com/mrd/1.5",
            "series": "f1",
            "url": "https://://ergast.com/api/f1/2022/placeholder/results.json",
            "limit": "30",
            "offset": "0",
            "total": "0",
            "RaceTable": {
                "season": "2022",
                "round": "-1",
                "Races": []
            }
        },
        "timestamp": timestamp
    }


###########################
# QUALIFYING RESULTS DATA #
###########################

def get_qualifying_results_data(timestamp):
    return {
        "MRData": {
            "xmlns": "https://://ergast.com/mrd/1.5",
            "series": "f1",
            "url": "https://://ergast.com/api/f1/2022/15/qualifying.json",
            "limit": "30",
            "offset": "0",
            "total": "20",
            "RaceTable": {
                "season": "2022",
                "round": "15",
                "Races": [
                    {
                        "season": "2022",
                        "round": "15",
                        "url": "https://://en.wikipedia.org/wiki/2022_Dutch_Grand_Prix",
                        "raceName": "Dutch Grand Prix",
                        "Circuit": {
                            "circuitId": "zandvoort",
                            "url": "https://://en.wikipedia.org/wiki/Circuit_Zandvoort",
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
                        "QualifyingResults": [
                            {
                                "number": "1",
                                "position": "1",
                                "Driver": {
                                    "driverId": "max_verstappen",
                                    "permanentNumber": "33",
                                    "code": "VER",
                                    "url": "https://://en.wikipedia.org/wiki/Max_Verstappen",
                                    "givenName": "Max",
                                    "familyName": "Verstappen",
                                    "dateOfBirth": "1997-09-30",
                                    "nationality": "Dutch"
                                },
                                "Constructor": {
                                    "constructorId": "red_bull",
                                    "url": "https://://en.wikipedia.org/wiki/Red_Bull_Racing",
                                    "name": "Red Bull",
                                    "nationality": "Austrian"
                                },
                                "Q1": "1:11.317",
                                "Q2": "1:10.927",
                                "Q3": "1:10.342"
                            },
                        ],
                    }
                ]
            }
        },
        "timestamp": timestamp
    }


def get_qualifying_results_response(timestamp=None):
    return {
        "timestamp": timestamp,
        "results": [
            {
                "timestamp": None,
                "number": 1,
                "position": 1,
                "Driver": {
                    "timestamp": None,
                    "driverId": "max_verstappen",
                    "url": "https://://en.wikipedia.org/wiki/Max_Verstappen",
                    "givenName": "Max",
                    "familyName": "Verstappen",
                    "dateOfBirth": "1997-09-30",
                    "nationality": "Dutch",
                    "permanentNumber": 33,
                    "code": "VER"
                },
                "Constructor": {
                    "timestamp": None,
                    "constructorId": "red_bull",
                    "url": "https://://en.wikipedia.org/wiki/Red_Bull_Racing",
                    "name": "Red Bull",
                    "nationality": "Austrian"
                },
                "Q1": "1:11.317",
                "Q2": "1:10.927",
                "Q3": "1:10.342"
            },
        ]
    }


def get_qualifying_results_placeholder_data(timestamp):
    return {
        "MRData": {
            "xmlns": "https://://ergast.com/mrd/1.5",
            "series": "f1",
            "url": "https://://ergast.com/api/f1/2022/placeholder/qualifying.json",
            "limit": "30",
            "offset": "0",
            "total": "0",
            "RaceTable": {
                "season": "2022",
                "round": "-1",
                "Races": []
            }
        },
        "timestamp": timestamp
    }


#########################
# DRIVER STANDINGS DATA #
#########################

def get_driver_standings_data(timestamp):
    return {
        "MRData": {
            "xmlns": "https://://ergast.com/mrd/1.5",
            "series": "f1",
            "url": "https://://ergast.com/api/f1/2022/driverstandings.json",
            "limit": "30",
            "offset": "0",
            "total": "22",
            "StandingsTable": {
                "season": "2022",
                "StandingsLists": [
                    {
                        "season": "2022",
                        "round": "22",
                        "DriverStandings": [
                            {
                                "position": "1",
                                "positionText": "1",
                                "points": "454",
                                "wins": "15",
                                "Driver": {
                                    "driverId": "max_verstappen",
                                    "permanentNumber": "33",
                                    "code": "VER",
                                    "url": "https://://en.wikipedia.org/wiki/Max_Verstappen",
                                    "givenName": "Max",
                                    "familyName": "Verstappen",
                                    "dateOfBirth": "1997-09-30",
                                    "nationality": "Dutch"
                                },
                                "Constructors": [
                                    {
                                        "constructorId": "red_bull",
                                        "url": "https://://en.wikipedia.org/wiki/Red_Bull_Racing",
                                        "name": "Red Bull",
                                        "nationality": "Austrian"
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        },
        "timestamp": timestamp
    }


def get_driver_standings_response(timestamp=None):
    return {
        "timestamp": timestamp,
        "standings": [
            {
                "timestamp": None,
                "position": 1,
                "positionText": "1",
                "points": 454,
                "wins": 15,
                "Driver": {
                    "timestamp": None,
                    "driverId": "max_verstappen",
                    "url": "https://://en.wikipedia.org/wiki/Max_Verstappen",
                    "givenName": "Max",
                    "familyName": "Verstappen",
                    "dateOfBirth": "1997-09-30",
                    "nationality": "Dutch",
                    "permanentNumber": 33,
                    "code": "VER"
                },
                "Constructors": [
                    {
                        "timestamp": None,
                        "constructorId": "red_bull",
                        "url": "https://://en.wikipedia.org/wiki/Red_Bull_Racing",
                        "name": "Red Bull",
                        "nationality": "Austrian"
                    }
                ]
            }
        ]
    }


def get_driver_standings_placeholder_data(timestamp):
    return {
        "MRData": {
            "xmlns": "https://://ergast.com/mrd/1.5",
            "series": "f1",
            "url": "https://://ergast.com/api/f1/placeholder/driverstandings.json",
            "limit": "30",
            "offset": "0",
            "total": "0",
            "StandingsTable": {
                "season": "placeholder",
                "StandingsLists": []
            }
        },
        "timestamp": timestamp
    }


##############################
# CONSTRUCTOR STANDINGS DATA #
##############################

def get_constructor_standings_data(timestamp):
    return {
        "MRData": {
            "xmlns": "https://://ergast.com/mrd/1.5",
            "series": "f1",
            "url": "https://://ergast.com/api/f1/2022/constructorstandings.json",
            "limit": "30",
            "offset": "0",
            "total": "10",
            "StandingsTable": {
                "season": "2022",
                "StandingsLists": [
                    {
                        "season": "2022",
                        "round": "22",
                        "ConstructorStandings": [
                            {
                                "position": "1",
                                "positionText": "1",
                                "points": "759",
                                "wins": "17",
                                "Constructor": {
                                    "constructorId": "red_bull",
                                    "url": "https://://en.wikipedia.org/wiki/Red_Bull_Racing",
                                    "name": "Red Bull",
                                    "nationality": "Austrian"
                                }
                            }
                        ]
                    }
                ]
            }
        },
        "timestamp": timestamp
    }


def get_constructor_standings_response(timestamp=None):
    return {
        "timestamp": timestamp,
        "standings": [
            {
                "timestamp": None,
                "position": 1,
                "positionText": "1",
                "points": 759,
                "wins": 17,
                "Constructor": {
                    "timestamp": None,
                    "constructorId": "red_bull",
                    "url": "https://://en.wikipedia.org/wiki/Red_Bull_Racing",
                    "name": "Red Bull",
                    "nationality": "Austrian"
                }
            }
        ]
    }


def get_constructor_standings_placeholder_data(timestamp):
    return {
        "MRData": {
            "xmlns": "https://://ergast.com/mrd/1.5",
            "series": "f1",
            "url": "https://://ergast.com/api/f1/placeholder/constructorStandings.json",
            "limit": "30",
            "offset": "0",
            "total": "0",
            "StandingsTable": {
                "season": "placeholder",
                "StandingsLists": []
            }
        },
        "timestamp": timestamp
    }
