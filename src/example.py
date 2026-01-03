"""
Example Python module for testing MCP server PR template selection.
"""


def calculate_sum(a: int, b: int) -> int:
    """Calculate the sum of two numbers.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        The sum of a and b
    """
    return a + b


def calculate_product(a: int, b: int) -> int:
    """Calculate the product of two numbers.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        The product of a and b
    """
    return a * b


def greet(name: str) -> str:
    """Greet someone by name.
    
    Args:
        name: The person's name
        
    Returns:
        A greeting string
    """
    return f"Hello, {name}!"


def divide(a: int, b: int) -> float:
    """Divide two numbers.
    
    Args:
        a: Numerator
        b: Denominator (must not be zero)
        
    Returns:
        The result of a divided by b
        
    Raises:
        ValueError: If b is zero
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(base: int, exponent: int) -> int:
    """Raise a number to a power.
    
    Args:
        base: The base number
        exponent: The exponent
        
    Returns:
        base raised to the power of exponent
    """
    return base ** exponent


if __name__ == "__main__":
    print(f"Sum: {calculate_sum(5, 3)}")
    print(f"Product: {calculate_product(5, 3)}")
    print(greet("World"))
