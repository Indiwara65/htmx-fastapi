from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.encoders import jsonable_encoder
import time

from typing import Annotated
from pydantic import BaseModel
import random

class userFormdata(BaseModel):
    uname:str
    password:str


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

@app.get("/jinga")
async def jinga(request:Request):
    return templates.TemplateResponse(request=request, context={'variableOne':"HelloWorld",
                                                                "variableTwo":{"One":"nestedHelloWorldOne",
                                                                               "Two":"nestedhelloWorldTwo"},
                                                                "variableThree":{"One":{"Two":"doubleNestedHelloWorld"}},
                                                                "PI":22/7,
                                                                'numberOne':11,
                                                                'fruits':['apple','chicken',
                                                                          'apple','chicken',
                                                                          'bannana']}, name='jinga.html')

@app.get("/login", response_class=HTMLResponse)
async def login(request:Request):
    return templates.TemplateResponse(request=request, name="login.html")

@app.get("/forms", response_class=HTMLResponse)
async def forms(request:Request):
    return templates.TemplateResponse(request=request, name="form.html")

@app.post("/login/login", response_class=JSONResponse)
async def login_login(userData:Annotated[userFormdata, Form()]):
    return userData

@app.get("/htmx", response_class=HTMLResponse)
async def forms(request:Request):
    return templates.TemplateResponse(request=request, name="htmx.html")


@app.get("/trigger-1", response_class=HTMLResponse)
async def trigger1(request:Request):
    return f"<p>Click Trigger</p>"

@app.get("/trigger-2", response_class=HTMLResponse)
async def trigger2(request:Request):
    return f"<p>Change Trigger</p>"

@app.get("/trigger-3", response_class=HTMLResponse)
async def trigger3(request:Request):
    return f"<p>KeyUp Trigger</p>"

@app.get("/trigger-4", response_class=HTMLResponse)
async def trigger4(request:Request):
    return f"<p>KeyDown Trigger</p>"

@app.get("/trigger-5", response_class=HTMLResponse)
async def trigger5(request:Request):
    return f"<p>Mouse moveover trigger</p>"

@app.get("/trigger-6", response_class=HTMLResponse)
async def trigger6(request:Request):
    price = round(random.uniform(10, 100),2)
    return f"<p>Stock Price : {price}</p>" 

@app.get("/trigger-7", response_class=HTMLResponse)
async def trigger7(request:Request):
    words = ["HelloWorld","HelloFromTheOtherSide","HellYeahBrother"]
    index = random.randint(0,2)
    return f"<p>{words[index]}</p>" 

@app.get("/trigger-8", response_class=HTMLResponse)
async def trigger8(request:Request):
    return f"<p>Revealed</p>" 

@app.get("/trigger-10", response_class=HTMLResponse)
async def trigger10(request:Request):
    print(request.body)
    return f"<p>Hello Login Triggered</p>" 

@app.get("/swap-1", response_class=HTMLResponse)
async def swap1(request:Request):
    return f"<p>Inner HTML SWAP</p>" 

@app.get("/swap-2", response_class=HTMLResponse)
async def swap2(request:Request):
    return f"<p>Entire input element was replaced by this paragraph</p>" 

@app.get("/swap-3", response_class=HTMLResponse)
async def swap2(request:Request):
    return f"<p>New paragraph element</p>"

@app.get("/indicator-1", response_class=HTMLResponse)
async def swap2(request:Request):
    time.sleep(2)
    return f"<p>Loaded</p>"

