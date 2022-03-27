import connector
import excel_writing
import kwork_parsing
from bs4 import BeautifulSoup as BS

if __name__ == '__main__':
    excel_writing.dump_to_xlsx()
    num = 2
    for x in range(1, 82):
        html = connector.undetected_connection(f'https://kwork.ru/projects?page={x}&a=1')
        soup = BS(html, "html.parser")
        num = kwork_parsing.general_parsing(soup, num)