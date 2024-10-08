import os
os.environ['TF_TFLITE_DISABLE_XNNPACK'] = '1'

import re

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from src.utils import *


class Extractor():
    def __init__(self, account_id):
        account_config = load_config('config/account_config.yaml')
        account_info = account_config[account_id]
        self.browser = self.login_facebook(account_info)

        self.phone_number_pattern = re.compile(r"(?:\+?84|0)(?:\d[\.\s]*){9,10}")
        self.intro_area_pattern = re.compile(r"(?:Đến từ|Sống tại)\s([^\n]+)")

    @staticmethod
    def login_facebook(facebook_account):
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        # chrome_options.add_argument('--headless')  # Run in background
        browser = webdriver.Chrome(
            executable_path='./asset/chromedriver.exe', chrome_options=chrome_options)

        browser.get('https://www.facebook.com/')
        sleeping()

        txtUser = browser.find_element_by_id('email')
        txtUser.send_keys(facebook_account['username'])
        sleeping()

        txtPwd = browser.find_element_by_id('pass')
        txtPwd.send_keys(facebook_account['password'])
        sleeping()

        txtPwd.send_keys(Keys.ENTER)
        sleeping(20,20)  # FB Authentication

        return browser

    def get_bio(self):
        try:
            bio = self.browser.find_element_by_css_selector('div.xieb3on > div:nth-child(1) > div > div')
            bio = bio.text
        except:
            bio = ''
        return bio

    def get_intro(self):
        try:
            intro = self.browser.find_element_by_css_selector('div.xieb3on > div > div > ul')
            intro = intro.text
        except:
            intro = ''
        return intro
    
    def extract(self, profile_link):
        self.browser.get(profile_link)
        sleeping()

        bio, intro, area, phone_number = '', '', '', ''

        bio = self.get_bio()
        if bio:
            phone_number = self.find_phone_number(bio)
            if phone_number:
                intro = self.get_intro()
                area = self.filter_area(intro)
        return bio, intro, area, phone_number

    def find_phone_number(self, text):
        phone_numbers = []
        matches = self.phone_number_pattern.findall(text)
        for match in matches:
            cleaned_number = re.sub(r'\D', '', match)
            if cleaned_number.startswith("84"):
                cleaned_number = "0" + cleaned_number[2:]
            phone_numbers.append(cleaned_number)
        return '\n'.join(phone_numbers)

    def filter_area(self, text):
        matches = self.intro_area_pattern.findall(text)
        return '\n'.join(matches)    

    def end(self):
        self.browser.close()