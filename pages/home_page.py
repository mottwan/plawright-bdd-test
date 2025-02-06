from playwright.async_api import Page
from datetime import date

from pages.base_page import BasePage
from utils.airport_code_enum import AirPortCode
from pages.selectors.home_page_selectors import HomePageSelector
from utils.datetime_utils import time_unit_mapping, calculate_time_delta, get_current_month_name, get_current_year, \
    get_next_month_date, to_iso_date_format

home_page_element = HomePageSelector


class HomePage(BasePage):
    """Page Object Model for the Kiwi.com homepage"""

    def __init__(self, page: Page) -> None:
        BasePage.__init__(self, page)
        self.return_picker = self.selector(home_page_element.RETURN_PICKER)
        self.one_way_trip_option = self.selector(home_page_element.ONE_WAY_TRIP_OPTION)
        self.departure_picker = self.selector(home_page_element.DEPARTURE_PICKER)
        self.departure_input = self.selector(home_page_element.DEPARTURE_INPUT)
        self.departure_option = self.selector(home_page_element.DEPARTURE_OPTION)
        self.destination_picker = self.selector(home_page_element.DESTINATION_PICKER)
        self.destination_input = self.selector(home_page_element.DESTINATION_INPUT)
        self.date_picker = self.selector(home_page_element.DATE_PICKER_INPUT)
        self.accommodation_checkbox = self.selector(home_page_element.ACCOMMODATION_CHECKBOX)
        self.search_button = self.selector(home_page_element.SEARCH_BUTTON)
        self.next_month = self.selector(home_page_element.NEXT_MONTH)
        self.day_picker = self.selector(home_page_element.DAY_PICKER)
        self.month_button = self.selector(home_page_element.MONTH_BUTTON)
        self.selected_date = self.selector(home_page_element.SELECTED_DATE)
        self.set_dates_button = self.selector(home_page_element.SET_DATES)

    def select_one_way_trip(self):
        """Selects one-way trip type"""
        self.return_picker.click()
        self.one_way_trip_option.click()

    def set_from_airport(self, airport_code: AirPortCode):
        """Sets the departure airport"""
        self.departure_picker.click()
        self.departure_input.fill(str(airport_code))
        option_value = self.departure_option.first.inner_text()
        if option_value.startswith("Rotterdam"):
            self.departure_option.first.click()

    def set_to_airport(self, airport_code: AirPortCode):
        """Sets the arrival airport"""
        self.destination_picker.click()
        self.destination_input.fill(str(airport_code))
        option_value = self.departure_option.first.inner_text()
        if option_value.startswith("Madrid"):
            self.departure_option.first.click()

    def set_departure_date(self, time_quantity: int, unit: str):
        """Sets the departure date a specified number of days from today"""
        self.date_picker.click()
        self.__select_future_date(time_quantity, unit)
        self.set_dates_button.click()

    def get_selected_departure_date(self):
        return self.selected_date.inner_text()

    def uncheck_accommodation(self):
        """Unchecks the accommodation checkbox"""
        self.accommodation_checkbox.click()

    def click_search(self):
        """Clicks the search button"""
        self.search_button.click()

    def get_search_button_href_value(self):
        return self.search_button.get_attribute('href')

    def __select_future_date(self, time_quantity: float, unit: str):
        current_date = date.today()
        current_month_name = get_current_month_name(current_date)
        current_year = get_current_year(current_date)
        next_month_name = get_current_month_name(get_next_month_date(current_date))

        current_month = self.month_button.first.filter(has_text="{} {}".format(current_month_name, current_year))
        next_month = self.month_button.last.filter(has_text="{} {}".format(next_month_name, current_year))

        future_date = calculate_time_delta(time_unit_mapping(unit), time_quantity)

        while True:
            try:
                # Try selecting the date
                if current_month.is_visible() and next_month.is_visible():
                    data_value = '[data-value="{}"]'.format(to_iso_date_format(future_date["future_date"]))
                    self.selector(home_page_element.CALENDAR_DAY.format(data_value)).click()
                break
            except Exception as e:
                # If not found, navigate to the next month
                print(f"Navigate to the next month: {e}")
                self.next_month.click()
