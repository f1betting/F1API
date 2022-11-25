#################
# CIRCUITS DATA #
#################

def get_albert_park_data(timestamp):
    return {
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


def get_albert_park_response(timestamp=None):
    return {
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


def get_placeholder_data(timestamp):
    return {
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
