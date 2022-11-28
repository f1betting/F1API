#####################
# CONSTRUCTORS DATA #
#####################

def get_red_bull_data(timestamp):
    return {
        "MRData": {
            "xmlns": "https://://ergast.com/mrd/1.5",
            "series": "f1",
            "url": "https://://ergast.com/api/f1/constructors/red_bull.json",
            "limit": "30",
            "offset": "0",
            "total": "1",
            "ConstructorTable": {
                "constructorId": "red_bull",
                "Constructors": [
                    {
                        "constructorId": "red_bull",
                        "url": "https://://en.wikipedia.org/wiki/Red_Bull_Racing",
                        "name": "Red Bull",
                        "nationality": "Austrian"
                    }
                ]
            }
        },
        "timestamp": timestamp
    }


def get_red_bull_response(timestamp=None):
    return {
        "timestamp": timestamp,
        "constructorId": "red_bull",
        "url": "https://://en.wikipedia.org/wiki/Red_Bull_Racing",
        "name": "Red Bull",
        "nationality": "Austrian"
    }


def get_placeholder_data(timestamp):
    return {
        "MRData": {
            "xmlns": "https://://ergast.com/mrd/1.5",
            "series": "f1",
            "url": "https://://ergast.com/api/f1/constructors/placeholder.json",
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
