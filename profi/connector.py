import requests
import undetected_chromedriver
import time
from bs4 import BeautifulSoup


#Connect to our site by using url with libraries requests and bs4
def soup_connection(link):
    proxies = {'http': 'socks5://user:pass@host:port',
               'https': 'socks5://user:pass@host:port'}
    res = requests.get(link, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}, proxies=proxies)
    html = BeautifulSoup(res.text, 'html.parser')
    return html

def driver_connection(link):
    try:
        driver = undetected_chromedriver.Chrome()
        driver.get(link)
        print(type(driver.get(link)))
        time.sleep(15)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

