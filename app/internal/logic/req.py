import requests


def req(url):
    res = requests.get(url)
    return res.json()
