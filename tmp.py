def add_numbers(a: str, b):
    """
    >>> add_numbers(1, 2)
    3
    >>> add_numbers(-1, 1)
    0
    >>> add_numbers(1.5, 2.5)
    4.0
    >>> add_numbers('one', 'two')
    Traceback (most recent call last):
        ...
    TypeError: arguments must be integers
    >>> add_numbers([1, 2], [3, 4])
    Traceback (most recent call last):
        ...
    TypeError: arguments must be integers
    >>> add_numbers(True, False)
    Traceback (most recent call last):
        ...
    TypeError: arguments must be integers
    """
    if type(a) not in (int, float):
        raise TypeError('arguments must be integers')

    if type(b) not in (int, float):
        raise TypeError('arguments must be integers')

    return a + b
