#!/usr/bin/env python3
'''
Module to wait_random
'''

import asyncio
import random
from typing import Union


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between
    0 and max_delay seconds, and eventually returns the delay.

    Args:
        max_delay (int): The maximum delay in seconds. Default is 10.

    Returns:
        float: The actual delay in seconds.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
