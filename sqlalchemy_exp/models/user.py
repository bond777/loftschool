from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy_exp.models.base import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(64), nullable=False)
    phone = Column(String(11), nullable=False, unique=True)
    created_at = Column(DateTime(), nullable=False, default=datetime.utcnow)

    def get_cardholder_name(self):
        return self.name.upper()
