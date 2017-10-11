import sys
from os import path
import os

sys.path.insert(0, path.abspath(path.join(path.dirname(__file__), '..')))

try:
    from async_actor import *
except Exception as e:
    print(e)
