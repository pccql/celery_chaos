from celery_app import celery_app


def is_prime(n):
    """Check if a number is prime (brute-force method)."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


@celery_app.task
def cpu_intensive_task(limit: int = 500_000):
    """
    Computes prime numbers up to a given limit.

    :param limit: The number up to which we check for prime numbers.
    :return: The count of prime numbers found.
    """
    primes = [n for n in range(limit) if is_prime(n)]
    return {"primes_found": len(primes), "limit": limit}
