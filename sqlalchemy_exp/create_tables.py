from sqlalchemy_exp import models
from sqlalchemy_exp.engine import engine

models.Base.metadata.create_all(engine)
