from sqlalchemy import Table, Column, Integer, MetaData, Numeric, DateTime, ForeignKey

from sqlalchemy_exp.tables import Account

Operation = Table('operation', MetaData(),
    Column('id', Integer, primary_key=True, nullable=False),
    Column('amount', Numeric(10, 2), nullable=False),
    Column('account_id', Integer, ForeignKey(Account.columns.id), nullable=False),
    Column('created_at', DateTime(), nullable=False),
)

