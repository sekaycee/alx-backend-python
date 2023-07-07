#!/usr/bin/env python3
'''
Task: 9: Annotate function’s parameters and return values
with the appropriate types
'''
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    ''' Compute the length of a list of sequences. '''
    return [(i, len(i)) for i in lst]
