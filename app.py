import requests
import json
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split


def main():
    url = "http://127.0.0.1:8000/"
    # california データセットを読み込む
    california_housing = fetch_california_housing()
    X = pd.DataFrame(california_housing.data, columns=california_housing.feature_names)
    y = pd.DataFrame(california_housing.target)
    # 訓練データとテストデータに分割する
    X_train, X_test, y_train, y_test = train_test_split(X, y)
    df_in = {
        "X_train": X_train.to_json(),
        "X_test": X_test.to_json(),
        "y_train": y_train.to_json(),
        "y_test": y_test.to_json(),
    }
    res = requests.post(url, json.dumps(df_in))
    print(res.json())


if __name__ == "__main__":
    main()
