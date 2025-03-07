from celery_app import celery_app

from tasks.cpu_intensive_task import cpu_intensive_task
from tasks.memory_intensive_task import memory_intensive_task
from tasks.request_task import request_task


@celery_app.task()
def add_experiment_tasks_to_queue():
    for _ in range(20):
        request_task.delay()

    for _ in range(2):
        cpu_intensive_task.delay()
        memory_intensive_task.delay()

    return "Hello World"
