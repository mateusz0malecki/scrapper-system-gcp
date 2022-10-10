from bs4 import BeautifulSoup
from requests import get


class OffersScrapper:
    def __init__(self, link: tuple):
        self._link = link[0]
        self._city = link[1]
        self._category = link[2]
        self._html = self._get_html()
        self._bs = BeautifulSoup(self._html, 'html.parser')

    def scrap(self) -> dict:
        earning_values = self._get_earning_values()
        response = {
            "link": self._link,
            "city": self._city,
            "category": self._category,
            "title": self._get_title(),
            "company_name": self._get_company_name(),
            "earning_value_from": earning_values[0],
            "earning_value_to": earning_values[1],
            "contract_type": self._get_contract_type(),
            "seniority": self._get_seniority(),
            "working_time": self._get_working_time(),
            "remote_recruitment": self._get_remote_recruitment(),
        }
        return response

    def _get_html(self) -> bytes:
        page = get(self._link).content
        return page

    def _get_title(self):
        try:
            title = self._bs.find('div', class_='app-offer__title').get_text().strip()
        except Exception:
            title = None
        return title

    def _get_company_name(self):
        company_name = None
        try:
            company_name_div = self._bs.find('div', class_='app-offer__main-item app-offer__main-item--employer')
            if company_name_div:
                company_name = company_name_div.get_text().split('Profil firmy')[0].strip()
        except Exception:
            company_name = None
        return company_name

    def _get_seniority(self):
        seniority = None
        try:
            seniority_div = self._bs.find('div', class_='app-offer__header-item app-offer__header-item--job-level')
            if seniority_div:
                seniority = seniority_div.get_text().strip()
        except Exception:
            seniority = None
        return seniority

    def _get_earning_values(self):
        earning_value_from = None
        earning_value_to = None
        try:
            salary_div = self._bs.find('div', class_='app-offer__salary')
            if salary_div:
                salary_text = salary_div.get_text().strip().split('-')
                earning_value_from = int(''.join([i for i in salary_text[0].split(',')[0] if i.isdigit()]))
                earning_value_to = int(''.join([i for i in salary_text[1].split(',')[0] if i.isdigit()]))
                if earning_value_from < 300:
                    earning_value_from *= 160
                if earning_value_to < 300:
                    earning_value_to *= 160
        except Exception:
            earning_value_from = None
            earning_value_to = None
        return earning_value_from, earning_value_to

    def _get_working_time(self):
        working_time = None
        try:
            working_time_div = self._bs.find(
                'div',
                class_='app-offer__header-item app-offer__header-item--working-time'
            )
            if working_time_div:
                working_time = working_time_div.get_text().strip()
        except Exception:
            working_time = None
        return working_time

    def _get_contract_type(self):
        contract_type = None
        try:
            contract_type_div = self._bs.find(
                'div',
                class_='app-offer__header-item app-offer__header-item--employment-type'
            )
            if contract_type_div:
                contract_type = contract_type_div.get_text().strip()
        except Exception:
            contract_type = None
        return contract_type

    def _get_remote_recruitment(self):
        remote_recruitment = None
        try:
            remote_recruitment_div = self._bs.find(
                'div',
                class_='app-offer__header-item app-offer__header-item--online-recruitment'
            )
            if remote_recruitment_div:
                remote_recruitment = True
        except Exception:
            remote_recruitment = None
        return remote_recruitment
