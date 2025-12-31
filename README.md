# 🌟 To-Do List Web Application

## 🎯 Objective

This project is a **To-Do List web application** built using **Python and FastAPI**. It provides **RESTful APIs** for managing tasks and uses **HTML templates** for rendering a user-friendly interface.

Users can:

- ✅ Create tasks
- ✅ View all tasks
- ✅ Mark tasks as complete
- ✅ Delete tasks
- ✅ Interact with tasks via the web interface

**Constraints and Guidelines Followed**:

- ❌ No ORM
- ❌ No Generic ViewSet
- ✅ Raw SQL queries only
- ✅ RESTful API design
- ✅ Templates for UI
- ✅ Automated testing with Pytest
- ✅ Logging and exception handling

---

## 🛠 Tech Stack

- **Backend Framework**: FastAPI
- **Database**: SQLite (raw SQL via `sqlite3`)
- **Templates**: Jinja2
- **Testing**: Pytest
- **Styling**: CSS (custom)
- **API Documentation**: Swagger UI / ReDoc (auto-generated)

---

## 📁 Project Structure

todo_app/
│
├── app/
│ ├── main.py # FastAPI application
│ ├── database.py # SQLite DB setup & connection
│ ├── crud.py # Task CRUD operations
│ ├── schemas.py # Pydantic models for tasks
│ ├── logging_config.py # Logger setup
│ ├── templates/
│ │ ├── base.html
│ │ ├── tasks.html
│ │ └── add_task.html
│ └── static/
│ └── styles.css
│
├── tests/
│ └── test_tasks.py # Pytest tests
│
├── requirements.txt
└── README.md

---

## 🗄 Database Design

**Table: `tasks`**

| Column      | Type    | Description                                |
| ----------- | ------- | ------------------------------------------ |
| id          | INTEGER | Primary Key                                |
| title       | TEXT    | Task title                                 |
| description | TEXT    | Task description                           |
| due_date    | TEXT    | Task due date                              |
| status      | TEXT    | Task status (`pending` or `completed`) |

> The database schema is automatically created at application startup using **raw SQL** in `database.py`. No ORM is used.

---

## 🔌 API Endpoints

| Method | Endpoint                     | Description            |
| ------ | ---------------------------- | ---------------------- |
| POST   | `/api/tasks`               | Create a new task      |
| GET    | `/api/tasks`               | Retrieve all tasks     |
| POST   | `/api/tasks/{id}/complete` | Mark task as completed |
| POST   | `/api/tasks/{id}/delete`   | Delete a task          |

## Example: Create Task Request

{
"title": "Complete assignment",
"description": "Finish To-Do List project",
"due_date": "2025-01-10",
"status": "pending"
}

---

## 🖥 Web Interface

- **Tasks Page**: Displays all tasks with their current status.
- **Add Task Page**: Form to create a new task.

**Buttons:**

- **Complete ✅** – Marks task as completed
- **Delete 🗑** – Removes task from the database
- **Back ⬅** – Returns to the main tasks page

Completed tasks appear grayed out with a strikethrough. Buttons are styled for a clean, modern UI using custom CSS.

---

## 🚀 Installation & Running the Application

### Clone the repository

git clone `<your-repo-url>`
cd todo_app

### Create and activate a virtual environment

python3 -m venv venv
source venv/bin/activate # Linux/Mac
venv\Scripts\activate # Windows CMD

### Install dependencies

pip install -r requirements.txt

### Start the FastAPI server

uvicorn app.main:app --reload

### Access the application

- Web UI: http://127.0.0.1:8000/
- Swagger API Docs: http://127.0.0.1:8000/docs
- ReDoc API Docs: http://127.0.0.1:8000/redoc

---

## 🧪 Testing

### Set PYTHONPATH (Linux/Mac)

export PYTHONPATH=$PWD

### Set PYTHONPATH (Windows CMD)

set PYTHONPATH=%CD%

### Run Pytest

pytest -v

Tests cover: **Create**, **Read**, **Complete**, **Delete** tasks.

Example output:

tests/test_tasks.py::test_create_task PASSED
tests/test_tasks.py::test_get_tasks PASSED
tests/test_tasks.py::test_complete_task PASSED
tests/test_tasks.py::test_delete_task PASSED

---

## 📄 Notes

- SQLite database file: `app/tasks.db` (auto-created).
- Delete and Complete buttons work directly via UI forms.

**Optional improvements:**

- Edit task functionality.
- Highlight overdue tasks.
- Responsive design for mobile.

---

## 📥 Download & Run (Quick)

git clone `<your-repo-url>`
cd todo_app
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload

Open your browser: http://127.0.0.1:8000/

Optional: run automated tests:

export PYTHONPATH=$PWD
pytest -v

---

## ⚡ License

This project is open-source and free to use for learning and demonstration purposes.
