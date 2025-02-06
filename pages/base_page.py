from typing import TypeVar

from playwright.sync_api import Page, Locator

T = TypeVar("T")


class BasePage(object):

    def __init__(self, page: Page):
        self.page = page

    def keyboard(self):
        return self.page.keyboard

    def mouse(self):
        return self.page.mouse

    def title_contains(self, text: str):
        title = self.page.title()
        if title.find(text) == -1:
            raise Exception("No {} was found in page title".format(text))
        return title

    def url_contains(self, text: str):
        page_url = self.page.url
        if page_url.find(text) == -1:
            raise Exception("No {} was found in page url".format(text))
        return page_url

    def navigate(self, url: str):
        self.page.goto(url)
        self.page.click('[data-test="CookiesPopup-Accept"]')

    def selector(self, selector: T):
        return self.page.locator(str(selector))
