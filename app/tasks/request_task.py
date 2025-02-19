import requests
from celery_app import celery_app


@celery_app.task
def request_task(url: str = "https://jsonplaceholder.typicode.com/todos/1"):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
