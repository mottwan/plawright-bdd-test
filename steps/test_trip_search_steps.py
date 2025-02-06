from datetime import date

import pytest
from playwright.sync_api import expect
from pytest_bdd import scenarios, given, when, then, parsers

from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from utils.airport_code_enum import AirPortCode

scenarios('../features/trip_search.feature')


@pytest.fixture
def home_page(page):
    return HomePage(page)


@pytest.fixture(scope="session")
def context():
    """A dictionary to store shared data between steps."""
    return {}


@pytest.fixture
def results_page(page):
    return SearchResultsPage(page)


@pytest.mark.basic_search
@given(parsers.parse('As a not logged-in user, navigate to the homepage "{page_url}"'))
def navigate_to_homepage(page_url: str, home_page, context) -> None:
    context.update({"page_url": page_url})
    home_page.navigate(page_url)


@when(parsers.parse('I select "{trip_type}" trip type'))
def select_trip(trip_type: str, home_page) -> None:
    if trip_type == 'one-way':
        home_page.select_one_way_trip()


@when(parsers.parse('Set the "{location}" airport "{airport_code}"'))
def set_location_airport(location: str, airport_code: AirPortCode, home_page) -> None:
    if location == "departure":
        home_page.set_from_airport(airport_code)
    if location == "arrival":
        home_page.set_to_airport(airport_code)


@when(parsers.parse('Set the departure time {numeric_value} "{unit}" in the future starting from the current date'))
def set_departure_time(numeric_value: int, unit: str, home_page) -> None:
    home_page.set_departure_date(numeric_value, unit)


@when("Uncheck the Check accommodation with booking.com option")
def uncheck_accommodation(home_page):
    home_page.uncheck_accommodation()


@when("Click the search button")
def click_button(home_page, context):
    context["page_url"] += home_page.get_search_button_href_value()
    home_page.click_search()


@then("I am redirected to the search results page")
def verify_search_results(results_page, context):
    result_page_url = context.get('page_url')
    page = results_page.get_page()

    results_page.results_list_is_visible()
    results_page.quick_navigation_date_is_visible(date.today())

    expect(page).to_have_url(result_page_url)
