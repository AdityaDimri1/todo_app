from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.database import init_db
from app.schemas import TaskCreate
from app import crud
from app.logging_config import logger

app = FastAPI(title="To-Do List API")

# Templates and Static files
templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.on_event("startup")
def startup():
    """Initialize the database at server startup."""
    init_db()
    logger.info("Database initialized")


# ------------------------------
# API Endpoints
# ------------------------------

@app.post("/api/tasks")
def create_task(
    title: str = Form(...),
    description: str = Form(None),
    due_date: str = Form(None),
    status: str = Form("pending"),
):
    """
    Create a new task using form data.
    """
    try:
        task = TaskCreate(
            title=title,
            description=description,
            due_date=due_date,
            status=status,
        )
        task_id = crud.create_task(task)
        return {"id": task_id, **task.dict()}
    except Exception as e:
        logger.error(f"Error creating task: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/tasks")
def list_tasks():
    """
    Retrieve all tasks from the database.
    """
    try:
        tasks = crud.get_tasks()
        return [
            {"id": t[0], "title": t[1], "description": t[2], "due_date": t[3], "status": t[4]}
            for t in tasks
        ]
    except Exception as e:
        logger.error(f"Error retrieving tasks: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/tasks/{task_id}/complete")
def complete_task(task_id: int):
    """
    Mark a task as completed by task ID.
    """
    try:
        crud.mark_task_completed(task_id)
        return RedirectResponse(url="/", status_code=303)
    except Exception as e:
        logger.error(f"Error completing task {task_id}: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/tasks/{task_id}/delete")
def delete_task(task_id: int):
    """
    Delete a task by task ID.
    """
    try:
        crud.delete_task(task_id)
        return RedirectResponse(url="/", status_code=303)
    except Exception as e:
        logger.error(f"Error deleting task {task_id}: {e}")
        raise HTTPException(status_code=500, detail="Could not delete task")


# ------------------------------
# Template Routes
# ------------------------------

@app.get("/", response_class=HTMLResponse)
def view_tasks(request: Request):
    """
    Render the tasks page template.
    """
    tasks = crud.get_tasks()
    return templates.TemplateResponse("tasks.html", {"request": request, "tasks": tasks})


@app.get("/add", response_class=HTMLResponse)
def add_task_form(request: Request):
    """
    Render the add task page template.
    """
    return templates.TemplateResponse("add_task.html", {"request": request})
