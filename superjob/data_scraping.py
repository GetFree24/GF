import re
from lxml import etree
from bs4 import BeautifulSoup as BS
import requests

own_data = ''

def scrap_id(soup):
    id_code = soup.find('span', class_='_4uUzb _1TcZY mO3i1 dAWx1')
    id = re.search('\d+', id_code.text)
    return id.group(0)

def scrap_updated(soup):
    updated_code = soup.find('span', class_='_3S_8X _4uUzb _1TcZY mO3i1 dAWx1')
    return updated_code.text

def scrap_online(soup):
    onl = []
    for online_code in soup.find_all('div', class_='_1gHjC'):
        for last_online in online_code.find_all('span', class_='_4uUzb _1TcZY mO3i1 dAWx1'):
           onl.append(last_online.text)
    return onl[1]

def scrap_category(soup):
    category1 = soup.find('span', class_='_37aap _1TcZY mO3i1 dAWx1')
    return category1.text

def scrap_own_data(soup):
    tree = etree.HTML(str(soup))
    own_data = tree.xpath('//*[@id="app"]/div/div[1]/div[4]/div/div/div[1]/div/div[3]/div/div/div[1]/div/div/div[1]/div[1]/div/div/div/div/span/span/span/div/div[1]/span')[0].text
    return own_data
# /html/body/div[3]/div/div[1]/div[4]/div/div/div[1]/div/div[3]/div/div/div[1]/div/div/div[1]/div[1]/div/div/div/div/span/span/span/div/div[1]/span
# /html/body/div[3]/div/div[1]/div[4]/div/div/div[1]/div/div[3]/div/div/div[1]/div/div/div[1]/div[1]/div/div/div/div/span/span/span/div/div[1]/span
# /html/body/div[3]/div/div[1]/div[4]/div/div/div[1]/div/div[3]/div/div/div[1]/div/div/div[1]/div[1]/div/div/div/div/span/span/span/div/div[1]/span
def scrap_merried(soup):
    own_data = scrap_own_data(soup)
    merried = re.split('[,]\s+', own_data)
    try:
        return merried[2]
    except Exception:
        return ' '

def scrap_child(soup):
    own_data = scrap_own_data(soup)
    child = re.split('[,]\s+', own_data)
    try:
        return child[3]
    except Exception:
        return ' '

def scrap_sex(soup):
    own_data = scrap_own_data(soup)
    sex = re.split('[,]\s+', own_data)
    try:
        if sex[0].find('родилась') != -1:
            return 'Женщина'
        else:
            return 'Мужчина'
    except Exception:
        return ' '

def scrap_position(soup):
    position = soup.find('h1', class_='_2L5ou _1TcZY mO3i1 dAWx1 Zruy6')
    return position.text

def scrap_employment(soup):
    employments = []
    for employment_code in soup.find_all('span', '_37aap _1TcZY mO3i1 dAWx1'):
        employments.append(employment_code.text)
    employment = re.split('[,]\s+', employments[1])
    return employment[0]

def scrap_birth(soup):
    own_data = scrap_own_data(soup)
    birth = re.split('[,]\s+', own_data)
    birth = re.split("\s[(]", birth[0])
    if birth[1]:
        birth = birth[1]
        return birth[:len(birth) - 1]
    else:
        return ' '

def scrap_age(soup):
    own_data = scrap_own_data(soup)
    birth = re.split('[,]\s+', own_data)
    birth = re.split("\s[(]", birth[0])
    if birth[0]:
        birth = birth[0]
        return birth
    else:
        return ' '

def scrap_trip(soup):
    trips = []
    for trip_code in soup.find_all('span', '_37aap _1TcZY mO3i1 dAWx1'):
        trips.append(trip_code.text)
    trip = re.split('[,]\s+', trips[1])
    return trip[1]

