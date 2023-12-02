from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Ссылка на базу данных
SQALCHEMY_DATABASE_URI = 'sqlite:///pay.db'

# Подключаемся к базе данных
engine = create_engine(SQALCHEMY_DATABASE_URI)

# Генерация сессий
SessionLocal = sessionmaker(bind=engine)

# Общий класс для моделей
Base = declarative_base()

from database import models


# Функция для генерации связи для базы данных
def get_database():
    my_db = SessionLocal()
    try:
        yield my_db

    except Exception:
        my_db.rollback()
        raise
    finally:
        my_db.close()


