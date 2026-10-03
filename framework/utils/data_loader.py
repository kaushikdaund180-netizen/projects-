import json
import os

# tests/data folder
DATA_FOLDER = os.path.join(os.path.dirname(__file__), "..", "..", "tests", "data")


def load_json(filename):
    # reads a json file from tests/data
    with open(os.path.join(DATA_FOLDER, filename), encoding="utf-8") as f:
        return json.load(f)
