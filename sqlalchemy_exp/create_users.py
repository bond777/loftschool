from sqlalchemy.orm import Session

from sqlalchemy_exp import models
from sqlalchemy_exp.engine import engine


session = Session(bind=engine)
session.add_all([
    models.User(name='Гарри Поттер', phone='79990000000'),
    models.User(name='Гермиона Грейнджер', phone='79990000001'),
    models.User(name='Волан-де-Морт', phone='79990000002'),
    models.User(name='Альбус Дамблдор', phone='79990000003'),
    models.User(name='Северус Снегг', phone='79990000004'),
    models.User(name='Драко Малфой', phone='79990000005'),
    models.User(name='Сириус Блэк', phone='79990000006'),
])
session.commit()
