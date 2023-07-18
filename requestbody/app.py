import requests
import json


def main():
    url = "http://127.0.0.1:8000/"
    params = {"random_state": 1, "test_size": 0.5, "is_shuffle": True, "test_number": 1}
    res = requests.post(url, json.dumps(params))
    print(res.json())


if __name__ == "__main__":
    main()
