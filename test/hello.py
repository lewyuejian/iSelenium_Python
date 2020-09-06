#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@file: hello.py
@time: 2020/9/6 0006 22:33
@desc:
'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('https://www.baidu.com')
driver.get_screenshot_as_file('a.png')
driver.quit()