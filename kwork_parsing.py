import openpyxl
from openpyxl.worksheet import worksheet

link = 'https://kwork.ru/projects'
OUT_XLSX_FILENAME = 'kwork_parsing.xlsx'


def general_parsing(soup, num):
    book = openpyxl.load_workbook(filename=OUT_XLSX_FILENAME)
    sheet: worksheet = book.worksheets[0]
    for general_element in soup.find_all('div', class_='card__content pb5'):
        for name_code in general_element.find_all('div', class_='wants-card__header-title first-letter breakwords pr250'):
            name = name_code.find('a')
            sheet.cell(row=num, column=1, value=name.text)
        for fprice_code in general_element.find_all('div', class_='wants-card__header-price wants-card__price m-hidden'):
            sheet.cell(row=num, column=2, value=fprice_code.text)
        for sprice_code in general_element.find_all('div', class_='wants-card__description-higher-price'):
            sheet.cell(row=num, column=3, value=sprice_code.text)
        for time_sugges_code in general_element.find_all('div', class_='force-font force-font--s12'):
            times = []
            for time_code in time_sugges_code.find('span'):
                times.append(time_code.text)
            sheet.cell(row=num, column=4, value=times[0])
        for time_sugges_code in general_element.find_all('div', class_='force-font force-font--s12'):
            sugges = []
            for sugges_code in time_sugges_code.find_all('span'):
                sugges.append(sugges_code.text)
            sheet.cell(row=num, column=5, value=sugges[1])
        for details_code in general_element.find_all('div', class_='breakwords first-letter js-want-block-toggle js-want-block-toggle-full hidden'):
            sheet.cell(row=num, column=6, value=details_code.text)
        num += 1
    book.save(OUT_XLSX_FILENAME)
    return num

