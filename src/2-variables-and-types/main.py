def create_variables():
    """
    Create variables of different types and return them as a dictionary.
    
    Returns:
        dict: A dictionary containing:
            - 'name': a string with your name
            - 'age': an integer representing age
            - 'height': a float representing height in meters
            - 'is_student': a boolean indicating if you're a student
    """
    # TODO: Create the variables and return them in a dictionary
    name = "Alice"
    age = 25
    height = 1.75
    is_student = True
    
    return {
        'name': name,
        'age': age,
        'height': height,
        'is_student': is_student
    }


def calculate_info(name, birth_year):
    """
    Calculate information about a person.
    
    Args:
        name (str): The person's name
        birth_year (int): The year they were born
        
    Returns:
        str: A formatted string with their info
    """
    current_year = 2025
    age = current_year - birth_year
    return f"Hello {name}, you are {age} years old!"


if __name__ == "__main__":
    variables = create_variables()
    print("Variables created:", variables)
    
    info = calculate_info("Bob", 1995)
    print(info)
