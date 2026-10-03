# Automated End-to-End QA Framework for Web Applications

Mini project for Software Testing and Quality Assurance (STQA).

## What is this project about?
Testing a website by hand again and again is slow and boring. In this project we made a small
framework that does the same checks automatically. It opens a real browser, logs in, adds and
deletes tasks, and checks whether the website behaves correctly. It also tests the website's API.

To have something to test, the project comes with a small demo website (login page + task list).
You can also test your own website by giving its address.

## What is inside

| Folder / file | What it does |
|---|---|
| `demo_app/` | The demo website we test (Flask) |
| `framework/pages/` | One class per page (Page Object Model) |
| `framework/utils/` | Logger and a helper to read test data |
| `config/settings.py` | Settings like browser and website address |
| `tests/ui/` | Browser tests (login, tasks) |
| `tests/api/` | API tests |
| `tests/data/` | Test data in a json file |
| `docs/` | Test plan, test cases, defect report format, screenshots |
| `run_all.py` | Runs everything and opens the report |

## How to run

```
pip install -r requirements.txt
playwright install chromium
python run_all.py
```

Other ways:

```
python -m pytest               # all tests
python -m pytest -m smoke      # only the quick basic tests
python -m pytest -m api        # only API tests
python -m pytest -m negative   # only wrong-input tests
```

On Windows you can also double-click `run_tests.bat`.

The report is created at `reports/report.html`. If a test fails, a screenshot is saved in
`reports/screenshots/`.

To test a different website, set its address first:
`BASE_URL=https://your-site.com python -m pytest` (on Windows: `set BASE_URL=https://your-site.com`).
To watch the browser while it runs: `HEADLESS=false`.

## Login for the demo website
- admin / admin123
- tester / test@123

## Things covered by the tests
- login with correct and wrong details, empty fields, a SQL injection text
- opening the dashboard without login, and after logout
- adding, deleting a task, adding an empty task, a `<script>` text as a task
- API: health check, create, list, delete, wrong input

Total: 19 tests.
