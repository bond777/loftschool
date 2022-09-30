from datetime import datetime

from sqlalchemy import Table, Column, Integer, String, MetaData, UniqueConstraint, \
    DateTime

User = Table('user', MetaData(),
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(64), nullable=False),
    Column('phone', String(11), nullable=False),
    Column('created_at', DateTime(), nullable=False, default=datetime.utcnow),
    UniqueConstraint('phone', name='unique_phone'),
)
