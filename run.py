from src.utils import *
from main import main

if __name__ == '__main__':
    config = load_config('config/extract_config.yaml')
    csv_path = 'data/' + config['csv_path']
    account_id = config['account_id']
    main(csv_path, account_id)