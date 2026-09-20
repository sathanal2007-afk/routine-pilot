from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from database import SessionLocal
from models import RoutineTask, Vocabulary
from vocab_service import lookup_dictionary, get_daily_vocab
from notifier import send_telegram_message
import os

app = FastAPI(title="RoutinePilot Dashboard")

# Templates path setup
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")
templates = Jinja2Templates(directory=TEMPLATES_DIR)

# 1. Main Dashboard View
@app.get("/", response_class=HTMLResponse)
def read_dashboard(request: Request):
    db = SessionLocal()
    tasks = db.query(RoutineTask).order_by(RoutineTask.alert_time).all()
    vocab_words = get_daily_vocab(day=1)
    db.close()
    
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "tasks": tasks,
            "vocab_words": vocab_words,
            "dict_result": None
        }
    )

# 2. Add New Routine Task
@app.post("/add-task")
def add_task(title: str = Form(...), alert_time: str = Form(...), task_type: str = Form(...)):
    db = SessionLocal()
    new_task = RoutineTask(title=title, alert_time=alert_time, task_type=task_type)
    db.add(new_task)
    db.commit()
    db.close()
    return HTMLResponse("<script>window.location.href='/';</script>")

# 3. Dictionary Lookup
@app.post("/search-word", response_class=HTMLResponse)
def search_word(request: Request, word: str = Form(...)):
    db = SessionLocal()
    tasks = db.query(RoutineTask).order_by(RoutineTask.alert_time).all()
    vocab_words = get_daily_vocab(day=1)
    db.close()

    dict_result = lookup_dictionary(word)

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "tasks": tasks,
            "vocab_words": vocab_words,
            "dict_result": dict_result
        }
    )

# 4. Instant Test Alert Button
@app.post("/test-alert")
def trigger_alert():
    send_telegram_message("⚡ *Manual Alert from Web Dashboard!* \nஉங்க Dashboard ஒழுங்கா connect ஆகியிருக்கு!")
    return HTMLResponse("<script>alert('Telegram alert sent!'); window.location.href='/';</script>")