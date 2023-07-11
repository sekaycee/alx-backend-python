#!/usr/bin/env python3
''' task 0: Write async coroutine to generate ten random numbers.'''
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    ''' generate 10 random numbers asynchronously '''
    for i in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
