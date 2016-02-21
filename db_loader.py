
import os
from webscraper import scraper
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Athlete

DB_USERNAME = os.getenv('DB_USERNAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_URL = os.getenv('DB_URL')
DB_NAME = os.getenv('DB_NAME')

SQLALCHEMY_DATABASE_URI = "postgresql://%s:%s@%s/%s" % (DB_USERNAME, DB_PASSWORD, DB_URL, DB_NAME)


def load_data():
    engine = create_engine(SQLALCHEMY_DATABASE_URI)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    athletes_data = scraper()

    insertion_data = []
    for athlete, athlete_data  in athletes_data.iteritems():

        athlete = Athlete(
            name=             athlete,
            age=              clean_string(athlete_data['age']),
            hieght=           clean_string(athlete_data['hieght']),
            wieght=           clean_string(athlete_data['wieght']),

            run_5k=           athlete_data['Run 5k'],
            back_squat=       clean_string(athlete_data['Back Squat']),
            clean_and_jerk=   clean_string(athlete_data['Clean & Jerk']),
            snatch=           clean_string(athlete_data['Snatch']),
            deadlift=         clean_string(athlete_data['Deadlift']),
            max_pullups=      athlete_data['Max Pull-ups'],
        )
        insertion_data.append(athlete)

    session.add_all(insertion_data)
    session.commit()

def clean_string(s):
    if s is None:
        return s

    if s == '--':
        return None

    if 'lb' in s:
        s = s.replace('lb', '')

    return s.strip()

if __name__ == '__main__':
    load_data()