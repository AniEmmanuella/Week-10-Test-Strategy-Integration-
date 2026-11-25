from app.database import connect

class TaskNotFoundError(Exception):
    pass

def create_task(db_path: str, title: str) -> dict:
    clean_title = title.strip()
    if not clean_title:
        raise ValueError("Task title cannot be blank.")
    with connect(db_path) as connection:
        cursor = connection.execute(
            "INSERT INTO tasks (title, completed) VALUES (?, 0)", (clean_title,)
        )
        task_id = cursor.lastrowid
    return {"id": task_id, "title": clean_title, "completed": False}

def get_task(db_path: str, task_id: int) -> dict:
    with connect(db_path) as connection:
        row = connection.execute(
            "SELECT id, title, completed FROM tasks WHERE id = ?", (task_id,)
        ).fetchone()
    if row is None:
        raise TaskNotFoundError(f"Task {task_id} was not found.")
    return {
        "id": row["id"],
        "title": row["title"],
        "completed": bool(row["completed"])
    }

def complete_task(db_path: str, task_id: int) -> dict:
    with connect(db_path) as connection:
        cursor = connection.execute(
            "UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,)
        )
        if cursor.rowcount == 0:
            raise TaskNotFoundError(f"Task {task_id} was not found.")
    return get_task(db_path, task_id)
