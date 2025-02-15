import sqlite3
from fastapi import FastAPI, HTTPException
from src.executor import execute_task
from src.file_handler import read_file

app = FastAPI()

@app.post("/run")
async def run_task(task: str):
    try:
        result = execute_task(task)
        return {"status": "success", "output": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.get("/read")
async def read_file_content(path: str):
    content = read_file(path)
    if content is None:
        raise HTTPException(status_code=404, detail="File not found")
    return {"content": content}

