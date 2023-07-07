#!/usr/bin/env python3
''' Task 5: Write a type-annotated function sum_list '''

from typing import List
from functools import reduce


def sum_list(input_list: List[float]) -> float:
    ''' Compute the sum of a list of floating-point numbers. '''
    total = reduce(lambda a, b: a + b, input_list)
    return total