def scrap_live(soup):
    dom = etree.HTML(str(soup))
    try:
        live = dom.xpath('//*[@id="app"]/div/div[1]/div[4]/div/div/div[1]/div/div[3]/div/div/div[1]/div/div/div[1]/div[1]/div/div/div/div/span/span/span/div/div[2]')[0].text
        # //*[@id="app"]/div/div[1]/div[4]/div/div/div[1]/div/div[3]/div/div/div[1]/div/div/div[1]/div[1]/div/div/div/div/span/span/span/div/div[2]
        # //*[@id="app"]/div/div[1]/div[4]/div/div/div[1]/div/div[3]/div/div/div[1]/div/div/div[1]/div[1]/div/div/div/div/span/span/span/div/div[2]/text()[1]
        return live
    except Exception:
        pass

def scrap_vaccine(soup):
    dom = etree.HTML(str(soup))
    vaccine = dom.xpath('//*[@id="app"]/div/div[1]/div[4]/div/div/div[1]/div/div[4]/div/div/div[1]/div[1]/div/div/div/div/div/div[3]/span')[0].text
    if vaccine:
        return vaccine
    else:
        return ' '

def scrap_salary(soup):
    dom = etree.HTML(str(soup))
    salary = dom.xpath('//*[@id="app"]/div/div[1]/div[4]/div/div/div[1]/div/div[4]/div/div/div[1]/div[1]/div/div/div/div/div/div[3]/span')
    if salary:
        salary = salary[0].text
    else:
        salary = dom.xpath('//*[@id="app"]/div/div[1]/div[4]/div/div/div[1]/div/div[4]/div/div/div[1]/div[1]/div/div/div/div/div/div[4]/span')[0].text
    # //*[@id="app"]/div/div[1]/div[4]/div/div/div[1]/div/div[4]/div/div/div[1]/div[1]/div/div/div/div/div/div[3]/span
    # //*[@id="app"]/div/div[1]/div[4]/div/div/div[1]/div/div[4]/div/div/div[1]/div[1]/div/div/div/div/div/div[4]/span
    salary = salary.replace('&nbsp;', ' ')
    salary = re.search('\d+\s\d+',  salary)
    return salary.group(0)

def scrap_curr(soup):
    dom = etree.HTML(str(soup))
    currency = dom.xpath('//*[@id="app"]/div/div[1]/div[4]/div/div/div[1]/div/div[4]/div/div/div[1]/div[1]/div/div/div/div/div/div[3]/span')[0].text
    currency = currency.replace('&nbsp;', ' ')
    currency = re.split('\s', currency)
    return currency[2]

def scrap_citiz(soup):
    dom = etree.HTML(str(soup))
    citizen = dom.xpath('//*[@id="app"]/div/div[1]/div[4]/div/div/div[1]/div/div[3]/div/div/div[1]/div/div/div[1]/div[1]/div/div/div/div/span/span/span/div/div[3]')[0].text
    citizen = re.split('\s', citizen)
    return citizen[1]

def scrap_exp(soup):
    exp = soup.find('span', class_='_4uUzb _1TcZY dAWx1')
    return exp.text

def scrap_wempl(soup):
    wempl = soup.find('h3', class_='_1CLYJ _1TcZY mO3i1 Bbtm8 Zruy6')
    return wempl.text

def scrap_org(soup):
    organizations = ''
    for org_code in soup.find_all('span', '_35ziJ _1TcZY mO3i1 Bbtm8 Zruy6'):
        organizations += org_code.text + '\n'
    return organizations

def scrap_sitec(soup):
    sitecs = ''
    for sitec_code in soup.find_all('span', '_4uUzb _1TcZY _1ppMM Bbtm8 Zruy6'):
        sitecs += sitec_code.text + '\n'
    return sitecs

def scrap_startw(soup):
    dom = etree.HTML(str(soup))
    startw = dom.xpath('//*[@id="app"]/div/div[1]/div[4]/div/div/div[1]/div/div[4]/div/div/div[1]/div[2]/div[1]/div/div/div[2]/div/div/ul/li[2]/div/ul/li[1]/span/span')[0].text
    startw = startw.replace('&nbsp;', ' ')
    startw = re.split('–', startw)
    return startw[0]

