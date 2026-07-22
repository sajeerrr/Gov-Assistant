from fastapi import FastAPI

app = FastAPI(
    title="Government Schemes Assistant",
    version="1.0"
)


@app.get("/")
def home():
    return {
        "message": "Government Schemes Assistant API is running"
    }