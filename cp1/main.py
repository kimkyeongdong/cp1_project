from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/assets", StaticFiles(directory="assets"), name="assets")
# 정적경로 설정해주기위해서 설정 불러올때 이안에서 불러와야함

@app.get("/")
def index():
    return FileResponse("templates/index.html")

@app.get("/lda")
def lda():
    return FileResponse("templates/lda_pre.html")

@app.get("/ngram")
def ngram():
    return FileResponse("templates/ngram.html")

@app.get("/dash")
def dash():
    return FileResponse("templates/dash.html")

@app.get("/detail")
def detail():
    return FileResponse("templates/detail.html")