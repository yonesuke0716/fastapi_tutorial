from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


class DatasetIn(BaseModel):
    X_train: str
    X_test: str
    y_train: str
    y_test: str


app = FastAPI()


@app.post("/")
def eval_regression(df_in: DatasetIn):
    X_train = pd.read_json(df_in.X_train)
    X_test = pd.read_json(df_in.X_test)
    y_train = pd.read_json(df_in.y_train)
    y_test = pd.read_json(df_in.y_test)

    # 回帰モデルの作成
    reg = LinearRegression()

    # 学習
    reg.fit(X_train, y_train)

    # 学習データに対するmodelの性能評価
    model_train_pred = reg.predict(X_train)
    model_train_mse = mean_squared_error(y_train, model_train_pred)
    model_train_rmse = np.sqrt(model_train_mse)
    print(model_train_rmse)

    # 訓練データに対するmodelの性能評価
    model_test_pred = reg.predict(X_test)
    model_test_mse = mean_squared_error(y_test, model_test_pred)
    model_test_rmse = np.sqrt(model_test_mse)

    return {"train_RMSE": model_train_rmse, "test_RMSE": model_test_rmse}
