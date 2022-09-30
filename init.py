import site
import os
from os.path import dirname


paths = site.getsitepackages()
for path in paths:
    with open(os.path.join(path, 'loftschool_path.pth'), 'w') as f:
        f.write(dirname(os.path.abspath(__file__)))
