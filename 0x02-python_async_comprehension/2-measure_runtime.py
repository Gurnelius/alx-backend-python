#!/usr/bin/env python3
'''
Module to measure runtime
'''
import asyncio
from time import time
async_comprehension = __import__('1_async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that measures the total runtime for executing async_comprehension
    four times in parallel using asyncio.gather.
    Returns the total runtime.
    """
    start_time = time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time()
    return end_time - start_time
