from sqlalchemy import select
from sqlalchemy.orm import Session

from sqlalchemy_exp import models
from sqlalchemy_exp.engine import engine


session = Session(bind=engine)
result = session.execute(select(models.User))
for user in result.scalars().all():
    print(tuple([user.id, user.name, user.phone, user.created_at]))
    # print(tuple([user.id, user.name, user.phone, user.created_at, user.get_cardholder_name()]))
