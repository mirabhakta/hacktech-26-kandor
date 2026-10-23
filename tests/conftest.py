import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(ROOT, "Backend"))
sys.path.insert(0, ROOT)

os.environ.setdefault("KANDOR_PROVIDER", "rules")