def scrap_endw(soup):
    dom = etree.HTML(str(soup))
    endw = dom.xpath('//*[@id="app"]/div/div[1]/div[4]/div/div/div[1]/div/div[4]/div/div/div[1]/div[2]/div[1]/div/div/div[2]/div/div/ul/li[1]/div/ul/li[1]/span/span')[0].text
    endw = endw.replace('&nbsp;', ' ')
    endw = re.split('–', endw)
    return endw[1]

def scrap_long(soup):
    long1, long2, long3, long4, long5, long6, long7, long8, long9, long10 = ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '
    try:
        dom = etree.HTML(str(soup))
        long1 = dom.xpath('//*[@id="app"]/div/div[1]/div[4]/div/div/div[1]/div/div[4]/div/div/div[1]/div[2]/div[1]/div/div/div[2]/div/div/ul/li[1]/div/ul/li[2]/span/span')[0].text
        long2 = dom.xpath('//*[@id="app"]/div/div[1]/div[4]/div/div/div[1]/div/div[4]/div/div/div[1]/div[2]/div[1]/div/div/div[2]/div/div/ul/li[2]/div/ul/li[2]/span/span')[0].text
        long3 = dom.xpath('//*[@id="app"]/div/div[1]/div[4]/div/div/div[1]/div/div[4]/div/div/div[1]/div[2]/div[1]/div/div/div[2]/div/div/ul/li[3]/div/ul/li[2]/span/span')[0].text
        long4 = dom.xpath('//*[@id="app"]/div/div[1]/div[4]/div/div/div[1]/div/div[4]/div/div/div[1]/div[2]/div[1]/div/div/div[2]/div/div/ul/li[4]/div/ul/li[2]/span/span')[0].text
        long5 = dom.xpath('//*[@id="app"]/div/div[1]/div[4]/div/div/div[1]/div/div[4]/div/div/div[1]/div[2]/div[1]/div/div/div[2]/div/div/ul/li[5]/div/ul/li[2]/span/span')[0].text
        long6 = dom.xpath('//*[@id="app"]/div/div[1]/div[4]/div/div/div[1]/div/div[4]/div/div/div[1]/div[2]/div[1]/div/div/div[2]/div/div/ul/li[6]/div/ul/li[2]/span/span')[0].text
        long7 = dom.xpath('//*[@id="app"]/div/div[1]/div[4]/div/div/div[1]/div/div[4]/div/div/div[1]/div[2]/div[1]/div/div/div[2]/div/div/ul/li[7]/div/ul/li[2]/span/span')[0].text
        long8 = dom.xpath('//*[@id="app"]/div/div[1]/div[4]/div/div/div[1]/div/div[4]/div/div/div[1]/div[2]/div[1]/div/div/div[2]/div/div/ul/li[8]/div/ul/li[2]/span/span')[0].text
        long9 = dom.xpath('//*[@id="app"]/div/div[1]/div[4]/div/div/div[1]/div/div[4]/div/div/div[1]/div[2]/div[1]/div/div/div[2]/div/div/ul/li[9]/div/ul/li[2]/span/span')[0].text
        long10 = dom.xpath('//*[@id="app"]/div/div[1]/div[4]/div/div/div[1]/div/div[4]/div/div/div[1]/div[2]/div[1]/div/div/div[2]/div/div/ul/li[10]/div/ul/li[2]/span/span')[0].text

    except Exception:
        pass
    finally:
        long_full = long1 + '\n' + long2 + '\n' + long3 + '\n' + long4 + '\n' + long5 + '\n' + long6 + '\n' + long7 + '\n' + long8 + '\n' + long9 + '\n' + long10 + '\n'
        return long_full

