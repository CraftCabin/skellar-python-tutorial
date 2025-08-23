def create_number_list(start, end):
    """
    Create a list of numbers from start to end (inclusive).
    
    Args:
        start (int): Starting number
        end (int): Ending number
        
    Returns:
        list: List of numbers from start to end
    """
    return list(range(start, end + 1))


def sum_list(numbers):
    """
    Calculate the sum of all numbers in a list.
    
    Args:
        numbers (list): List of numbers
        
    Returns:
        int: Sum of all numbers
    """
    total = 0
    for number in numbers:
        total += number
    return total


def find_even_numbers(numbers):
    """
    Find all even numbers in a list.
    
    Args:
        numbers (list): List of numbers
        
    Returns:
        list: List containing only even numbers
    """
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers


def create_shopping_list():
    """
    Create and manipulate a shopping list.
    
    Returns:
        list: A shopping list with at least 5 items
    """
    shopping_list = ["apples", "bread", "milk", "eggs", "cheese"]
    shopping_list.append("bananas")
    shopping_list.insert(0, "tomatoes")
    return shopping_list


if __name__ == "__main__":
    # Test the functions
    numbers = create_number_list(1, 10)
    print("Numbers:", numbers)
    print("Sum:", sum_list(numbers))
    print("Even numbers:", find_even_numbers(numbers))
    print("Shopping list:", create_shopping_list())
