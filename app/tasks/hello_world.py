from celery_app import celery_app

from tasks.request_task import request_task


@celery_app.task()
def hello_world():
    for _ in range(20):
        request_task.delay()

    return "Hello World"
