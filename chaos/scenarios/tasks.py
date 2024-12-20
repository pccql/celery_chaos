import json

import redis
from fastapi import APIRouter

tasks_router = APIRouter(prefix="/tasks", tags=["Tasks"])

redis_client = redis.StrictRedis(host="redis", port=6379, db=0)


@tasks_router.post("/inject-bad-task")
async def inject_bad_task(queue: str = "hello_queue"):
    """
    Inject a malformed or invalid task into the queue.
    """
    bad_task = {
        "headers": {
            "id": "bad-task",
            "task": "unknown_task",
            "argsrepr": "()",
            "kwargsrepr": "{}",
        },
        "body": {"args": [], "kwargs": {}},
        "content-type": "application/json",
        "content-encoding": "utf-8",
    }
    redis_client.lpush(queue, json.dumps(bad_task))
    return {"status": "success", "message": "Injected a bad task"}
