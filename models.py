from sqlalchemy import Column, Integer, String, Boolean, Time
from database import Base, engine

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    telegram_chat_id = Column(String, nullable=False)  # Notifications வர
    wake_time = Column(String, default="06:30")        # Format: "HH:MM"
    sleep_time = Column(String, default="22:30")
    college_start = Column(String, default="08:30")
    college_end = Column(String, default="16:30")

class RoutineTask(Base):
    __tablename__ = "routine_tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)             # e.g., "Learn 10 Vocab", "Study Python"
    task_type = Column(String, nullable=False)         # study, break, vocab, routine
    alert_time = Column(String, nullable=False)        # Format: "HH:MM" (e.g., "07:00")
    is_completed = Column(Boolean, default=False)

class Vocabulary(Base):
    __tablename__ = "vocabulary"

    id = Column(Integer, primary_key=True, index=True)
    word = Column(String, nullable=False)
    tamil_meaning = Column(String, nullable=False)
    example = Column(String, nullable=False)
    day_number = Column(Integer, default=1)            # Day 1, Day 2...

# Database tables-ஐ create செய்ய
if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    print("Database schema successfully created in routine.db!")