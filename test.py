import requests
import json


def main():
    url = "http://127.0.0.1:8000/"
    data = {"cost": 100, "tax_rate": 0.1}

    # ここでAPIを呼び出す,データはjson形式でないとエラーが起きる
    res = requests.post(url, json.dumps(data))
    print(res.json())


if __name__ == "__main__":
    main()
