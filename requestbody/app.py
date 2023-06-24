import requests
import json


def main():
    url = "http://127.0.0.1:8000/"
    params = {"test_size": 0.5}
    res = requests.post(url, json.dumps(params))
    print(res.json())


if __name__ == "__main__":
    main()
