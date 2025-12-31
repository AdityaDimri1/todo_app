import sqlite3
from app.logging_config import logger

DB_FILE = "app/tasks.db"


def get_db_connection():
    """
    Create and return a new SQLite database connection.
    """
    try:
        conn = sqlite3.connect(DB_FILE)
        conn.row_factory = sqlite3.Row  # Optional: return rows as dict-like objects
        return conn
    except Exception as e:
        logger.error(f"Error connecting to database: {e}")
        raise


def init_db():
    """
    Initialize the tasks database with the 'tasks' table.
    """
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                due_date TEXT,
                status TEXT NOT NULL
            )
            """
        )
        conn.commit()
        conn.close()
        logger.info("Database initialized successfully.")
    except Exception as e:
        logger.error(f"Error initializing database: {e}")
        raise
