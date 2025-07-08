import os
import datetime
from sqlalchemy import create_engine, Column, Integer, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

class Counter(Base):
    __tablename__ = 'counter'
    id = Column(Integer, primary_key=True)
    count = Column(Integer, default=0)
    created = Column(DateTime)

    def increment(self, session):
        self.count += 1
        session.commit()
        return self.count

    def decrement(self, session):
        self.count -= 1
        session.commit()
        return self.count

    def reset(self, session):
        self.count = 0
        session.commit()
        return self.count

def connect_to_db(db_path: str) -> sessionmaker:
    print('Подключение к БД')
    engine = create_engine(f'sqlite:///{db_path}')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session



def main():
    path_to_db = 'data.sqlite3'
    if os.path.exists(path_to_db):
        os.remove(path_to_db)
        print('Существующая БД удалена')
    Session = connect_to_db(path_to_db)
    session = Session()

    counter = Counter(count=1, created=datetime.datetime.now() + datetime.timedelta(hours=3))
    session.add(counter)
    session.commit()
    print(f"{counter.id} | {counter.count} | {counter.created}")

    input("Pause. Press Enter for continue ")

    session.query(Counter).filter(Counter.id == 1).update({Counter.count: 2})
    session.commit()
    print(f"{counter.id} | {counter.count} | {counter.created}")

    input("Pause. Press Enter for continue ")

    # Демонстрация работы методов increment/decrement с БД

    # Увеличиваем на 1
    counter.increment(session)
    print(f"{counter.id} | {counter.count} | {counter.created}")

    # Уменьшаем на 1
    counter.decrement(session)
    print(f"{counter.id} | {counter.count} | {counter.created}")

    # Сбрасываем в 0
    counter.reset(session)
    print(f"{counter.id} | {counter.count} | {counter.created}")

    # Увеличиваем на 2
    counter.increment(session)
    counter.increment(session)
    print(f"{counter.id} | {counter.count} | {counter.created}")

if __name__ == '__main__':
    main()