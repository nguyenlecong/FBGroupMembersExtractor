from src.utils import *
from main import main

if __name__ == '__main__':
    config = load_config('config/extract_config.yaml')
    csv_filename = config['csv_filename']
    account_id = config['account_id']
    continue_index = config['account_id']
    main(csv_filename, account_id, continue_index)