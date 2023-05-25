import requests
import json
import pandas as pd


def main():
    url = "http://127.0.0.1:8000/"
    # data = {"cost": 100, "tax_rate": 0.1}
    df = pd.read_csv("test.csv")
    payload = {"json_str": df.to_json()}
    res = requests.post(url, json.dumps(payload))
    print(res.json())


if __name__ == "__main__":
    main()
