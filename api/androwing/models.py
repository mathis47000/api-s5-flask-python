from sqlalchemy import Column, DateTime, Integer, String, Enum, ForeignKey
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import relationship, backref
from androwing.database import Base
from datetime import datetime
import enum

class Feeling(enum.Enum):
    GOOD = 1
    NORMAL = 2
    BAD = 3

class Training(Base, SerializerMixin):
    __tablename__ = 'training'
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    distance = Column(Integer, nullable=False)
    duration = Column(Integer, nullable=False)
    date_training = Column(DateTime, nullable=False)
    feeling = Column(Enum(Feeling), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

    def __init__(self, title, distance,duration, feeling):
        self.title = title
        self.distance = distance
        self.duration = duration
        self.feeling = feeling
        self.date_training = datetime.now()
    def __repr__(self):
        return '<Training: {}>'.format(self.id)

class User(Base, SerializerMixin):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(200), unique=True, nullable=False)
    email = Column(String(200), unique=True, nullable=False)
    trainings = relationship('Training', cascade="all, delete-orphan", lazy = 'dynamic')
    

    def __init__(self, name, email):
        self.name = name
        self.email = email
    def __repr__(self):
        return '<User: {}>'.format(self.id)
