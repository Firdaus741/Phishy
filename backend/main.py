from fastapi import FastAPI

app = FastAPI(title="Phishy API")


@app.get("/health")
def health():
    return {"status": "ok"}