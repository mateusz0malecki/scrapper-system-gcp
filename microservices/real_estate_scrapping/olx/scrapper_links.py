from bs4 import BeautifulSoup
from requests import get


def olx_get_links_to_offers():
    cities = {
        'gdansk': "Gdańsk",
        # 'szczecin': "Szczecin",
        # 'bialystok': "Białystok",
        # 'torun': "Toruń",
        # 'bydgoszcz': "Bydgoszcz",
        # 'olsztyn': "Olsztyn",
        # 'warszawa': "Warszawa",
        # 'lublin': "Lublin",
        # 'rzeszow': "Rzeszów",
        # 'krakow': "Kraków",
        # 'katowice': "Katowice",
        # 'opole': "Opole",
        # 'wroclaw': "Wrocław",
        # 'lodz': "Łódź",
        # 'poznan': "Poznań",
        # 'zielona-gora': "Zielona Góra",
        # 'gorzow-wielkopolski': "Gorzów Wielkopolski",
        # 'kielce': "Kielce"
    }
    for_sale_conditions = [False]
    estates = ['dom']

    links = []

    for city, city_name in cities.items():
        for for_sale in for_sale_conditions:
            for estate in estates:
                page_number = 1
                if city == 'zielona-gora':
                    city = 'zielonagora'
                if city == 'gorzow-wielkopolski':
                    city = 'gorzow'

                sale_or_rent = None
                if for_sale is True:
                    sale_or_rent = 'sprzedaz'
                if for_sale is False:
                    sale_or_rent = 'wynajem'

                estate = "mieszkania" if estate == "mieszkanie" else "domy"

                while True:
                    try:
                        page = get(
                            f'https://www.olx.pl/d/nieruchomosci/{estate}/{sale_or_rent}/{city}/?page={page_number}',
                            allow_redirects=False
                        ).content
                        bs = BeautifulSoup(page, 'html.parser')
                        offers = bs.find_all('div', class_='css-14fnihb')

                        scrap = offers[0].find_all("a", class_="css-1bbgabe")
                        page_number += 1

                        for endpoint in scrap:
                            if not endpoint['href'].startswith('http'):
                                link = 'https://www.olx.pl' + endpoint['href']
                                links.append((link, city_name, estate, for_sale))

                        if bs.find('div', class_='css-wsrviy'):
                            break
                    except Exception as e:
                        print(f'olx_get_links_to_offers: {e}')
    return links
