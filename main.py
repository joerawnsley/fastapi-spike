from fastapi import FastAPI,Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import os
from dotenv import load_dotenv
import psycopg

load_dotenv()

connection = psycopg.connect(
    user = os.getenv("DB_USER"),
    password = os.getenv("DB_PASSWORD"),
    host = os.getenv("DB_HOST"),
    port = os.getenv("DB_PORT"),
    dbname = os.getenv("DB_NAME")
)

print("main", connection)

app = FastAPI()
templates=Jinja2Templates(directory="templates")

@app.get("/")
def read_root():
    return RedirectResponse("/welcome")

@app.get("/welcome", response_class=HTMLResponse)
def read_items(request: Request, name: str = "Taybah"):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"name": name}
    )

@app.get("/coins")
def get_coins(): 
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM coins.coins")
        coins = cursor.fetchall()
        return coins

@app.post("/coins", status_code = status.HTTP_201_CREATED)
def insert_coin():
    with connection.cursor() as cursor:
        cursor.execute("INSERT into coins.coins (coin_name) VALUES ('Biscuit')")
        cursor.execute("SELECT * from coins.coins")
        coins = cursor.fetchall()
        return coins