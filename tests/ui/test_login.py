import pytest

from framework.utils.data_loader import load_json

data = load_json("login_data.json")

pytestmark = pytest.mark.ui


@pytest.mark.smoke
@pytest.mark.parametrize("user", data["valid"], ids=lambda u: u["username"])
def test_valid_login(login_page, page, user):
    login_page.login(user["username"], user["password"])
    page.wait_for_url("**/dashboard")
    assert user["username"] in page.inner_text("#welcome")


@pytest.mark.negative
@pytest.mark.parametrize("case", data["invalid"], ids=lambda c: c["username"][:6] + "|" + c["password"][:6])
def test_invalid_login(login_page, case):
    login_page.login(case["username"], case["password"])
    assert login_page.error_message() == case["error"]


def test_dashboard_needs_login(page, base_url):
    # opening dashboard directly should send us back to login
    page.goto(base_url + "/dashboard")
    assert page.url.endswith("/login")


def test_logout(dashboard, page, base_url):
    dashboard.logout()
    page.goto(base_url + "/dashboard")
    assert page.url.endswith("/login")
