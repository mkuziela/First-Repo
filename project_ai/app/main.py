from fastapi import FastAPI, UploadFile, File, HTTPException
from celery.result import AsyncResult
import shutil
import os
import uuid
from app.worker import process_image_task
from app.tasks import detect_people_on_image

app = FastAPI(title="System Liczenia Osób")


@app.get("/local")
def count_local(path: str):
    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="Plik nie istnieje")
    count = detect_people_on_image(path)
    return {"people_count": count}


@app.get("/process-url")
def process_url(url: str):
    task = process_image_task.delay("url", url)
    return {"task_id": task.id, "status": "queued"}


@app.post("/upload")
async def upload_image(file: UploadFile = File(...)):

    filename = f"{uuid.uuid4()}_{file.filename}"
    file_path = os.path.join("uploaded_images", filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    task = process_image_task.delay("file", file_path)
    return {"task_id": task.id, "status": "queued"}


@app.get("/status/{task_id}")
def get_status(task_id: str):
    result = AsyncResult(task_id)
    response = {"status": result.state}
    if result.state == 'SUCCESS':
        response["data"] = result.result
    elif result.state == 'FAILURE':
        response["error"] = str(result.result)
    return response