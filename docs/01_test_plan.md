# Test Plan

**1. Aim**
Check that the web application works correctly (login, tasks, API) using automated tests instead of manual testing.

**2. What we test**
Login and logout, page protection (session), adding and deleting tasks, input checks, and the API.
We do not test speed / load, different phone screens, or third-party services.

**3. How we test**

| Type | Method | Tool |
|---|---|---|
| Functional (end-to-end) | Black-box, Page Object Model | Playwright + pytest |
| API | Check status code and response | requests + pytest |
| Negative and boundary | Wrong and empty inputs | pytest parametrize |
| Basic security | SQL injection text, script text | automated checks |
| Regression | Re-run smoke tests after a change | `pytest -m smoke` |

**4. Environment**
Python 3.10 or above, Chromium browser, Flask demo app (or any website using BASE_URL).

**5. Entry and exit criteria**
Start: website is running and test data is ready.
Finish: all smoke tests pass, at least 95% of all tests pass, and there is no open critical defect.

**6. Risks**
- Element ids change on the page, so tests break. Fix: keep locators only inside page classes.
- Tests depending on each other. Fix: each test uses a fresh browser context.

**7. What we submit**
Test plan, test cases, automation code, HTML report, defect report.
