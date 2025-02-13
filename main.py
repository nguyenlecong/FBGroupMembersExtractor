import pandas as pd
from tqdm import tqdm

from src.spam import Spam
from src.utils import read_csv


def main(csv_filename, account_id, continue_index):
    spam = Spam(account_id)

    csv_path = 'data/csv/' + csv_filename + '.csv'
    data = read_csv(csv_path)
    profiles = data[continue_index+1:]  # Include header
    for profile in tqdm(profiles):
        link = profile[2]
        spam.spam(link)
    spam.end()
