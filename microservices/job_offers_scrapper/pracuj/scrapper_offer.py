from bs4 import BeautifulSoup
from requests import get
from datetime import date, timedelta


class OffersScrapper:
    def __init__(self, link: tuple):
        self._link = link[0]
        self._city = link[1]
        self._category = link[2]
        self._html = self._get_html()
        self._bs = BeautifulSoup(self._html, 'html.parser')

    def scrap(self) -> dict:
        extra_elements = self._get_extra_elements()
        response = {
            "link": self._link,
            "city": self._city,
            "category": self._category,
            "title": self._get_title(),
            "company_name": self._get_company_name(),
            "earning_value_from": self._get_earning_value_from(),
            "earning_value_to": self._get_earning_value_to(),
            "contract_type": extra_elements["contract_type"],
            "seniority": extra_elements["seniority"],
            "offer_deadline": extra_elements["offer_deadline"],
            "working_mode": extra_elements["working_mode"],
            "working_time": extra_elements["working_time"],
            "remote_recruitment": extra_elements["remote_recruitment"],
            "immediate_employment": extra_elements["immediate_employment"],
            "responsibilities": self._get_responsibilities(),
            "requirements": self._get_requirements(),
            "benefits": self._get_benefits(),
        }
        return response

    def _get_html(self) -> bytes:
        page = get(self._link).content
        return page

    def _get_title(self):
        try:
            title = self._bs.find('h1', class_='offer-viewkHIhn3').get_text()
        except Exception:
            title = None
        return title

    def _get_company_name(self):
        try:
            company_name = self._bs.find('h2', class_='offer-viewwtdXJ4').get_text().split('O firmie')[0]
        except Exception:
            company_name = None
        return company_name

    def _get_earning_value_from(self):
        try:
            value_from = self._bs.find('span', class_='offer-viewZGJhIB')
            earning_value_from = ''.join([i for i in value_from.get_text() if i.isdigit()]) if value_from else None
        except Exception:
            earning_value_from = None
        return earning_value_from

    def _get_earning_value_to(self):
        try:
            value_to = self._bs.find('span', class_='offer-viewYo2KTr')
            earning_value_to = ''.join([i for i in value_to.get_text() if i.isdigit()]) if value_to else None
        except Exception:
            earning_value_to = None
        return earning_value_to

    def _get_extra_elements(self):
        elements = self._bs.find_all('li', class_='offer-viewdQMogN')
        extra_elements = {
            "contract_type": None,
            "seniority": None,
            "offer_deadline": None,
            "working_mode": None,
            "working_time": None,
            "remote_recruitment": None,
            "immediate_employment": None
        }
        for element in elements:
            if element.find(
                    'div',
                    {'class': 'offer-viewXo2dpV', "data-test": 'sections-benefit-contracts-text'}
            ):
                extra_elements["contract_type"] = element.get_text()
            if element.find(
                    'div',
                    {'class': 'offer-viewXo2dpV', "data-test": 'sections-benefit-employment-type-name-text'}
            ):
                extra_elements["seniority"] = element.get_text()
            if element.find(
                    'div',
                    {'class': 'offer-viewXo2dpV', "data-test": 'sections-benefit-work-modes-text'}
            ):
                extra_elements["working_mode"] = element.get_text()
            if element.find(
                    'div',
                    {'class': 'offer-viewXo2dpV', "data-test": 'sections-benefit-work-schedule-text'}
            ):
                extra_elements["working_time"] = element.get_text()
            if element.find('div', class_='offer-view5VS8w0'):
                deadline = element.find(
                    'div',
                    {'class': 'offer-viewRKwqEV', "data-test": 'text-benefit'}
                ).get_text()
                days = ''.join([i for i in deadline if i.isdigit()])
                if len(days) == 0:
                    extra_elements["offer_deadline"] = date.today() + timedelta(days=30)
                else:
                    extra_elements["offer_deadline"] = date.today() + timedelta(days=int(days) - 1)
            if element.find('div', {"data-test": "sections-benefit-remote-recruitment-text"}):
                extra_elements["remote_recruitment"] = True
            if element.find('div', {"data-test": "sections-benefit-immediate-employment-text"}):
                extra_elements["immediate_employment"] = True
        return extra_elements

    def _get_responsibilities(self):
        responsibilities = []
        try:
            responsibilities_table = self._bs.find('div', {'class': 'offer-viewIPoRwg', "data-test": 'section-responsibilities'})
            if responsibilities_table:
                responsibilities_objects = responsibilities_table.find_all('p', {"class": "offer-viewchej5g"})
                for item in responsibilities_objects:
                    responsibilities.append(item.get_text())
        except Exception:
            pass
        return responsibilities

    def _get_requirements(self):
        requirements = []
        try:
            requirements_table = self._bs.find('div', {'class': 'offer-viewIPoRwg', "data-test": 'section-requirements'})
            if requirements_table:
                requirements_table_expected = requirements_table.find(
                    'div',
                    {"class": "offer-viewfjH4z3", "data-test": "section-requirements-expected"}
                )
                if requirements_table_expected:
                    requirements_objects_expected = requirements_table_expected.find_all('p', {"class": "offer-viewchej5g"})
                    for item in requirements_objects_expected:
                        requirements.append(
                            {
                                "requirement": item.get_text(),
                                "must_have": True
                            }
                        )
                requirements_table_optional = requirements_table.find(
                    'div',
                    {"class": "offer-viewfjH4z3", "data-test": "section-requirements-optional"}
                )
                if requirements_table_optional:
                    requirements_objects_optional = requirements_table_optional.find_all('p', {"class": "offer-viewchej5g"})
                    for item in requirements_objects_optional:
                        requirements.append(
                            {
                                "requirement": item.get_text(),
                                "must_have": False
                            }
                        )
        except Exception:
            pass
        return requirements

    def _get_benefits(self):
        benefits = []
        try:
            benefits_table = self._bs.find('ul', class_="offer-view7CmY-p offer-viewF0WZVq")
            if benefits_table:
                benefits_objects = benefits_table.find_all(
                    'p',
                    {"class": "offer-view4bdC6U", "data-test": "text-benefit-title"}
                )
                for item in benefits_objects:
                    benefits.append(item.get_text())
        except Exception:
            pass
        return benefits
