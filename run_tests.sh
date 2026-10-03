#!/usr/bin/env bash
# Usage: ./run_tests.sh [pytest args]   e.g. ./run_tests.sh -m smoke
set -e
python -m pytest "$@"
echo "HTML report: reports/report.html"
