# 🚀 RoutinePilot — Student Daily Routine & English Co-Pilot

A lightweight, automated daily productivity and vocabulary assistant built for students. It combines a real-time FastAPI dashboard, dynamic routine scheduler, instant dictionary lookup, and automated Telegram alerts.

---

## 🌟 Key Features
- **⏰ Smart Daily Schedule:** Organize daily study slots, college hours, and break intervals.
- **🔔 Automated Telegram Alerts:** Background cron jobs via `APScheduler` send real-time reminders directly to your phone.
- **📚 Daily 10 Vocabulary Engine:** Delivers 10 curated English words with Tamil meanings and practical example sentences every day.
- **📖 Instant Dictionary Lookup:** Seamless integration with Free Dictionary API for word definitions, phonetics, and usage examples.
- **💻 Minimalist Web Dashboard:** Built with FastAPI, Jinja2 templates, and Tailwind CSS.

---

## 🛠️ Tech Stack
- **Backend:** Python, FastAPI, Uvicorn
- **Task Scheduling:** APScheduler (Advanced Python Scheduler)
- **Database:** SQLite with SQLAlchemy ORM
- **Frontend:** Jinja2 Templates, Tailwind CSS
- **APIs & Integrations:** Telegram Bot API, Free Dictionary API

---

## 📁 Project Architecture
```text
routine-pilot/
├── templates/
│   └── index.html         # Tailwind CSS Dashboard UI
├── database.py            # SQLite connection engine
├── models.py              # SQLAlchemy database schemas
├── seed.py                # Initial routine and vocabulary seeder
├── vocab_service.py       # Dictionary API & vocab queries
├── notifier.py            # Telegram Bot alert integration
├── scheduler.py           # APScheduler background runner
├── main.py                # FastAPI web application routes
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation