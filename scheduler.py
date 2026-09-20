from apscheduler.schedulers.blocking import BlockingScheduler
from database import SessionLocal
from models import RoutineTask
from vocab_service import get_daily_vocab
from notifier import send_telegram_message
import datetime

scheduler = BlockingScheduler()

# 1. அன்றைய 10 ஆங்கில வார்த்தைகளை format செய்து அனுப்பும் function
def send_daily_vocab_alert():
    # தற்போதைக்கு Day 1 எடுக்கிறோம் (அடுத்த ஸ்டெப்பில் dynamic day tracker சேர்ப்போம்)
    words = get_daily_vocab(day=1)
    
    if not words:
        return

    message = "📚 *Daily 10 English Words for You!*\n\n"
    for i, item in enumerate(words, start=1):
        message += f"*{i}. {item.word}*\n"
        message += f"  • *தமிழ் அர்த்தம்:* {item.tamil_meaning}\n"
        message += f"  • *Example:* _{item.example}_\n\n"

    message += "💪 _இந்த 10 வார்த்தைகளையும் இன்னைக்கு பேசி/எழுதி பழகிடுங்க!_"
    send_telegram_message(message)
    print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] Daily Vocab sent to Telegram!")


# 2. Routine Task alert அனுப்பும் generic function
def trigger_task_alert(task_title: str):
    msg = f"⏰ *Routine Alert!*\n\n👉 *{task_title}*\n\nஇப்போ இந்த டாஸ்க்கை முடிக்க வேண்டிய நேரம். Let's do it! 🚀"
    send_telegram_message(msg)
    print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] Alert sent: {task_title}")


# 3. Database-ல் உள்ள routine-ஐப் படித்து scheduler-ல் register செய்தல்
def schedule_all_tasks():
    db = SessionLocal()
    tasks = db.query(RoutineTask).all()

    for task in tasks:
        # alert_time Format: "HH:MM" (e.g., "07:00", "18:00")
        hour, minute = map(int, task.alert_time.split(":"))

        if task.task_type == "vocab":
            # Vocab task என்றால் 10 வார்த்தைகள் format செய்து அனுப்பும்
            scheduler.add_job(
                send_daily_vocab_alert,
                'cron',
                hour=hour,
                minute=minute,
                id=f"task_{task.id}",
                replace_existing=True
            )
        else:
            # Routine / Study / Break task alerts
            scheduler.add_job(
                trigger_task_alert,
                'cron',
                hour=hour,
                minute=minute,
                args=[task.title],
                id=f"task_{task.id}",
                replace_existing=True
            )

        print(f"Scheduled: '{task.title}' at {task.alert_time} every day.")

    db.close()


if __name__ == "__main__":
    print("Initializing RoutinePilot Scheduler...")
    
    # உடனடி டெஸ்ட்: Script ஆன் ஆன உடனே ஒரு startup confirmation அனுப்பும்
    send_telegram_message("🤖 *RoutinePilot Scheduler is now Active!*\nஉங்க routine அட்டவணைப்படி சரியான நேரத்துக்கு alerts வரும்.")
    
    schedule_all_tasks()
    print("\nScheduler is running live. (Stop செய்ய Ctrl + C அழுத்தலாம்)...")
    
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        print("Scheduler stopped.")