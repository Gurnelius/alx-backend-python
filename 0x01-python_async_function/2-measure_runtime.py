#!/usr/bin/env python3
'''
Module to measure runtime
'''

import asyncio
from time import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay) and
    returns the average time per task.

    Args:
        n (int): The number of tasks.
        max_delay (int): The maximum delay in seconds.

    Returns:
        float: The average execution time per task.
    """
    start_time = time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time()
    total_time = end_time - start_time
    return total_time / n
