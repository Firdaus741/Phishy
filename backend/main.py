from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel, ConfigDict, Field

from analysis import analyze
from classifier import PhishingClassifier
from link_checks import VirusTotal


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.clf = PhishingClassifier()  # load the model once, not per request
    app.state.vt = VirusTotal()           # key from backend/.env (VT_API_KEY); works without one
    yield


app = FastAPI(title="Phishy API", lifespan=lifespan)


class PredictRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    subject: str = ""
    body: str = ""                     # plain-text body
    html: str = ""                     # HTML body, used only if the plain-text body is empty
    sender: str = Field("", alias="from")
    reply_to: str = ""
    authentication_results: str = ""   # topmost Authentication-Results header (added by Gmail)


@app.get("/health")
def health(request: Request):
    clf = getattr(request.app.state, "clf", None)
    vt = getattr(request.app.state, "vt", None)
    return {"status": "ok", "model_loaded": clf is not None, "model": clf.name if clf else None,
            "virustotal": {"enabled": bool(vt and vt.enabled), "requests_today": vt.requests_today() if vt else 0,
                           "daily_cap": vt.daily_cap if vt else None}}


@app.post("/predict")
def predict(req: PredictRequest, request: Request):
    result = analyze(request.app.state.clf, request.app.state.vt, subject=req.subject, body=req.body,
                     html=req.html, sender=req.sender, reply_to=req.reply_to,
                     authentication_results=req.authentication_results)
    if result is None:
        raise HTTPException(status_code=400, detail="no usable text in subject or body")
    return result
