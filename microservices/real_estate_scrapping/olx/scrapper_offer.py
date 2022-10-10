from bs4 import BeautifulSoup
from requests import get


class OffersScrapper:
    def __init__(self, link: tuple):
        self._link = link[0]
        self._city = link[1]
        self._estate = link[2]
        self._for_sale = link[3]
        self._html = self._get_html()
        self._bs = BeautifulSoup(self._html, 'html.parser')

    def scrap(self) -> dict:
        extra_elements = self._get_extra_elements()
        prices = self._get_prices()
        pictures = self._get_images()
        instance = {
            "link": self._link,
            "for_sale": self._for_sale,
            "estate": self._estate,
            "city": self._city,
            "id_scrap": self._get_id_scrap(),
            "title": self._get_title(),
            "area": extra_elements.get("area"),
            "number_of_rooms": extra_elements.get("number_of_rooms"),
            "flat_floor": extra_elements.get("flat_floor"),
            "extras": extra_elements.get("extras"),
            "type_of_building": extra_elements.get("type_of_building"),
            "bills_monthly": extra_elements.get("bills_monthly"),
            "market": extra_elements.get("market"),
            "number_of_floors": extra_elements.get("number_of_floors"),
            "price_per_m2": extra_elements.get("price_per_m2"),
            "price": prices[0],
            "rent_price": prices[1],
            "picture1": pictures[0],
            "picture2": pictures[1],
            "picture3": pictures[2],
            "picture4": pictures[3],
            "picture5": pictures[4],
            "picture6": pictures[5],
            "picture7": pictures[6],
            "picture8": pictures[7]
        }
        return instance

    def _get_html(self) -> bytes:
        page = get(self._link).content
        return page

    def _get_id_scrap(self):
        try:
            id_scrap = self._bs.find('span', class_='css-9xy3gn-Text eu5v0x0').get_text()
            id_scrap = ''.join([i for i in id_scrap if i.isdigit()])
        except Exception:
            id_scrap = None
        return id_scrap

    def _get_title(self):
        try:
            title = self._bs.find('h1', class_='css-r9zjja-Text eu5v0x0').get_text()
        except Exception:
            title = None
        return title

    def _get_prices(self):
        try:
            if self._for_sale:
                rent_price = None
                price = self._bs.find('h3', class_='css-okktvh-Text eu5v0x0').get_text()
                price = ''.join([i for i in price if i.isdigit()])
            else:
                price = None
                rent_price = self._bs.find('h3', class_='css-okktvh-Text eu5v0x0').get_text()
                rent_price = ''.join([i for i in rent_price if i.isdigit()])
        except Exception:
            rent_price = None
            price = None
        return price, rent_price

    def _get_extra_elements(self):
        extra_elements = {
            "area": None,
            "number_of_rooms": None,
            "flat_floor": None,
            "extras": None,
            "type_of_building": None,
            "bills_monthly": None,
            "market": None,
            "number_of_floors": None,
            "price_per_m2": None,
        }
        table = self._bs.find_all('p', class_='css-xl6fe0-Text eu5v0x0')
        for element in table:
            detail = element.get_text()
            if detail.startswith('Powierzchnia'):
                area = detail.split(': ')[1]
                extra_elements["area"] = int(area.split(' ')[0].split('.')[0].split(',')[0])
            if detail.startswith('Liczba pokoi'):
                if detail.split(' ')[2] == "Kawalerka":
                    extra_elements["number_of_rooms"] = 1
                else:
                    extra_elements["number_of_rooms"] = int(detail.split(' ')[2])
            if detail.startswith('Poziom'):
                extra_elements["flat_floor"] = detail.split(' ')[1]
            if detail.startswith('Umeblowane'):
                extra_elements["extras"] = 'Umeblowane' if detail.split(' ')[1] == 'Tak' else None
            if detail.startswith('Rodzaj zabudowy'):
                extra_elements["type_of_building"] = ''.join([i for i in detail.split(': ')[1]])
            if detail.startswith('Czynsz'):
                extra_elements["bills_monthly"] = int(detail.split(' ')[2].split('.')[0].split(',')[0])
            if detail.startswith('Rynek'):
                extra_elements["market"] = detail.split(' ')[1]
            if detail.startswith('Liczba pięter'):
                if detail.split(' ')[2] == 'Parterowy':
                    extra_elements["number_of_floors"] = 1
                elif detail.split(' ')[2] == 'Jednopiętrowy':
                    extra_elements["number_of_floors"] = 2
                else:
                    extra_elements["number_of_floors"] = 3
            if detail.startswith('Cena za'):
                price_per_m2 = detail.split(' ')[3]
                extra_elements["price_per_m2"] = int(price_per_m2.split('.')[0].split(',')[0])
        return extra_elements

    def _get_images(self):
        try:
            img = self._bs.find_all('img', alt=self._get_title())
            images = []
            for i in img:
                try:
                    images.append(i['src'])
                except KeyError:
                    try:
                        images.append(i['data-src'].split(' ')[0])
                    except KeyError:
                        pass
            picture1 = images[0] if len(images) > 1 else None
            picture2 = images[1] if len(images) > 2 else None
            picture3 = images[2] if len(images) > 3 else None
            picture4 = images[3] if len(images) > 4 else None
            picture5 = images[4] if len(images) > 5 else None
            picture6 = images[5] if len(images) > 6 else None
            picture7 = images[6] if len(images) > 7 else None
            picture8 = images[7] if len(images) > 8 else None
        except Exception:
            picture1 = None
            picture2 = None
            picture3 = None
            picture4 = None
            picture5 = None
            picture6 = None
            picture7 = None
            picture8 = None
        return picture1, picture2, picture3, picture4, picture5, picture6, picture7, picture8
