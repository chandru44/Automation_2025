from fastapi import FastAPI
from analyzer import analyze_log

app = FastAPI()

@app.get("/")
def home():
    return {"message": "GenAI Cybersecurity Analyzer Running"}

@app.post("/analyze")
def analyze(log: dict):
    result = analyze_log(log)
    return {"analysis": result}
