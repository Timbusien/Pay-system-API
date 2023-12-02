from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean, Float
from sqlalchemy.orm import relationship
from database import Base


# Таблица для пользователей
class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    surname = Column(String)
    number = Column(String)
    email = Column(String, unique=True, nullable=False)
    city = Column(String)
    password = Column(String, nullable=False)
    reg_date = Column(DateTime)


# Таблица для крединтных карт
class UserCard(Base):
    __tablename__ = 'cards'
    card_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    card_number = Column(Integer, nullable=False, unique=True)
    balance = Column(Float, default=0)
    exp_date = Column(Integer, nullable=False)
    card_name = Column(String)
    user_fk = relationship(User, lazy='subquery')


# Таблица для перевода денег
class Transfer(Base):
    __tablename__ = 'transfers'
    transfer_id = Column(Integer, primary_key=True, autoincrement=True)
    card_from_id = Column(Integer, ForeignKey('cards.card_id'))
    card_to_id = Column(Integer, ForeignKey('cards.card_id'))
    amount = Column(Float)
    status = Column(Boolean, default=True)
    transaction_date = Column(DateTime)
    card_from_fk = relationship(UserCard, lazy='subquery')
    card_to_fk = relationship(UserCard, lazy='subquery')


