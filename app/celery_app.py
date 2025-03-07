from celery import Celery
from celery.schedules import crontab

celery_app = Celery(
    "celery_app",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/1",
)

celery_app.conf.imports = ["tasks"]

celery_app.conf.beat_schedule = {
    "hello-world-every-minute": {
        "task": "tasks.add_experiment_tasks_to_queue.add_experiment_tasks_to_queue",
        "schedule": crontab(),
    }
}


celery_app.conf.task_acks_late = True
celery_app.conf.task_reject_on_worker_lost = True
