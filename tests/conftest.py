import pytest
from fastapi.testclient import TestClient
from app import main
from app.database import initialize_database

@pytest.fixture
def test_db(tmp_path, monkeypatch):
    db_path = str(tmp_path / "test_tasks.db")
    monkeypatch.setattr(main, "DB_PATH", db_path)
    initialize_database(db_path)
    return db_path

@pytest.fixture
def client(test_db):
    return TestClient(main.app)
