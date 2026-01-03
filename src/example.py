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


if __name__ == "__main__":
    print(f"Sum: {calculate_sum(5, 3)}")
    print(f"Product: {calculate_product(5, 3)}")
    print(greet("World"))
