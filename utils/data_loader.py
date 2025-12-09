import json
import csv

def load_json(path):
    with open(path, "r") as f:
        return json.load(f)

def load_csv(path):
    with open(path, "r") as f:
        reader = csv.DictReader(f)
        return list(reader)
