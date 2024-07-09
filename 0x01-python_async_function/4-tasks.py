#!/usr/bin/env python3

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with the specified max_delay and
    returns the list of all delays.

    Args:
        n (int): The number of tasks to spawn.
        max_delay (int): The maximum delay in seconds for task_wait_random.

    Returns:
        List[float]: A list of all the delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
