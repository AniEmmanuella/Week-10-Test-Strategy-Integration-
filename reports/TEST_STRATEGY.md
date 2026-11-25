# Test Strategy

## Scope
The Task Service exposes health, task creation, retrieval and completion operations.

## Test levels
- **Unit:** service validation and business rules.
- **Integration:** persistence through real temporary SQLite databases.
- **API:** HTTP status codes, JSON payloads, validation and error handling through FastAPI TestClient.

## Fixtures and isolation
`tmp_path` creates a unique database for each test. `monkeypatch` redirects the app to that database. The `client` fixture supplies the HTTP test client. Tests therefore do not share a developer's local database.

## Mocking decision
The service tests use a real temporary database because persistence is part of the behaviour under test. Mocking the database would conceal integration defects. This sample has no external service dependency to mock.

## CI and coverage
GitHub Actions runs the test suite on Python 3.11 and 3.12 for pushes and pull requests to `main`. The pipeline fails if tests fail or total statement coverage is below 75%.

## Limitations
This is a compact SQLite teaching API. It does not implement authentication, authorization, load testing or production database validation.
