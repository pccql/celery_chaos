import numpy as np
from celery_app import celery_app


@celery_app.task
def memory_intensive_task(size: int = 100_000_000):
    """
    Simulates a memory-bound task by creating a large array in memory.

    :param size: Number of elements in the array.
    :return: Sum and mean of the generated data.
    """
    # Generate a massive NumPy array
    data = np.random.rand(size)

    # Perform memory-intensive computation
    result_sum = np.sum(data)
    result_mean = np.mean(data)

    return {
        "sum": result_sum,
        "mean": result_mean,
        "array_size": size,
    }
