from sqlalchemy import create_engine

engine = create_engine(
    'postgresql://admin:!AS6DF:LD3LKJdsfh@localhost/loft_school_bank_sqlalchemy', echo=True
)
