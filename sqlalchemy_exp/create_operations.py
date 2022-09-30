from sqlalchemy import select
from sqlalchemy.orm import Session

from sqlalchemy_exp import models
from sqlalchemy_exp.engine import engine

session = Session(bind=engine)

stm = select(models.User).where(models.User.name == 'Гарри Поттер')
result = session.execute(stm)
user = result.fetchone()[0]

stm = select(models.Account).where(
    (models.User.id == user.id) &
    (models.Account.name == 'Пластиковая карта')
)
result = session.execute(stm)
account = result.fetchone()[0]

amount = 100000
session.add(
    models.Operation(account_id=account.id, amount=amount),
)

account.balance += amount

session.commit()
