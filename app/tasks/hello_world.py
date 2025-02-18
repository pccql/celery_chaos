from celery_app import celery_app

from tasks.memory_intensive_task import memory_intensive_task


@celery_app.task()
def hello_world():
    memory_intensive_task.delay()

    return "Hello World"
