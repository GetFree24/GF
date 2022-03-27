import undetected_chromedriver as uc
import time


def undetected_connection(link):
    driver = uc.Chrome()
    driver.get(link)
    time.sleep(10)
    html = driver.page_source
    driver.quit()
    return html