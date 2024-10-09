import os
import csv
import yaml
import random
from time import sleep


def sleeping(min=3, max=4):
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

def create_valid_path(filename):
    xlsx_path = 'data/xlsx/' + filename + '.xlsx'
    if not os.path.exists(xlsx_path):
        return xlsx_path
    
    counter = 1
    while True:
        new_filename = f"{filename}_{counter}"
        new_xlsx_path = 'data/xlsx/' + new_filename + '.xlsx'
        if not os.path.exists(new_xlsx_path):
            return new_xlsx_path
        counter += 1