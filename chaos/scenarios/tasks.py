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
