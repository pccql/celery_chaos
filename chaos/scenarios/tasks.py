import docker
import redis
from fastapi import APIRouter

tasks_router = APIRouter(prefix="/tasks", tags=["Tasks"])

redis_client = redis.StrictRedis(host="redis", port=6379, db=0)
docker_client = docker.from_env()


# TODO
# Memory exhaustion (resource pressure).
# Redis broker delays (communication bottlenecks).
# Worker termination (unexpected crashes).
# CPU Saturation


@tasks_router.post("/redis_add_delay")
def redis_add_delay(delay_ms: int = 1000):
    # Find the Redis container by name
    redis_container = docker_client.containers.get("redis")

    command = f"tc qdisc add dev eth0 root netem delay {delay_ms}ms"
    exit_code, output = redis_container.exec_run(command)

    if exit_code != 0:
        raise Exception(f"Failed to introduce delay: {output.decode()}")

    return {"status": f"Redis delay of {delay_ms}ms introduced"}


@tasks_router.post("/redis_delay_clear")
def redis_delay_clear():
    redis_container = docker_client.containers.get("redis")

    command = "tc qdisc del dev eth0 root"
    exit_code, output = redis_container.exec_run(command)

    if exit_code != 0:
        raise Exception(f"Failed to clear delay: {output.decode()}")

    return {"status": "Redis delay cleared"}


@tasks_router.post("/memory_exhaustion")
def memory_exhaustion():
    worker_container = docker_client.containers.get("worker")

    command = (
        'python -c "import time; memory_hog = []; '
        "[(memory_hog.append(' ' * 10**6), time.sleep(0.1)) for _ in range(1000000)]\""
    )

    worker_container.exec_run(command, detach=True)

    return {"status": "Memory exhaustion triggered in worker"}


@tasks_router.post("/worker_termination")
def worker_termination():
    worker_container = docker_client.containers.get("worker")
    worker_container.kill()

    return {"status": "Worker terminated"}


@tasks_router.post("/cpu_exhaustion")
def cpu_exhaustion():
    worker_container = docker_client.containers.get("worker")

    command = 'python -c "[x**x for x in range(1000000)]"'

    worker_container.exec_run(command, detach=True)

    return {"status": "CPU exhaustion triggered in worker"}
