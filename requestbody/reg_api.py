from fastapi import FastAPI
from pydantic import BaseModel

import pandas as pd

# import numpy as np

from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# from sklearn.metrics import mean_squared_error


class ModelParam(BaseModel):
    random_state: int
    test_size: float
    is_shuffle: bool
    test_number: int


app = FastAPI()


@app.post("/")
def calc_california_price(params: ModelParam):
    california_housing = fetch_california_housing()
    X = pd.DataFrame(california_housing.data, columns=california_housing.feature_names)
    y = pd.DataFrame(california_housing.target)
    # 訓練データとテストデータに分割する
    print(params.random_state, params.test_size, params.is_shuffle, params.test_size)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, random_state=params.random_state, test_size=params.test_size, shuffle=params.is_shuffle
    )
    # 回帰モデルの作成
    reg = LinearRegression()

    # 学習
    reg.fit(X_train, y_train)

    # 学習データに対するmodelの性能評価
    # model_train_pred = reg.predict(X_train)
    # model_train_mse = mean_squared_error(y_train, model_train_pred)
    # model_train_rmse = np.sqrt(model_train_mse)

    # 訓練データに対するmodelの性能評価
    model_test_pred = reg.predict(X_test)
    # model_test_mse = mean_squared_error(y_test, model_test_pred)
    # model_test_rmse = np.sqrt(model_test_mse)

    # return {"train_RMSE": model_train_rmse, "test_RMSE": model_test_rmse}
    pred_num = params.test_number
    # 上限設定
    if pred_num >= len(X_test):
        pred_num = len(X_test) - 1
    return {"predict": model_test_pred[pred_num][0], "answer": y_test.iloc[pred_num].values[0]}
