from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from pdf_downloader import download


BOOK_PAGE_URL = 'https://tula-online.org/items/show/'

# pass your login and password
TULA_LOGIN = 'andrii_matsiiebskyi'
TULA_PASSWORD = 'nMdNp7muFVp4P3h'


def run():
    browser = webdriver.Firefox()

    browser.get('https://tula-online.org/')

    browser.find_element_by_id('action-login').click()

    browser.find_element_by_id(
        'u-enter__email').send_keys(f'{TULA_LOGIN}')

    browser.find_element_by_id(
        'u-enter__psw').send_keys(f'{TULA_PASSWORD}')
    browser.find_element_by_id('u-enter__smb').click()

    session_cookie = browser.get_cookies()[-1]

    cookies = {}

    cookies[session_cookie.get('name')] = session_cookie.get('value')
    browser.quit()

    with open('book_links.txt') as file:
        for line in file:
            print(line.rstrip())
            download(line.rstrip(), cookies)


run()
