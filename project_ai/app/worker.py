from celery import Celery
import requests
import os
import uuid
from app.tasks import detect_people_on_image

celery_app = Celery(
    "worker",
    broker="amqp://guest:guest@localhost:5672//",
    backend="rpc://"
)


@celery_app.task(name="process_image_task")
def process_image_task(source_type, source_path):

    unique_name = f"{uuid.uuid4()}.jpg"

    output_path = os.path.join("processed_images", unique_name)
    local_input_path = ""


    if source_type == 'url':
        local_input_path = os.path.join("uploaded_images", unique_name)
        try:
            response = requests.get(source_path, stream=True)
            if response.status_code == 200:
                with open(local_input_path, 'wb') as f:
                    f.write(response.content)
            else:
                return {"status": "error", "msg": "Błąd pobierania pliku"}
        except Exception as e:
            return {"status": "error", "msg": str(e)}

    else:
        local_input_path = source_path
        filename = os.path.basename(source_path)
        output_path = os.path.join("processed_images", filename)


    count = detect_people_on_image(local_input_path, output_path)

    return {
        "status": "completed",
        "people_count": count,
        "processed_image": output_path
    }