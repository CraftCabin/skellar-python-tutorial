# Mission 5: Functions and Modules

## Learning Objectives
- Master advanced function concepts and parameter types
- Learn error handling with exceptions
- Understand module imports and usage
- Practice function design patterns
- Implement mathematical algorithms

## Concepts Covered
- Function parameters: default, *args, **kwargs
- Exception handling with `raise` and `try/except`
- Module imports (`import math`)
- Function documentation and type hints
- Algorithm implementation (Fibonacci sequence)
- Input validation and error handling

## Mission Description
Functions are the building blocks of larger programs. This mission covers advanced function concepts that you'll use in real-world programming: flexible parameters, error handling, and algorithm implementation.

## What You'll Build
Six advanced functions demonstrating different concepts:
1. `calculate_circle_area()` - Error handling and validation
2. `calculate_rectangle_area()` - Multiple parameters with validation
3. `greet_user()` - Default parameters and customization
4. `calculate_total_cost()` - Variable arguments (*args) and keyword parameters
5. `create_user_profile()` - Flexible keyword arguments (**kwargs)
6. `fibonacci_sequence()` - Algorithm implementation with recursion alternative

## Key Code Concepts

### Default Parameters
```python
def greet_user(name, greeting="Hello", punctuation="!"):
    return f"{greeting}, {name}{punctuation}"
```

### Variable Arguments (*args)
```python
def calculate_total_cost(*prices, tax_rate=0.08):
    subtotal = sum(prices)  # prices is a tuple of all arguments
    return subtotal * (1 + tax_rate)
```

### Keyword Arguments (**kwargs)
```python
def create_user_profile(**kwargs):
    profile = {
        'name': kwargs.get('name', 'Unknown'),
        'age': kwargs.get('age', 0)
    }
    return profile
```

### Exception Handling
```python
def calculate_circle_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2
```

### Module Usage
```python
import math
area = math.pi * radius ** 2  # Using math.pi constant
```

## Tasks to Complete
1. ✅ Implement functions with input validation
2. ✅ Use default parameters for customizable behavior
3. ✅ Handle variable numbers of arguments with *args
4. ✅ Create flexible interfaces with **kwargs
5. ✅ Raise appropriate exceptions for invalid inputs
6. ✅ Import and use standard library modules

## Function Design Patterns

### Validation Pattern
```python
def function_with_validation(param):
    if not valid_condition(param):
        raise ValueError("Descriptive error message")
    # Continue with valid input
```

### Default + Override Pattern
```python
def flexible_function(required_param, optional="default"):
    # Use optional parameter or its default
    return f"{required_param} with {optional}"
```

### Builder Pattern with **kwargs
```python
def create_object(**kwargs):
    obj = {}
    obj['field1'] = kwargs.get('field1', default1)
    obj['field2'] = kwargs.get('field2', default2)
    # Add any extra fields
    for key, value in kwargs.items():
        if key not in obj:
            obj[key] = value
    return obj
```

## Running Your Code
```bash
# Run the script directly
python main.py

# Run the tests
pytest tests.py -v
```

## Expected Output
When you run `main.py`, you should see:
```
Circle area (radius 5): 78.53981633974483
Rectangle area (4x6): 24
Greeting: Hello, Alice!
Custom greeting: Hi, Bob.
Total cost: 48.61
User profile: {'name': 'Charlie', 'age': 25, 'email': 'charlie@example.com', 'occupation': 'Student', 'location': 'Unknown', 'hobby': 'coding'}
Fibonacci (10): [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

## Test Requirements
Your code must pass these tests:
- Mathematical calculations are accurate
- Exceptions are raised for invalid inputs
- Default parameters work correctly
- Variable arguments are handled properly
- Keyword arguments create complete profiles
- Fibonacci sequence is generated correctly
- Edge cases are handled (empty inputs, negative values)

## Common Mistakes to Avoid
- ❌ Not validating inputs before processing
- ❌ Using mutable default arguments: `def func(items=[]):`
- ❌ Forgetting to handle edge cases in algorithms
- ❌ Not importing required modules
- ❌ Raising generic `Exception` instead of specific types

## Error Handling Best Practices
- Use specific exception types (`ValueError`, `TypeError`)
- Provide descriptive error messages
- Validate inputs early in the function
- Don't catch exceptions unless you can handle them meaningfully

## Module Usage Tips
- Import only what you need: `from math import pi`
- Use descriptive aliases: `import numpy as np`
- Organize imports at the top of files
- Understand the difference between built-in and third-party modules

## Next Steps
Mission 6 will introduce object-oriented programming with classes, bringing together all the concepts you've learned in a powerful new paradigm!
