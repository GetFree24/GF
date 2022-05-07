from bs4 import BeautifulSoup as BS
import requests

from GF.habr_freelance import excel_writing

# if __name__ == '__main__':
#     urls = ['https://freelance.habr.com/tasks?categories=development_all_inclusive,development_backend,development_frontend,development_prototyping,development_ios,development_android,development_desktop,development_bots,development_games,development_1c_dev,development_scripts,development_voice_interfaces,development_other',
#             'https://freelance.habr.com/tasks?categories=testing_sites,testing_mobile,testing_software',
#             'https://freelance.habr.com/tasks?categories=admin_servers,admin_network,admin_databases,admin_security,admin_other',
#             'https://freelance.habr.com/tasks?categories=design_sites,design_landings,design_logos,design_illustrations,design_mobile,design_icons,design_polygraphy,design_banners,design_graphics,design_corporate_identity,design_presentations,design_modeling,design_animation,design_photo,design_other',
#             'https://freelance.habr.com/tasks?categories=content_copywriting,content_rewriting,content_audio,content_article,content_scenarios,content_naming,content_correction,content_translations,content_coursework,content_specification,content_management,content_other',
#             'https://freelance.habr.com/tasks?categories=marketing_smm,marketing_seo,marketing_context,marketing_email,marketing_research,marketing_sales,marketing_pr,marketing_other',
#             'https://freelance.habr.com/tasks?categories=other_audit_analytics,other_consulting,other_jurisprudence,other_accounting,other_audio,other_video,other_engineering,other_other']
#     page_links = []
#     for url in urls:
#         # page_links[0] = url
#         res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'})
#         soup = BS(res.content, 'html.parser')
#         max_page = habr_scraper.scrap_pages(soup)
#         for x in range(1, max_page + 1):
#             page_links.append(url + f'&page={x}')
#         excel_writing.urls_to_xlsx(page_links)

if __name__ == '__main__':
    urls = excel_writing.add_url()
    excel_writing.dump_to_xlsx()
    num = 2
    for url in urls:
        try:
            res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'})
            soup = BS(res.text, 'html.parser')
            # print(url)
            excel_writing.data_to_xlsx(soup, num)
            num += 1
        except Exception:
            pass
        # links.extend(habr_scraper.scrap_urls(soup))
