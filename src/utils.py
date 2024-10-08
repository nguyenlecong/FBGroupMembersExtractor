import csv
import yaml
import random
from time import sleep


def sleeping(min=2, max=3):
    sleep(random.randint(min, max))

def load_config(path):
    with open(path, 'r', encoding="utf8") as f:
        config = yaml.safe_load(f)
    return config

def read_csv(path):
    lines = []
    with open(path, mode ='r', encoding="utf8")as file:
        csv_file = csv.reader(file)
        for line in csv_file:
            lines.append(line)
    return lines