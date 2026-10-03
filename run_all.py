# Runs all the tests and opens the report.
#   python run_all.py          -> all tests
#   python run_all.py smoke    -> only smoke tests
import os
import subprocess
import sys
import webbrowser

command = [sys.executable, "-m", "pytest"]
if len(sys.argv) > 1:
    command += ["-m", sys.argv[1]]

exit_code = subprocess.call(command)

report = os.path.abspath("reports/report.html")
if os.path.exists(report):
    print("\nReport: " + report)
    webbrowser.open("file:///" + report.replace("\\", "/").lstrip("/"))

if exit_code == 0:
    print("RESULT: all tests passed")
else:
    print("RESULT: some tests failed")
sys.exit(exit_code)
