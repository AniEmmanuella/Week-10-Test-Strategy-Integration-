# Injected Failure and Recovery

1. In `app/service.py`, temporarily change `clean_title = title.strip()` to `clean_title = title`.
2. Run `pytest tests/test_service_unit.py::test_create_task_strips_surrounding_whitespace`.
3. Confirm the test fails because surrounding spaces are retained.
4. Restore `clean_title = title.strip()`.
5. Run `pytest` and confirm the full suite passes.

## Analysis
- Defect: input normalization was removed.
- Detection: the whitespace-normalization unit test fails.
- Impact: inconsistent titles may be stored.
- Fix: trim the title before inserting it.
- Verification: rerun the focused test and the full suite.

Capture screenshots of the failing test, passing recovery run and successful GitHub Actions run. This exercise is documented but has not been performed as part of package generation.
