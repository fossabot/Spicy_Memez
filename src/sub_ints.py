def subtract_ints(x: int, y: int):
    """A basic subtraction function with some input control."""
    if x is not int or y is not int:
        try:
            x = int(x)
            y = int(y)
        except ValueError as ve:
            return ve
        except TypeError as te:
            return te

    result = "POSITIVE" if (x-y) > 0 else "NEGATIVE"

    return (x-y, result)
