from sqlalchemy import select
from sqlalchemy.orm import Session

from sqlalchemy_exp import models
from sqlalchemy_exp.engine import engine


session = Session(bind=engine)

stm = select(models.User).where(models.User.name == 'Гарри Поттер')
result = session.execute(stm)
user = result.fetchone()[0]

session.add(
    models.Account(user_id=user.id, name="Пластиковая карта", balance=0),
)

session.commit()
