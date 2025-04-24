import sys
import os

sys.path.append("..")

import pycps
import json

os.chdir(os.path.dirname(__file__))

with open("sample.cps", "r") as f:
    b = json.loads(f.read())
    f.seek(0)
    c = pycps.loads(f.read())
    assert b == c.to_dict()