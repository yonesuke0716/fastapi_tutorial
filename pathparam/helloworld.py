from fastapi import FastAPI


app = FastAPI()


@app.get("/{name}")
def root(name: str):
    return {"message": f"Hello World {name}"}
