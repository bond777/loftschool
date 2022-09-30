from sqlalchemy.orm import Session

from sqlalchemy_exp import models
from sqlalchemy_exp.engine import engine


session = Session(bind=engine)
session.add(
    models.User(name='Распус Люпин', phone='79990000000')
)
session.commit()
