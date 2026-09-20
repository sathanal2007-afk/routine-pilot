from database import SessionLocal
from models import User, RoutineTask, Vocabulary

def seed_data():
    db = SessionLocal()

    # 1. பழைய டேட்டா இருந்தால் மீண்டும் add ஆகாமல் தடுக்க check செய்தல்
    if db.query(RoutineTask).count() > 0:
        print("Data already seeded! Skipping...")
        db.close()
        return

    # 2. User Profile Setup (உங்க details)
    user = User(
        name="Student",
        telegram_chat_id="YOUR_CHAT_ID",  # அடுத்த step-ல் இதைப் பெறுவோம்
        wake_time="06:30",
        sleep_time="22:30",
        college_start="08:30",
        college_end="16:30"
    )
    db.add(user)

    # 3. Daily Routine Tasks (நேரம் & செய்ய வேண்டிய வேலை)
    tasks = [
        RoutineTask(title="Wake Up & Drink Water 💧", task_type="routine", alert_time="06:30"),
        RoutineTask(title="Learn 10 English Words 📖", task_type="vocab", alert_time="07:00"),
        RoutineTask(title="Evening Study: Core Tech / Coding 💻", task_type="study", alert_time="18:00"),
        RoutineTask(title="Quick 10-Min Walk & Break ☕", task_type="break", alert_time="18:45"),
        RoutineTask(title="Night Review & Sleep On Time 😴", task_type="routine", alert_time="22:30"),
    ]
    db.add_all(tasks)

    # 4. Day 1 - 10 Essential English Words with Tamil Meaning
    vocab_list = [
        Vocabulary(word="Resilient", tamil_meaning="மீண்டு வரக்கூடிய தன்மை", example="He is resilient and never gives up.", day_number=1),
        Vocabulary(word="Meticulous", tamil_meaning="மிகவும் நுணுக்கமான / கவனமான", example="She pays meticulous attention to detail.", day_number=1),
        Vocabulary(word="Pragmatic", tamil_meaning="நடைமுறைக்கு ஏற்ற", example="We need a pragmatic solution to this problem.", day_number=1),
        Vocabulary(word="Eloquent", tamil_meaning="தெளிவாக / சரளமாக பேசும் திறன்", example="His speech was powerful and eloquent.", day_number=1),
        Vocabulary(word="Lucid", tamil_meaning="எளிதில் புரியக்கூடிய / தெளிவான", example="The explanation was lucid and simple.", day_number=1),
        Vocabulary(word="Vigilant", tamil_meaning="விழிப்புடன் இருத்தல்", example="Be vigilant while working on system security.", day_number=1),
        Vocabulary(word="Concise", tamil_meaning="சுருக்கமான மற்றும் தெளிவான", example="Keep your resume summary concise.", day_number=1),
        Vocabulary(word="Amicable", tamil_meaning="நட்பான / சுமுகமான", example="They reached an amicable agreement.", day_number=1),
        Vocabulary(word="Tenacious", tamil_meaning="விடாமுயற்சியுடன் கூடிய", example="He has a tenacious pursuit of his goals.", day_number=1),
        Vocabulary(word="Innovate", tamil_meaning="புதிதாக உருவாக்கு / புகுத்து", example="Developers must constantly innovate.", day_number=1),
    ]
    db.add_all(vocab_list)

    db.commit()
    db.close()
    print("Default routine tasks and Day 1 vocabulary successfully inserted!")

if __name__ == "__main__":
    seed_data()