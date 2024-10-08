import os

import pandas as pd
from tqdm import tqdm

from src.utils import read_csv
from src.extractor import Extractor


def main(csv_path, account_id):
    xlsx_path = csv_path.replace('csv', 'xlsx')
    assert not os.path.exists(xlsx_path), f"FileExistsError"

    columns = ['ProfileLink', 'FullName', 'Intro', 'Bio', 'Area', 'PhoneNumber']
    result = pd.DataFrame(columns=columns)

    extractor = Extractor(account_id)

    data = read_csv(csv_path)
    profiles = data[1:]

    for profile in tqdm(profiles[48:]):
        link = profile[2]
        bio, intro, area, phone_number = extractor.extract(link)
        
        if phone_number:
            fullname = profile[1]
            result = result._append({
                "ProfileLink": link,
                "FullName": fullname,
                "Intro": intro,
                "Bio": bio,
                "Area": area,
                "PhoneNumber": phone_number
                }, ignore_index=True)
            result.to_excel(xlsx_path, index=False)

    extractor.end()


if __name__ == '__main__':
    account_id = 1
    csv_path = 'data/sanads.vn.csv'
    main(csv_path, account_id)