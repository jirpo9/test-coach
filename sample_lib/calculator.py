"""Sample calculator library with basic arithmetic functions."""
def add(a: int, b: int) -> int:
    """Return the sum of a and b."""
    return a + b

def divide(a: int, b: int) -> float:
    """Return a divided by b. May raise ZeroDivisionError if b is zero."""
    return a / b  # note: ZeroDivisionError if b == 0