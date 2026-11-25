import pytest
from app.database import initialize_database
from app.service import create_task, get_task, complete_task, TaskNotFoundError

def test_create_task_strips_surrounding_whitespace(tmp_path):
    db = str(tmp_path / "unit.db")
    initialize_database(db)
    task = create_task(db, "  Prepare report  ")
    assert task["title"] == "Prepare report"
    assert task["completed"] is False

def test_create_task_rejects_blank_title(tmp_path):
    db = str(tmp_path / "unit.db")
    initialize_database(db)
    with pytest.raises(ValueError, match="cannot be blank"):
        create_task(db, "   ")

def test_get_task_raises_for_unknown_id(tmp_path):
    db = str(tmp_path / "unit.db")
    initialize_database(db)
    with pytest.raises(TaskNotFoundError):
        get_task(db, 999)

def test_complete_task_changes_status(tmp_path):
    db = str(tmp_path / "unit.db")
    initialize_database(db)
    task = create_task(db, "Run tests")
    assert complete_task(db, task["id"])["completed"] is True
