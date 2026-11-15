import os
from contextlib import asynccontextmanager
from email.utils import parseaddr

from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel, ConfigDict, Field

from classifier import PhishingClassifier
from header_checks import check_headers
from link_checks import VirusTotal, check_links

# Placeholder cutoff for the text model alone. The final Safe/Phishing verdict will combine
# text, header and link signals; this value is only what /predict reports for the text part.
TEXT_THRESHOLD = float(os.environ.get("PHISHY_TEXT_THRESHOLD", "0.5"))


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
    clf: PhishingClassifier = request.app.state.clf
    prob, text = clf.score_email(req.subject, req.body, req.html)
    if not text:
        raise HTTPException(status_code=400, detail="no usable text in subject or body")
    headers = check_headers({
        "from": req.sender, "reply_to": req.reply_to,
        "authentication_results": req.authentication_results,
    })
    sender_domain = parseaddr(req.sender)[1].rsplit("@", 1)[-1] if "@" in parseaddr(req.sender)[1] else ""
    links = check_links(req.body, req.html, request.app.state.vt, sender_domain)
    return {
        "phishing_probability": round(prob, 4),
        "text_label": "phishing" if prob >= TEXT_THRESHOLD else "safe",
        "threshold": TEXT_THRESHOLD,
        "model": clf.name,
        "headers": headers,
        "links": links,
    }
