from datetime import datetime

from sqlalchemy import Column, Integer, ForeignKey, Numeric, DateTime

from sqlalchemy_exp import models
from sqlalchemy_exp.models.base import Base


class Operation(Base):
    __tablename__ = 'operation'

    id = Column(Integer, primary_key=True, nullable=False)
    amount = Column(Numeric(10, 2), nullable=False)
    account_id = Column(Integer, ForeignKey(models.Account.id), nullable=False)
    created_at = Column(DateTime(), default=datetime.utcnow, nullable=False)
