from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase


# Создаём движок для подключения к базе данных
engine = create_engine("sqlite:///./shop.db", echo=True)

# Создаём фабрику сессий для работы с базой данных
SessionLocal = sessionmaker(bind=engine)

# Базовый класс для всех моделей SQLAlchemy
class Base(DeclarativeBase):
    pass

