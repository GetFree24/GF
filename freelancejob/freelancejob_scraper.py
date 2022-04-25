import re

from bs4 import BeautifulSoup as BS
import requests



def urls_scraping(soup):
    link = []
    for url in soup.find_all('a', class_='big'):
        link.append('https://www.freelancejob.ru' + url['href'])
    return link

def get_pages():
    res = requests.get('https://www.freelancejob.ru/projects/p1/', headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'})
    soup = BS(res.content, 'html.parser')
    pages = soup.find('ul', class_='pagination')
    for page_code in pages.find_all('a'):
        if page_code.text == '»»':
            page = re.search('\d+', page_code['href'])
            return page.group(0)


def scrap_title(soup):
    title = soup.find('h1')
    return title.text

def scrap_body(soup):
    body = soup.find('td')
    return body

def get_details(soup):
    body = scrap_body(soup)
    details_code = re.match('<td>[\s\n\d\w\W]+<div', str(body))
    details = details_code.group(0)
    try:
        details = re.sub('<noindex>[\s\n\d\w\W]+<\/noindex>', '', details)
    except Exception:
        pass
    details = details.replace('<td>', '')
    details = details.replace('<br>', '')
    details = details.replace('<br/>', '')
    details = details.replace('<div', '')
    return details

def get_price(soup):
    body = scrap_body(soup)
    price_code = re.search('Бюджет:<\/b> \d+', str(body))
    if price_code:
        price = re.search('\d+', price_code.group(0))
        return price

def get_currency(soup):
    body = scrap_body(soup)
    currency_code = re.search('Бюджет:<\/b> \d+', str(body))
    if currency_code:
        currency = re.split('\d+\s', currency_code.group(0))
        return currency[1]

def get_town(soup):
    body = scrap_body(soup)
    town_code = re.search('Город:<\/b> [а-яёА-ЯЁ-]+', str(body))
    if town_code:
        town = re.split('>\s', town_code.group(0))
        return town[1]

def get_offer(soup):
    body = scrap_body(soup)
    offer_code = re.search('Вид предложения:<\/b> [а-яёА-ЯЁ()\s-]+', str(body))
    if offer_code:
        offer = re.split('>\s', offer_code.group(0))
        return offer[1]

def get_category(soup):
    body = scrap_body(soup)
    category_code = re.search('[а-яёА-ЯЁ-]+<\/a', str(body))
    if category_code:
        category = category_code.group(0).replace('</a', '')
        return category