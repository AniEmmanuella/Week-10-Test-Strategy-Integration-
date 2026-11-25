# Intermediate Week 10 — Test Strategy, Integration Testing & Continuous Integration

A runnable sample Python API demonstrating unit, integration and API testing, isolated pytest fixtures, coverage, and GitHub Actions CI.

**Curriculum note:** Intermediate Week 10 specifies applying tests to a Project 2 or Project 3 repository. This package includes a sample service so the workflow runs immediately. If your existing Intermediate Project 2/3 has different business logic, adapt the tests to that project before claiming it satisfies the prerequisite.

## Setup (PowerShell)
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Run tests and coverage
```powershell
pytest
pytest --cov=app --cov-report=term-missing
```

## Run API
```powershell
uvicorn app.main:app --reload
```
Open `http://127.0.0.1:8000/docs`.

## CI
`.github/workflows/ci.yml` runs tests on Python 3.11 and 3.12 for pushes and pull requests to `main`. After pushing, inspect the GitHub Actions tab. A local pass does not prove the remote workflow passed.

## Injected failure
Follow `reports/INJECTED_FAILURE.md`, capture the failing test, restore the fix, rerun the suite and capture the passing output.

## Before submission
- [ ] Local tests pass.
- [ ] Coverage report reviewed.
- [ ] Injected failure and recovery evidence captured.
- [ ] GitHub Actions run is green.
- [ ] Demo recording or live URL prepared.
