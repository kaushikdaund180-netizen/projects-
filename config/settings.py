# All the settings live here. Any of them can be changed with an environment variable,
# for example:  BROWSER=firefox python -m pytest
import os

BASE_URL = os.getenv("BASE_URL", "")            # empty -> framework starts the bundled demo app
DEMO_PORT = int(os.getenv("DEMO_PORT", "5055"))
HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
BROWSER = os.getenv("BROWSER", "chromium")      # chromium | firefox | webkit
SLOW_MO = int(os.getenv("SLOW_MO", "0"))
DEFAULT_TIMEOUT_MS = int(os.getenv("TIMEOUT_MS", "5000"))
SCREENSHOT_DIR = os.getenv("SCREENSHOT_DIR", "reports/screenshots")
