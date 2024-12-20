from celery import Celery
from celery.schedules import crontab
from kombu import Queue

celery_app = Celery(
    "celery_app",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/1",
)

celery_app.conf.imports = ["tasks"]

celery_app.worker_send_task_events = True
celery_app.task_send_sent_event = True

celery_app.conf.task_routes = {
    "tasks.hello_world.hello_world": {"queue": "hello_queue"},
}

celery_app.conf.task_queues = (Queue("hello_queue"),)

celery_app.conf.beat_schedule = {
    "hello-world-every-minute": {
        "task": "tasks.hello_world.hello_world",
        "schedule": crontab(),
    },
}
