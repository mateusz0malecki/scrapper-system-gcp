from bs4 import BeautifulSoup
from requests import get


def get_links_to_offers_praca():
    links = []
    cities = {
        # 'Gdańsk': 'gdansk',
        # 'Szczecin': 'szczecin',
        # 'Białystok': 'bialystok',
        # 'Toruń': 'torun',
        # 'Bydgoszcz': 'bydgoszcz',
        # 'Olsztyn': 'olsztyn',
        # 'Warszawa': 'warszawa',
        # 'Lublin': 'lublin',
        # 'Rzeszow': 'rzeszow',
        # 'Kraków': 'krakow',
        # 'Katowice': 'katowice',
        # 'Opole': 'opole',
        # 'Wrocław': 'wroclaw',
        # 'Łódź': 'lodz',
        # 'Poznań': 'poznan',
        # 'Zielona Góra': 'zielona-gora',
        # 'Gorzów Wielkopolski': 'gorzow-wielkopolski',
        'Kielce': 'kielce'
    }
    categories = {
        'Administracja biurowa': 'administracja-biurowa',
        # 'Administracja publiczna / Służba publiczna': 'administracja-publiczna-sluzba-cywilna',
        # 'Architektura': 'architektura',
        # 'Badania i rozwój': 'badania-i-rozwój',
        # 'BHP / Ochrona środowiska': 'rolnictwo-ochrona-srodowiska',
        # 'Budownictwo': 'budownictwo-geodezja',
        # 'Doradztwo / Konsulting': 'doradztwo-konsulting',
        # 'Energetyka': 'energetyka-elektronika',
        # 'Edukacja / Szkolenia': 'edukacja-nauka-szkolenia',
        # 'Farmaceutyka / Biotechnologia': 'farmaceutyka-biotechnologia',
        # 'Finanse / Ekonomia': 'finanse-bankowosc',
        # 'Franczyza / Własny biznes': 'franczyza',
        # 'Gastronomia / Catering': 'gastronomia-catering',
        # 'Hotelarstwo / Gastronomia / Turystyka': 'turystyka-hotelarstwo',
        # 'Human Resources / Zasoby ludzkie': 'human-resources-kadry',
        # 'Internet / e-Commerce / Nowe media': 'internet-e-commerce',
        # 'Inżynieria': 'inzynieria-projektowanie',
        # 'IT - Administracja': 'informatyka-administracja',
        # 'IT - Rozwój oprogramowania': 'informatyka-programowanie',
        # 'Kadra zarządzająca': 'kadra-zarzadzajaca',
        # 'Kontrola jakości': 'kontrola-jakosci',
        # 'Księgowość': 'ksiegowosc-audyt-podatki',
        # 'Łańcuch dostaw': 'logistyka-dystrybucja',
        # 'Marketing': 'marketing-reklama',
        # 'Montaż / Serwis / Technika': 'serwis-technika-montaz',
        # 'Motoryzacja': 'motoryzacja',
        # 'Nieruchomości': 'nieruchomosci',
        # 'Ochrona osób i mienia': 'ochrona-osob-i-mienia',
        # 'Opieka zdrowotna': 'medycyna-opieka-zdrowotna',
        # 'Praca fizyczna': 'praca-fizyczna',
        # 'Prawo': 'prawo',
        # 'Produkcja': 'przemysl-produkcja',
        # 'Reklama / Grafika / Kreacja / Fotografia': 'grafika-fotografia-kreacja',
        # 'Sport': 'sport-rekreacja',
        # 'Sprzedaż': 'sprzedaz-obsluga-klienta',
        # 'Telekomunikacja': 'telekomunikacja',
        # 'Tłumaczenia': 'tlumaczenia',
        # 'Transport / Spedycja / Logistyka': 'transport-spedycja',
        # 'Ubezpieczenia': 'ubezpieczenia',
        # 'Zakupy': 'zakupy',
        # 'Zdrowie / Uroda / Rekreacja': 'kosmetyka-pielegnacja'
    }

    for city_name, city in cities.items():
        for category_name, category in categories.items():
            page_number = 1
            while True:
                try:
                    page = get(
                        f"https://www.praca.pl/{category}_m-{city}_{page_number}",
                        allow_redirects=False
                    ).content
                    bs = BeautifulSoup(page, 'html.parser')

                    section = bs.find('section', class_="app-content__main-content")

                    if not section:
                        break

                    offers_list = section.find_all('li', class_="listing__item")

                    for item in offers_list:
                        offer_link = item.find('a', class_="listing__observe gtm-action-star")
                        links.append((f"{offer_link['href']}", city_name, category_name))
                    page_number += 1

                except Exception as e:
                    print(f'get_links_to_offers_praca: {e}')

    links = list(set(links))
    return links
