#!/usr/bin/env python3
''' Task 8: Write a type-annotated function make_multiplier '''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    ''' Create a multiplier function. '''
    return lambda x: x * multiplier
