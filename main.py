from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.encoders import jsonable_encoder


templates = Jinja2Templates(directory='templates')

app = FastAPI()
app.mount("/static",StaticFiles(directory="static"),name="static")

@app.get("/", response_class=HTMLResponse)
async def index(request:Request):
    request_parameters = {"method":request.method,"url":request.url,"headers":request.headers,"cookies":request.cookies,
                             "client":request.client}
    print(request_parameters)
    return templates.TemplateResponse(request=request, name='index.html')

@app.get("/internal", response_class=HTMLResponse)
async def internal(request:Request):
    return templates.TemplateResponse(request=request, name='internal_css.html')

@app.get("/external", response_class=HTMLResponse)
async def external(request:Request):
    return templates.TemplateResponse(request=request,name='external_css.html')

@app.get("/table", response_class=HTMLResponse)
async def table(request:Request):
    return templates.TemplateResponse(request=request, context={}, name="tables.html")