#!/usr/bin/env python3
'''
Task 0: write async coroutine that delays for & returns a random wait time
'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    ''' Wait for a random number of seconds. '''
    wait_time = random.uniform(0, max_delay)
    await asyncio.sleep(wait_time)
    return wait_time
