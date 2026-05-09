import os
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'game.sqllite')

#connect to database
engine = create_engine(f"sqlite:///{DB_PATH}", echo=False)

#standart class
Base = declarative_base

SessionLocal = sessionmaker(bind=engine)

class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    total_win = Column(Integer, default=0)
    total_lose = Column(Integer, default=0)
    class_role = Column(String, default="Учень")

    def init_db():
        Base.metadata.create_all(engine)

    def get_user(user_id: int):
        session = SessionLocal()
        user = session.query(User).get(user_id)
        session.close()
        return user
    
    def add_user(user_id: int, username: str):
        session = SessionLocal()
        new_user = User(user_id=user_id, username=username)
        session.add(new_user)
        session.commit()
        session.close()

