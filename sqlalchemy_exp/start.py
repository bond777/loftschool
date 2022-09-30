import os.path
import sys
from os.path import dirname

print()
# sys.path.insert(1, dirname(dirname(os.path.abspath(__file__))))

print(sys.path)

from sqlalchemy_exp import connection


print(connection.engine)
