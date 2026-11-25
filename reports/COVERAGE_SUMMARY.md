# Coverage Summary

Executed locally with Python 3.13.5.

- Command: `PYTHONPATH=. python -m pytest -q --cov=app --cov-report=term-missing`
- Result: **10 passed**
- Total statement coverage: **95%**
- `app/database.py`: 100%
- `app/main.py`: 94%
- `app/service.py`: 96%
- CI threshold configured: 75%

The local result does not prove the remote GitHub Actions workflow passed. Inspect the Actions tab after pushing.
