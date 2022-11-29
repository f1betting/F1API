###############
# SEASON DATA #
###############

def get_season_data(timestamp):
    return {
        "MRData": {
            "xmlns": "https://ergast.com/mrd/1.5",
            "series": "f1",
            "url": "https://ergast.com/api/f1/2022.json",
            "limit": "30",
            "offset": "0",
            "total": "22",
            "RaceTable": {
                "season": "2022",
                "Races": [
                    {
                        "season": "2022",
                        "round": "15",
                        "url": "https://en.wikipedia.org/wiki/2022_Dutch_Grand_Prix",
                        "raceName": "Dutch Grand Prix",
                        "Circuit": {
                            "circuitId": "zandvoort",
                            "url": "https://en.wikipedia.org/wiki/Circuit_Zandvoort",
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


def get_season_response():
    return {
        "timestamp": None,
        "season": 2022,
        "round": 15,
        "url": "https://en.wikipedia.org/wiki/2022_Dutch_Grand_Prix",
        "raceName": "Dutch Grand Prix",
        "Circuit": {
            "timestamp": None,
            "circuitId": "zandvoort",
            "url": "https://en.wikipedia.org/wiki/Circuit_Zandvoort",
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


def get_season_placeholder_data(timestamp):
    return {
        "MRData": {
            "xmlns": "https://ergast.com/mrd/1.5",
            "series": "f1",
            "url": "https://ergast.com/api/f1/placeholder.json",
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


##################
# NEXT RACE DATA #
##################

def get_next_race_data(timestamp):
    return {
        "MRData": {
            "xmlns": "https://ergast.com/mrd/1.5",
            "series": "f1",
            "url": "https://ergast.com/api/f1/current/next.json",
            "limit": "30",
            "offset": "0",
            "total": "0",
            "RaceTable": {
                "season": "2023",
                "round": "1",
                "Races": []
            }
        },
        "timestamp": timestamp
    }


def get_next_race_response(timestamp):
    return {
        "timestamp": timestamp,
        "season": 2023,
        "round": 1
    }


######################
# PREVIOUS RACE DATA #
######################

def get_previous_race_data(timestamp):
    return {
        "MRData": {
            "xmlns": "https://ergast.com/mrd/1.5",
            "series": "f1",
            "url": "https://ergast.com/api/f1/current/last.json",
            "limit": "30",
            "offset": "0",
            "total": "1",
            "RaceTable": {
                "season": "2022",
                "round": "22",
                "Races": [
                    {
                        "season": "2022",
                        "round": "22",
                        "url": "https://en.wikipedia.org/wiki/2022_Abu_Dhabi_Grand_Prix",
                        "raceName": "Abu Dhabi Grand Prix",
                        "Circuit": {
                            "circuitId": "yas_marina",
                            "url": "https://en.wikipedia.org/wiki/Yas_Marina_Circuit",
                            "circuitName": "Yas Marina Circuit",
                            "Location": {
                                "lat": "24.4672",
                                "long": "54.6031",
                                "locality": "Abu Dhabi",
                                "country": "UAE"
                            }
                        },
                        "date": "2022-11-20",
                        "time": "13:00:00Z",
                        "FirstPractice": {
                            "date": "2022-11-18",
                            "time": "10:00:00Z"
                        },
                        "SecondPractice": {
                            "date": "2022-11-18",
                            "time": "13:00:00Z"
                        },
                        "ThirdPractice": {
                            "date": "2022-11-19",
                            "time": "11:00:00Z"
                        },
                        "Qualifying": {
                            "date": "2022-11-19",
                            "time": "14:00:00Z"
                        }
                    }
                ]
            }
        },
        "timestamp": timestamp
    }


def get_previous_race_response(timestamp):
    return {
        "timestamp": timestamp,
        "season": 2022,
        "round": 22
    }


##############
# EVENT DATA #
##############


def get_event_details_data(timestamp):
    return {
        "MRData": {
            "xmlns": "https://ergast.com/mrd/1.5",
            "series": "f1",
            "url": "https://ergast.com/api/f1/2022/15.json",
            "limit": "30",
            "offset": "0",
            "total": "1",
            "RaceTable": {
                "season": "2022",
                "round": "15",
                "Races": [
                    {
                        "season": "2022",
                        "round": "15",
                        "url": "https://en.wikipedia.org/wiki/2022_Dutch_Grand_Prix",
                        "raceName": "Dutch Grand Prix",
                        "Circuit": {
                            "circuitId": "zandvoort",
                            "url": "https://en.wikipedia.org/wiki/Circuit_Zandvoort",
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


def get_event_details_response(timestamp=None):
    return {
        "timestamp": timestamp,
        "season": 2022,
        "round": 15,
        "url": "https://en.wikipedia.org/wiki/2022_Dutch_Grand_Prix",
        "raceName": "Dutch Grand Prix",
        "Circuit": {
            "timestamp": None,
            "circuitId": "zandvoort",
            "url": "https://en.wikipedia.org/wiki/Circuit_Zandvoort",
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


def get_event_details_placeholder(timestamp):
    return {
        "MRData": {
            "xmlns": "https://ergast.com/mrd/1.5",
            "series": "f1",
            "url": "https://ergast.com/api/f1/placeholder/placeholder.json",
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
