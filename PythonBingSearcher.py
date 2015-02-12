from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time


for line in open('Words\words.txt'):
    word = line.strip()
    browser = webdriver.Firefox()
    browser.get('https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=12&ct=1423691523&rver=6.0.5286.0&wp=MBI&wreply=https:%2F%2Fwww.bing.com%2Fsecure%2FPassport.aspx%3Frequrl%3Dhttp%253a%252f%252fwww.bing.com%252f&lc=1033&id=264960')  

    email = browser.find_element_by_id('i0116')
    password = browser.find_element_by_id('i0118')
    submit = browser.find_element_by_id('idSIButton9')

    email.send_keys('email')
    password.send_keys('pass')
    submit.click()

    time.sleep(5)

    url = 'http://bing.com/search/?q=' + word
    browser.get(url)
    time.sleep(1)
    browser.close()


