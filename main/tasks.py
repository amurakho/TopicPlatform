from celery import shared_task
from TopicPlatform.celery import app

@app.task
def add(x, y):
    return x + y