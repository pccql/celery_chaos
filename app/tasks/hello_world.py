from celery_app import celery_app


@celery_app.task()
def hello_world():
    return "Hello World"
