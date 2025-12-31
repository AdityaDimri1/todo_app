from app.database import get_db_connection
from app.schemas import TaskCreate
from app.logging_config import logger


def create_task(task: TaskCreate) -> int:
    """
    Insert a new task into the database and return its ID.
    """
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO tasks (title, description, due_date, status) VALUES (?, ?, ?, ?)",
            (task.title, task.description, task.due_date, task.status),
        )
        conn.commit()
        task_id = cursor.lastrowid
        conn.close()
        logger.info(f"Task '{task.title}' created with ID {task_id}.")
        return task_id
    except Exception as e:
        logger.error(f"Error creating task: {e}")
        raise


def get_tasks():
    """
    Retrieve all tasks from the database.
    """
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tasks")
        tasks = cursor.fetchall()
        conn.close()
        return tasks
    except Exception as e:
        logger.error(f"Error fetching tasks: {e}")
        raise


def mark_task_completed(task_id: int):
    """
    Mark a task as completed.
    """
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE tasks SET status = 'completed' WHERE id = ?", (task_id,)
        )
        conn.commit()
        conn.close()
        logger.info(f"Task {task_id} marked as completed.")
    except Exception as e:
        logger.error(f"Error completing task {task_id}: {e}")
        raise


def delete_task(task_id: int):
    """
    Delete a task by its ID.
    """
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()
        conn.close()
        logger.info(f"Task {task_id} deleted successfully.")
    except Exception as e:
        logger.error(f"Error deleting task {task_id}: {e}")
        raise
