import math


def calculate_circle_area(radius):
    """
    Calculate the area of a circle.
    
    Args:
        radius (float): Radius of the circle
        
    Returns:
        float: Area of the circle
        
    Raises:
        ValueError: If radius is negative
    """
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    
    return math.pi * radius ** 2


def calculate_rectangle_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Args:
        length (float): Length of the rectangle
        width (float): Width of the rectangle
        
    Returns:
        float: Area of the rectangle
        
    Raises:
        ValueError: If length or width is negative
    """
    if length < 0 or width < 0:
        raise ValueError("Length and width must be non-negative")
    
    return length * width


def greet_user(name, greeting="Hello", punctuation="!"):
    """
    Greet a user with customizable greeting and punctuation.
    
    Args:
        name (str): Name of the user
        greeting (str): Greeting word (default: "Hello")
        punctuation (str): Punctuation to use (default: "!")
        
    Returns:
        str: Formatted greeting
    """
    return f"{greeting}, {name}{punctuation}"


def calculate_total_cost(*prices, tax_rate=0.08):
    """
    Calculate total cost including tax for multiple items.
    
    Args:
        *prices: Variable number of item prices
        tax_rate (float): Tax rate as decimal (default: 0.08)
        
    Returns:
        float: Total cost including tax
    """
    subtotal = sum(prices)
    tax = subtotal * tax_rate
    return round(subtotal + tax, 2)


def create_user_profile(**kwargs):
    """
    Create a user profile from keyword arguments.
    
    Args:
        **kwargs: Arbitrary keyword arguments for user data
        
    Returns:
        dict: User profile with default values for missing fields
    """
    profile = {
        'name': kwargs.get('name', 'Unknown'),
        'age': kwargs.get('age', 0),
        'email': kwargs.get('email', 'no-email@example.com'),
        'location': kwargs.get('location', 'Unknown'),
        'occupation': kwargs.get('occupation', 'Student')
    }
    
    # Add any additional fields that were provided
    for key, value in kwargs.items():
        if key not in profile:
            profile[key] = value
    
    return profile


def fibonacci_sequence(n):
    """
    Generate the first n numbers in the Fibonacci sequence.
    
    Args:
        n (int): Number of Fibonacci numbers to generate
        
    Returns:
        list: First n Fibonacci numbers
        
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i-1] + sequence[i-2])
    
    return sequence


if __name__ == "__main__":
    # Test the functions
    print("Circle area (radius 5):", calculate_circle_area(5))
    print("Rectangle area (4x6):", calculate_rectangle_area(4, 6))
    print("Greeting:", greet_user("Alice"))
    print("Custom greeting:", greet_user("Bob", "Hi", "."))
    print("Total cost:", calculate_total_cost(10.99, 25.50, 8.75))
    
    profile = create_user_profile(
        name="Charlie", 
        age=25, 
        email="charlie@example.com",
        hobby="coding"
    )
    print("User profile:", profile)
    
    print("Fibonacci (10):", fibonacci_sequence(10))
