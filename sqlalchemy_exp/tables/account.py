from sqlalchemy import Table, Column, Integer, String, MetaData, Numeric, ForeignKey
from sqlalchemy_exp.tables import User

Account = Table('account', MetaData(),
    Column('id', Integer, primary_key=True, nullable=False),
    Column('user_id', Integer, ForeignKey(User.columns.id), nullable=False),
    Column('name', String(32), nullable=False),
    Column('balance', Numeric(10, 2), nullable=False),
)
