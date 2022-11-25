################
# DRIVERS DATA #
################

def get_max_verstappen_data(timestamp):
    return {
        "MRData": {
            "xmlns": "http://ergast.com/mrd/1.5",
            "series": "f1",
            "url": "http://ergast.com/api/f1/drivers/max_verstappen.json",
            "limit": "30",
            "offset": "0",
            "total": "1",
            "DriverTable": {
                "driverId": "max_verstappen",
                "Drivers": [
                    {
                        "driverId": "max_verstappen",
                        "permanentNumber": "33",
                        "code": "VER",
                        "url": "http://en.wikipedia.org/wiki/Max_Verstappen",
                        "givenName": "Max",
                        "familyName": "Verstappen",
                        "dateOfBirth": "1997-09-30",
                        "nationality": "Dutch"
                    }
                ]
            }
        },
        "timestamp": timestamp
    }


def get_max_verstappen_response(timestamp=None):
    return {
        "timestamp": timestamp,
        "driverId": "max_verstappen",
        "url": "http://en.wikipedia.org/wiki/Max_Verstappen",
        "givenName": "Max",
        "familyName": "Verstappen",
        "dateOfBirth": "1997-09-30",
        "nationality": "Dutch",
        "permanentNumber": 33,
        "code": "VER"
    }


def get_placeholder_data(timestamp):
    return {
        "MRData": {
            "xmlns": "http://ergast.com/mrd/1.5",
            "series": "f1",
            "url": "http://ergast.com/api/f1/drivers/placeholder.json",
            "limit": "30",
            "offset": "0",
            "total": "0",
            "DriverTable": {
                "driverId": "placeholder",
                "Drivers": []
            }
        },
        "timestamp": timestamp
    }
