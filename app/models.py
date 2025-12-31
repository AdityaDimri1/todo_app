"""
This file defines the Task data model as a plain Python class.
As per the assignment instructions, NO ORM is used.

The actual database schema is created using raw SQL
inside database.py.
"""

class Task:
    def __init__(self, id, title, description, due_date, status):
        self.id = id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def to_dict(self):
        """
        Convert Task object to dictionary format
        (useful for JSON responses).
        """
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "status": self.status
        }
