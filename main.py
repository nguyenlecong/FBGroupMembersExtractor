from tqdm import tqdm

from src.spam import Spam
from src.utils import read_csv


def main(csv_filename, account_id, continue_index):
    spam = Spam(account_id)

    csv_path = 'data/' + str(csv_filename) + '.csv'
    data = read_csv(csv_path)
    users = data[continue_index+1:]  # Include header
    for user in tqdm(users):
        profile_link = user[2]
        spam.spam(profile_link)
    spam.end()
