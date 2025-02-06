import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def context(browser):
    context = browser.new_context()
    yield context
    context.close()


@pytest.fixture(scope="session", autouse=True)
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=700, args=["--start-maximized"])
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()