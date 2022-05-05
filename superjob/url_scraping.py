from bs4 import BeautifulSoup as BS
import requests


def scrap_urls():
    urls = ['https://www.superjob.ru/resume/pomoschnik-lichnyj.html?t[0]=4&order_by[datepub]=desc?page=1', 'https://www.superjob.ru/resume/biznes-assistent.html?t[0]=4&order_by[datepub]=desc&page=1', 'https://www.superjob.ru/resume/pomoschnik-rukovoditelya.html?t[0]=4&order_by[datepub]=desc&page=1']
    resume_urls = []
    for i in range(1, 21):
        html = requests.get(f'https://www.superjob.ru/resume/pomoschnik-rukovoditelya.html?t[0]=4&order_by[datepub]=desc&page={i}', headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'})
        soup = BS(html.text, "html.parser")
        for link_code in soup.find_all('div', class_='_3igJl _3lK_W ljjt-'):
            link = link_code.find('a')
            resume_urls.append(link['href'])
    return resume_urls