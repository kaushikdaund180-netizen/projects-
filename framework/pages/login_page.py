from framework.pages.base_page import BasePage


class LoginPage(BasePage):
    # locators
    USERNAME = "#username"
    PASSWORD = "#password"
    LOGIN_BUTTON = "#login-btn"
    ERROR = "#error"

    def load(self):
        self.open("/login")
        return self

    def login(self, username, password):
        self.fill(self.USERNAME, username)
        self.fill(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)

    def error_message(self):
        # returns empty text when there is no error on the page
        if self.is_visible(self.ERROR):
            return self.text_of(self.ERROR)
        return ""
