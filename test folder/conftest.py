import os
import sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

print("PROJECT ROOT:",project_root)
sys.path.insert(0,project_root)
