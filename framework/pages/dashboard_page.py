from framework.pages.base_page import BasePage


class DashboardPage(BasePage):
    # locators
    WELCOME = "#welcome"
    INPUT = "#item-input"
    ADD_BUTTON = "#add-btn"
    ITEM_NAMES = "#item-list li .name"
    DELETE_BUTTON = ".delete-btn"
    LOGOUT = "#logout"
    MESSAGE = "#msg"

    def welcome_text(self):
        return self.text_of(self.WELCOME)

    def add_item(self, name):
        self.fill(self.INPUT, name)
        self.click(self.ADD_BUTTON)

    def items(self):
        return self.page.locator(self.ITEM_NAMES).all_inner_texts()

    def delete_first(self):
        self.page.locator(self.DELETE_BUTTON).first.click()

    def message(self):
        if self.is_visible(self.MESSAGE):
            return self.text_of(self.MESSAGE)
        return ""

    def logout(self):
        self.click(self.LOGOUT)
