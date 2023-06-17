from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import numpy as np

from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


class ModelParam(BaseModel):
    test_size: float


app = FastAPI()


@app.post("/")
def eval_california_price_rmse(params: ModelParam):
    california_housing = fetch_california_housing()
    X = pd.DataFrame(california_housing.data, columns=california_housing.feature_names)
    y = pd.DataFrame(california_housing.target)
    # 訓練データとテストデータに分割する
    print(params.test_size)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=params.test_size)
    # 回帰モデルの作成
    reg = LinearRegression()

    # 学習
    reg.fit(X_train, y_train)

    # 学習データに対するmodelの性能評価
    model_train_pred = reg.predict(X_train)
    model_train_mse = mean_squared_error(y_train, model_train_pred)
    model_train_rmse = np.sqrt(model_train_mse)

    # 訓練データに対するmodelの性能評価
    model_test_pred = reg.predict(X_test)
    model_test_mse = mean_squared_error(y_test, model_test_pred)
    model_test_rmse = np.sqrt(model_test_mse)

    return {"train_RMSE": model_train_rmse, "test_RMSE": model_test_rmse}
