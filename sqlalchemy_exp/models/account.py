from sqlalchemy import Column, Integer, String, ForeignKey, Numeric

from sqlalchemy_exp import models
from sqlalchemy_exp.models.base import Base


class Account(Base):
    __tablename__ = 'account'

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey(models.User.id), nullable=False)
    name = Column(String(32), nullable=False)
    balance = Column(Numeric(10, 2), nullable=False)
