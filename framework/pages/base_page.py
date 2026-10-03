from framework.utils.logger import get_logger

log = get_logger()


class BasePage:
    # every page class inherits from this one, so the common steps are written only once

    def __init__(self, page, base_url):
        self.page = page
        self.base_url = base_url.rstrip("/")

    def open(self, path="/"):
        log.info("opening %s%s", self.base_url, path)
        self.page.goto(self.base_url + path)

    def click(self, selector):
        log.info("click %s", selector)
        self.page.click(selector)

    def fill(self, selector, value):
        log.info("type in %s", selector)
        self.page.fill(selector, value)

    def text_of(self, selector):
        return self.page.inner_text(selector).strip()

    def is_visible(self, selector):
        return self.page.is_visible(selector)
