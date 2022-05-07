import openpyxl
from openpyxl.worksheet import worksheet

from GF.kwork import connector
from bs4 import BeautifulSoup as BS
import re

from excel_writing import OUT_XLSX_FILENAME


def scrap_categories(soup):
    categories = {}
    for categories_code in soup.find_all('select', 'js-category projects-filter__select-styled'):
        for category_code in categories_code.find_all('option', value=True):
            categories.update({category_code['value'] : category_code.text})
    return categories

def scrap_subcategories(soup):
    subcategories = {}
    for subcategories_code in soup.find_all('select', 'js-sub-category long-touch-js projects-filter__select-styled'):
        for subcategory_code in subcategories_code.find_all('option', value=True):
            subcategories.update({subcategory_code['value'] : subcategory_code.text})
    return subcategories

def scrap_thirdcategories(soup):
    thirdcategories = {}
    for thirdcategories_code in soup.find_all('select', 'js-third-category-select long-touch-js projects-filter__select-styled'):
        for thirdcategory_code in thirdcategories_code.find_all('option', value=True):
            thirdcategories.update({thirdcategory_code['value'] : thirdcategory_code.text})
    return thirdcategories


def scrap_page_count(soup):
    pages = 1
    for pages_code in soup.find_all('div', 'paging'):
        for page_code in pages_code.find_all('a'):
            page = page_code.text
            page = re.search('\d+', page)
            if page is None:
                continue
            page = int(page.group(0))
            if pages < page:
                pages = page
    return pages


def final_urls(soup, num):
    book = openpyxl.load_workbook(filename=OUT_XLSX_FILENAME)
    sheet: worksheet = book.worksheets[0]
    subcategories_value = scrap_subcategories(soup).keys()
    # subcategories = scrap_subcategories(soup).values()
    # thirdcategories_value = scrap_thirdcategories(soup).keys()
    # thirdcategories = scrap_thirdcategories(soup).values()
    # final_urls = []
    urls = []
    for subvalue in subcategories_value:
        html = connector.undetected_connection(f'https://kwork.ru/projects?c={subvalue}')
        soup = BS(html, "html.parser")
        thirdvalues = scrap_thirdcategories(soup).keys()
        for thirdvalue in thirdvalues:
            html = connector.undetected_connection(f'https://kwork.ru/projects?c={subvalue}&attr={thirdvalue}')
            soup = BS(html, "html.parser")
            pages = scrap_page_count(soup)
            for page in range(1, pages + 1):
                sheet.cell(row=num, column=11, value=f'https://kwork.ru/projects?c={subvalue}&attr={thirdvalue}&page={page}')
                # urls.append(f'https://kwork.ru/projects?c={subvalue}&attr={thirdvalue}&page={page}')
                num += 1
    book.save(OUT_XLSX_FILENAME)
    # return urls
