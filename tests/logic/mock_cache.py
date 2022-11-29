import json
import os
import time


def mock_cache(mock_data, file_name: str):
    delete_cache_file(file_name)

    full_path = f"./app/cache/{file_name}.json"

    timestamp = float(time.time())

    data = mock_data(timestamp)

    cache_file = open(full_path, "w+")
    cache_file.write(json.dumps(data))
    cache_file.close()

    return timestamp


def empty_cache_data(timestamp):
    return {
        "timestamp": timestamp
    }


def delete_cache_file(file):
    if os.path.exists(f"./app/cache/{file}.json"):
        os.remove(f"./app/cache/{file}.json")
        print(f"Deleted {file}.json")
