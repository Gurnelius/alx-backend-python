#!/usr/bin/env python3
'''
Define safely_get_value function
'''


from typing import Mapping, Any, Union, TypeVar


T = TypeVar('T')


def safely_get_value(
        dct: Mapping[Any, Any], key: Any,
        default: Union[T, None] = None) -> Union[Any, T]:
    '''Get value from dictionary'''
    if key in dct:
        return dct[key]
    else:
        return default
