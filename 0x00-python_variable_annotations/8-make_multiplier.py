#!/usr/bin/env python3
'''
Define make_multiplier function
'''


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''make_multiplier function'''
    def multiply(x: float) -> float:
        return x * multiplier
    return multiply
