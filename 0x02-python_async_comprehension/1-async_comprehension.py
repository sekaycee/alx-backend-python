#!/usr/bin/env python3
''' task 1: same as task 0 but use async comprehension '''
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''
    collect 10 random numbers using an async comprehension over
    async_generator and returns the 10 random numbers.
    '''
    return [x async for x in async_generator()]
