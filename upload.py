from fastapi import FastAPI
import pandas as pd

app = FastAPI()


@app.post("/receive_df")
def receive_df(df_in: str):
    print(df_in)
    df = pd.DataFrame.read_json(df_in)
    return {"df": df.head()}
