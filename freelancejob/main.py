import requests
from bs4 import BeautifulSoup as BS
from GF.freelancejob import excel_writing

if __name__ == '__main__':
    # excel_writing.urls_to_xlsx()
    urls = excel_writing.get_urls()
    excel_writing.fill_title()
    excel_writing.dump_to_xlsx(urls)

