#!/usr/bin/env python3
'''
Task 4: code similar to task 3 except task_wait_random is being called.
'''
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    ''' execute task_wait_random n times. '''
    wait_times = await asyncio.gather(
        *tuple(task_wait_random(max_delay) for i in range(n))
    )
    return sorted(wait_times)
