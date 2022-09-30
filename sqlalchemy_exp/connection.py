from sqlalchemy import create_engine

#sqlite
# engine = create_engine('sqlite:///sqlalchemy_exp/loft_school_bank.db', echo=True)

#postgresql
engine = create_engine(
    'postgresql://admin:!AS6DF:LD3LKJdsfh@localhost/loft_school_bank_sqlalchemy', echo=True
)
