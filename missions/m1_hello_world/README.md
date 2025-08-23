# Mission 1: Hello World

## Learning Objectives
- Understand basic Python function syntax
- Learn how to define and call functions
- Practice printing output to the console
- Get familiar with string literals

## Concepts Covered
- Function definition with `def`
- Print statements
- String literals
- Function documentation with docstrings
- Basic program structure

## Mission Description
Your first mission is to create a simple function that prints a greeting message. This is the traditional "Hello, World!" program that introduces you to basic Python syntax.

## What You'll Build
A function called `mission()` that:
- Takes no parameters
- Prints the exact string "Hello, World!" to the console
- Uses the `print()` function to display output

## Key Code Concepts

### Function Definition
```python
def mission() -> None:
    """
    Prints a greeting message to the console.
    
    This function demonstrates basic Python syntax by printing
    the traditional "Hello, World!" message.
    """
    print("Hello, World!")
```

### Print Function
The `print()` function is used to display output to the console. It automatically adds a newline character at the end.

### Type Hints
The `-> None` indicates that this function doesn't return a value - it just performs an action (printing).

## Tasks to Complete
1. ✅ Create a function named `mission()`
2. ✅ Make it print the exact string "Hello, World!"
3. ✅ Add proper documentation with a docstring
4. ✅ Use type hints to indicate the function returns None

## Running Your Code
```bash
# Run the script directly
python main.py

# Run the tests
pytest tests.py -v
```

## Expected Output
When you run `main.py` or call `mission()`, you should see:
```
Hello, World!
```

## Test Requirements
Your function must pass these tests:
- Prints exactly "Hello, World!" (captured by pytest's `capsys`)
- The output must match the expected string exactly
- No extra characters, spaces, or newlines beyond what `print()` adds

## Understanding the Test
The test uses `capsys` (capture system output) to verify that your function prints the correct message:

```python
def test_hello_world(capsys):
    mission()
    captured = capsys.readouterr()
    assert captured.out == "Hello, World!"
```

## Next Steps
Once you complete this mission, you'll be ready for Mission 2 where you'll learn about variables and different data types!
