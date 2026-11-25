# Test Matrix

| ID | Level | Scenario | Expected result | Test module |
|---|---|---|---|---|
| UT-01 | Unit | Title has surrounding spaces | Title is trimmed | `test_service_unit.py` |
| UT-02 | Unit | Blank title | `ValueError` | `test_service_unit.py` |
| UT-03 | Unit | Unknown task ID | `TaskNotFoundError` | `test_service_unit.py` |
| UT-04 | Unit | Complete an existing task | Completion flag is true | `test_service_unit.py` |
| IT-01 | Integration | Create then retrieve across connections | Retrieved record matches | `test_integration.py` |
| API-01 | API | Health check | HTTP 200 | `test_api.py` |
| API-02 | API | Create and retrieve task | HTTP 201 then 200 | `test_api.py` |
| API-03 | API | Whitespace-only title | HTTP 422 | `test_api.py` |
| API-04 | API | Unknown task | HTTP 404 | `test_api.py` |
| API-05 | API | Complete task | HTTP 200; completed true | `test_api.py` |

## CI matrix
| Python | Suite | Coverage gate |
|---|---|---|
| 3.11 | Full pytest suite | At least 75% |
| 3.12 | Full pytest suite | At least 75% |