def scrap_duties(soup):
    duties = soup.find('span', class_='_2BpzE _35ziJ _1TcZY mO3i1 Bbtm8 Zruy6')
    return duties.text

def scrap_lvl(soup):
    own_data = scrap_own_data(soup)
    birth = re.split('[,]\s+', own_data)
    try:
        return birth[1]
    except:
        return ' '

def scrap_form(soup):
    dom = etree.HTML(str(soup))
    try:
        form = dom.xpath('//*[@id="app"]/div/div[1]/div[4]/div/div/div[1]/div/div[4]/div/div/div[1]/div[2]/div[2]/div/div/div[2]/div/div/ul/li/div/ul/li[2]/span/span')[0].text
        return form
    except Exception:
        pass

def scrap_year(soup):
    dom = etree.HTML(str(soup))
    try:
        year = dom.xpath('//*[@id="app"]/div/div[1]/div[4]/div/div/div[1]/div/div[4]/div/div/div[1]/div[2]/div[2]/div/div/div[2]/div/div/ul/li/div/ul/li[3]/span/span')[0].text
        return year
    except Exception:
        pass

def scrap_name(soup):
    dom = etree.HTML(str(soup))
    try:
        name = dom.xpath('//*[@id="app"]/div/div[1]/div[4]/div/div/div[1]/div/div[4]/div/div/div[1]/div[2]/div[2]/div/div/div[2]/div/div/ul/li/div/div/div[1]/div/div/div[1]/div/div/h3')[0].text
        return name
    except Exception:
        pass

def scrap_fac(soup):
    dom = etree.HTML(str(soup))
    try:
        fac = dom.xpath('//*[@id="app"]/div/div[1]/div[4]/div/div/div[1]/div/div[4]/div/div/div[1]/div[2]/div[2]/div/div/div[2]/div/div/ul/li/div/div/div[1]/div/div/div[2]/div[1]/span')[0].text
        fac = re.split('[:]\s', fac)
        return fac[1]
    except Exception:
        pass

def scrap_spec(soup):
    dom = etree.HTML(str(soup))
    try:
        spec = dom.xpath('//*[@id="app"]/div/div[1]/div[4]/div/div/div[1]/div/div[4]/div/div/div[1]/div[2]/div[2]/div/div/div[2]/div/div/ul/li/div/div/div[1]/div/div/div[2]/div[2]/span')[0].text
        spec = re.split('[:]\s', spec)
        return spec[1]
    except Exception:
        pass

def scrap_prof(soup):
    dom = etree.HTML(str(soup))
    prof = dom.xpath('//*[@id="app"]/div/div[1]/div[4]/div/div/div[1]/div/div[4]/div/div/div[1]/div[2]/div[3]/div/div/div[2]/div/div/div/div/div/div/div/div/div[1]/div/div[2]/span')[0].text
    return prof

def scrap_add(soup):
    dom = etree.HTML(str(soup))
    add = dom.xpath('//*[@id="app"]/div/div[1]/div[4]/div/div/div[1]/div/div[4]/div/div/div[1]/div[2]/div[3]/div/div/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div[2]/span')[0].text
    return add

def scrap_lan(soup):
    lan_code = soup.find('ul', class_='_3wx9- _3ZTO6 _179AW')
    if lan_code:
        lan = re.split('\s[—]\s', lan_code.text)
        return lan[0]
    else:
        return ' '

def scrap_lvlknw(soup):
    lan_code = soup.find('ul', class_='_3wx9- _3ZTO6 _179AW')
    if lan_code:
        lan = re.split('\s[—]\s', lan_code.text)
        return lan[1]
    else:
        return ' '

def scrap_drive(soup):
    dom = etree.HTML(str(soup))
    try:
        drive = dom.xpath('//*[@id="app"]/div/div[1]/div[4]/div/div/div[1]/div/div[4]/div/div/div[1]/div[2]/div[5]/div/div/div[2]/div/div/ul/li/span')[0].text
    except Exception:
        pass

