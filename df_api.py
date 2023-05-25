from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd


class TaxIn(BaseModel):
    cost: int
    tax_rate: float


class RecipeIn(BaseModel):
    json_str: str


app = FastAPI()


@app.post("/")
def calc(df_in: RecipeIn):
    # in_tax_cost = data.cost * (1 + data.tax_rate)
    df = pd.read_json(df_in.json_str)
    return {"output": df.columns.to_list()}
