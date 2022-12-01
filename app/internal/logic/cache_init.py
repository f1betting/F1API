import json
import os
import time
from json import JSONDecodeError
from pathlib import Path

import requests


def cache_init(file_name, duration):
    json_dump = None

    base_path = Path(__file__).parent

    full_path = base_path / f"../../cache/{file_name}.json"

    try:
        with open(full_path, "r", encoding="utf-8") as cache_file:
            json_dump = cache_file.read()

    except FileNotFoundError:
        open(full_path, "x", encoding="utf-8").close()  # pylint: disable=consider-using-with

    current_timestamp = float(time.time())

    if json_dump:
        json_file = json.loads(json_dump)

        cache_timestamp = json_file["timestamp"]

        if current_timestamp < float(cache_timestamp) + duration:
            return [True, json_file, float(cache_timestamp)]

        return [False, json_file, current_timestamp]
    return [None, {}, current_timestamp]


def cache_write(cache, file_name):
    base_path = Path(__file__).parent

    full_path = base_path / f"../../cache/{file_name}.json"

    with open(full_path, "w+", encoding="utf-8") as cache_file:
        cache["timestamp"] = float(time.time())
        cache_file.write(json.dumps(cache))


def invalidate_cache(file_name):
    base_path = Path(__file__).parent

    os.remove(base_path / f"../../cache/{file_name}.json")


def get_cache(url, path, duration=3600):
    status, cache, timestamp = cache_init(path, duration)

    match status:
        case True:
            return [cache, timestamp]
        case False:
            try:
                data = requests.get(url, timeout=5).json()

                cache_write(data, path)
            except JSONDecodeError:  # pragma: no coverage
                pass
            finally:
                return [cache, timestamp]
        case None:
            try:
                data = requests.get(url, timeout=5).json()
            except JSONDecodeError:  # pragma: no coverage
                data = {}

            cache_write(data, path)
            return [data, timestamp]

    # What are you doing here???
    return [{}, timestamp]  # pragma: no coverage
