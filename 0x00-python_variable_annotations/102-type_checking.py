#!/usr/bin/env python3
'''
Implement zoom_array() function
'''


from typing import Tuple, List


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    """
    Creates a new list by repeating each item in the input list
    `lst` `factor` times.

    Args:
        lst (Tuple[int, ...]): The input list of integers.
        factor (int, optional): The number of times each item in
        `lst` should be repeated.
        Defaults to 2.

    Returns:
        List[int]: The new list with repeated items.

    Example:
        >>> zoom_array((1, 2, 3), 3)
        [1, 1, 1, 2, 2, 2, 3, 3, 3]
    """

    zoomed_in: List[int] = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
