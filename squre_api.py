from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def calc(df_in: RecipeIn):
    # in_tax_cost = data.cost * (1 + data.tax_rate)
    df = pd.read_json(df_in.json_str)
    return {"output": df.columns.to_list()}
