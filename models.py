
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class Athlete(Base):

    __tablename__ = 'athletes'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    age = Column(Integer)
    hieght = Column(String)
    wieght = Column(String)

    clean_and_jerk = Column(String)
    snatch = Column(String)
    deadlift = Column(String)
    back_squat = Column(String)
    max_pullups = Column(Integer)
    run_5k = Column(String)