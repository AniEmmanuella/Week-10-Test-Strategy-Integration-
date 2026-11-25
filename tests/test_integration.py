from app.database import initialize_database
from app.service import create_task, get_task

def test_task_persists_between_database_connections(tmp_path):
    db = str(tmp_path / "integration.db")
    initialize_database(db)
    created = create_task(db, "Integration test")
    assert get_task(db, created["id"]) == created
