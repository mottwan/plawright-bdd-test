from datetime import datetime

from playwright.sync_api import Page, Locator

from pages.base_page import BasePage
from utils.datetime_utils import to_abbreviated_date_format


class SearchResultsPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.results_list = self.selector('[data-test="ResultList"]')
        self.quick_navigation_date = self.selector('[data-test="QuickNavigationDate"]')

    def get_page(self):
        return self.page

    def results_list_is_visible(self) -> Locator:
        return self.results_list.is_visible()

    def quick_navigation_date_is_visible(self, date_string: datetime) -> Locator:
        return self.quick_navigation_date.filter(has_text=to_abbreviated_date_format(date_string)).is_visible()

    def get_result_card(self, index: int):
        return self.selector('[data-test="ResultCardWrapper"]')[index]

    def get_result_departure_location(self, card_index: int, index: int):
        return self.get_result_card(card_index).locator('[data-test="ResultCardStopPlace"]')[index]

