# Mission 1: Hello World

## Learning Objectives
- Understand basic Python function syntax
- Learn how to define and call functions
- Practice returning values from functions
- Get familiar with string data types

## Concepts Covered
- Function definition with `def`
- Return statements
- String literals
- Function documentation with docstrings
- The `if __name__ == "__main__":` pattern

## Mission Description
Your first mission is to create a simple function that returns a greeting message. This is the traditional "Hello, World!" program that introduces you to basic Python syntax.

## What You'll Build
A function called `hello_world()` that:
- Takes no parameters
- Returns the string "Hello, World!"
- Can be executed directly or imported by other modules

## Key Code Concepts

### Function Definition
```python
def hello_world():
    """
    Returns a greeting message.
    
    Returns:
        str: The greeting "Hello, World!"
    """
    return "Hello, World!"
```

### Docstrings
The triple-quoted string immediately after the function definition is called a docstring. It documents what the function does, its parameters, and return value.

### Main Guard
```python
if __name__ == "__main__":
    print(hello_world())
```
This pattern allows the file to be both:
- Run directly as a script (prints the greeting)
- Imported as a module (doesn't automatically print)

## Tasks to Complete
1. ✅ Create a function named `hello_world()`
2. ✅ Make it return the exact string "Hello, World!"
3. ✅ Add proper documentation
4. ✅ Include a main section that prints the result

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
Hello, World!
```

## Test Requirements
Your function must pass these tests:
- Returns exactly "Hello, World!"
- Returns a string type
- Returns a non-empty string

## Next Steps
Once you complete this mission, you'll be ready for Mission 2 where you'll learn about variables and different data types!
