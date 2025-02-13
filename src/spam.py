import os
os.environ['TF_TFLITE_DISABLE_XNNPACK'] = '1'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from src.utils import *


class Spam():
    def __init__(self, account_id):
        account_config = load_config('config/account_config.yaml')
        account_info = account_config[account_id]
        self.browser = self.login_facebook(account_info)
        
        self.cmt_content = open("config/cmt_content.txt", "r").read()

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

    def spam(self, profile_link):
        self.browser.get(profile_link)
        sleeping()
        
        try:
            # cmt_btn = self.browser.find_element_by_css_selector('[role="comment_button"]')
            # cmt_btn.click()
            # sleeping()

            cmt_textbox = self.browser.find_element_by_css_selector('role="textbox"')
            cmt_textbox.send_keys(self.cmt_content)
            sleeping()

            cmt_textbox.send_keys(Keys.ENTER)
            sleeping()
        except:
            pass
        
    def end(self):
        self.browser.close()