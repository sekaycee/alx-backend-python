#!/usr/bin/env python3
''' Task 6: Write a type-annotated function sum_mixed_list '''
from typing import List, Union
from functools import reduce


def sum_mixed_list(mixed_list: List[Union[int, float]]) -> float:
    '''
    Compute the sum of a list of integers and floating-point numbers.
    '''
    total = reduce(lambda a, b: a + b, mixed_list)
    return total
