import os
import threading

import pytest
from werkzeug.serving import make_server

from config import settings
from demo_app.app import create_app
from framework.pages.dashboard_page import DashboardPage
from framework.pages.login_page import LoginPage


@pytest.fixture(scope="session")
def base_url():
    # if BASE_URL is given we test that site, otherwise we start our own demo site
    if settings.BASE_URL:
        yield settings.BASE_URL
        return

    server = make_server("127.0.0.1", settings.DEMO_PORT, create_app())
    t = threading.Thread(target=server.serve_forever, daemon=True)
    t.start()
    yield "http://127.0.0.1:%d" % settings.DEMO_PORT
    server.shutdown()


@pytest.fixture(scope="session")
def browser():
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        pytest.skip("playwright is not installed")

    with sync_playwright() as p:
        try:
            b = getattr(p, settings.BROWSER).launch(headless=settings.HEADLESS, slow_mo=settings.SLOW_MO)
        except Exception:
            pytest.skip("browser not installed, run: playwright install " + settings.BROWSER)
        yield b
        b.close()


@pytest.fixture
def page(browser, base_url, request):
    # a new clean browser window for every test
    context = browser.new_context()
    pg = context.new_page()
    pg.set_default_timeout(settings.DEFAULT_TIMEOUT_MS)
    yield pg

    # after the test: if it failed, save a screenshot
    result = getattr(request.node, "rep_call", None)
    if result is not None and result.failed:
        os.makedirs(settings.SCREENSHOT_DIR, exist_ok=True)
        pg.screenshot(path=os.path.join(settings.SCREENSHOT_DIR, request.node.name + ".png"))
    context.close()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # remembers if the test passed or failed, needed for the screenshot above
    outcome = yield
    report = outcome.get_result()
    setattr(item, "rep_" + report.when, report)


@pytest.fixture
def login_page(page, base_url):
    return LoginPage(page, base_url).load()


@pytest.fixture
def dashboard(page, base_url, login_page):
    # logs in first, then gives the dashboard page
    login_page.login("admin", "admin123")
    return DashboardPage(page, base_url)
