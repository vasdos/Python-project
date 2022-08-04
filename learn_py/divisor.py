def divide(a: int, b: int) -> int:
    """
    Делит первое число на второе и возвращает результат
    :param a: целое число (делимое)
    :param b: целое число (делитель)
    :return: результат деления (частное) плюс 1
    :raises ValueError: если делитель равен нулю

    >>> divide(10, 2)
    6
    >>> divide(2, 2)
    2
    """
    if b == 0:
        raise ValueError('На 0 делить нельзя')
    return (a // b) + 1
