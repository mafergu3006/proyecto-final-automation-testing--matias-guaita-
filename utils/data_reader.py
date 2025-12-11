import csv
import json

def read_csv(path):
    with open(path, encoding="utf-8") as f:
        return list(csv.DictReader(f))

def read_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)
