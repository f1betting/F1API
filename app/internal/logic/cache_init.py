import json
import time
from json import JSONDecodeError
from pathlib import Path

import requests


def cache_init(file_name, duration):
    json_dump = None

    base_path = Path(__file__).parent

    full_path = base_path / f"../../cache/{file_name}.json"

    try:
        cache_file = open(full_path, "r")
        json_dump = cache_file.read()
        cache_file.close()

    except FileNotFoundError:
        open(full_path, "w").close()

    current_timestamp = float(time.time())

    if json_dump:
        json_file = json.loads(json_dump)

        cache_timestamp = 0

        if json_file["timestamp"]:
            cache_timestamp = json_file["timestamp"]

        if current_timestamp < float(cache_timestamp) + duration:
            return [True, json_file, float(cache_timestamp)]

        return [False, json_file, current_timestamp]
    return [None, {}, 0]


def cache_write(cache, file_name):
    base_path = Path(__file__).parent

    full_path = base_path / f"../../cache/{file_name}.json"

    cache_file = open(full_path, "w+")
    cache["timestamp"] = float(time.time())
    cache_file.write(json.dumps(cache))
    cache_file.close()


def get_cache(url, path, duration=3600):
    status, cache, timestamp = cache_init(path, duration)

    match status:
        case True:
            return [cache, timestamp]
        case False:
            try:
                data = requests.get(url).json()

                cache_write(data, path)
            except JSONDecodeError:
                pass
            finally:
                return [cache, timestamp]
        case None:
            try:
                data = requests.get(url).json()
            except JSONDecodeError:
                data = {}

            cache_write(data, path)
            return [data, timestamp]
