def add_numbers(a: int, b: int) -> int:
    """
    Add two numbers and return the result.
    
    Args:
        a (int): First number
        b (int): Second number
        
    Returns:
        int: Sum of the two numbers
    Example:
    >>> add_numbers(5, 10)
    15
    """
    return a + b

    

def concat_numbers_as_string(a: int, b: int) -> str:
    """
    Concatenate two numbers as strings and return the result.
    
    Args:
        a (int): First number
        b (int): Second number
        
    Returns:
        str: Concatenated string of the two numbers
    Example:
    >>> concat_numbers_as_string(5, 10)
    '510'
    """
    return str(a) + str(b)
