import pandas as pd
from tqdm import tqdm

from src.extractor import Extractor
from src.utils import read_csv, create_valid_path


def main(csv_filename, account_id, continue_index):
    csv_path = 'data/csv/' + csv_filename + '.csv'
    xlsx_path = create_valid_path(csv_filename)

    columns = ['ProfileLink', 'FullName', 'Intro', 'Bio', 'Area', 'PhoneNumber']
    result = pd.DataFrame(columns=columns)

    extractor = Extractor(account_id)

    data = read_csv(csv_path)
    profiles = data[continue_index+1:]  # Include header

    for profile in tqdm(profiles):
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
            try:
                result.to_excel(xlsx_path, index=False)  # Handle iligal characters
            except:
                pass

    extractor.end()


if __name__ == '__main__':
    continue_index = 0
    account_id = 1
    csv_filename = 'sanads.vn'
    main(csv_filename, account_id, continue_index)