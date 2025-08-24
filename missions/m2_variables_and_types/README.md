# Mission 2: Variables and Types

## Learning Objectives
- Understand Python's basic data types (str, int)
- Learn function parameters and return types
- Practice arithmetic operations and type conversion
- Understand the difference between mathematical operations and string operations

## Concepts Covered
- Function definition with type hints
- Integer arithmetic (addition)
- Type conversion (int to str)
- String concatenation
- Return statements with specific types

## Mission Description
In this mission, you'll implement two fundamental functions that demonstrate the difference between mathematical operations and string operations on numbers. You'll learn how the same numbers can be treated as mathematical values or as text depending on what you want to accomplish.

## What You'll Build
Two main functions:
1. `add_numbers(a: int, b: int) -> int` - Performs mathematical addition
2. `concat_numbers_as_string(a: int, b: int) -> str` - Concatenates numbers as text

## Key Code Concepts

### Function with Type Hints
```python
def add_numbers(a: int, b: int) -> int:
    """Add two numbers mathematically."""
    return a + b
```

### Type Conversion and String Concatenation
```python
def concat_numbers_as_string(a: int, b: int) -> str:
    """Convert numbers to strings and concatenate them."""
    return str(a) + str(b)
```

### The Difference Between + Operations
```python
# Mathematical addition
5 + 10 = 15

# String concatenation
"5" + "10" = "510"
```

## Tasks to Complete
1. ✅ Implement `add_numbers()` to perform mathematical addition
2. ✅ Implement `concat_numbers_as_string()` to concatenate numbers as strings
3. ✅ Use proper type hints for parameters and return values
4. ✅ Handle both positive and negative numbers correctly
5. ✅ Ensure return types match the function signatures

## Examples

### Mathematical Addition
```python
add_numbers(5, 10)    # Returns: 15
add_numbers(-3, 7)    # Returns: 4
add_numbers(0, 5)     # Returns: 5
```

### String Concatenation
```python
concat_numbers_as_string(5, 10)    # Returns: "510"
concat_numbers_as_string(-3, 7)    # Returns: "-37" 
concat_numbers_as_string(0, 5)     # Returns: "05"
```

## Running Your Code
```bash
# Run the script directly
python main.py

# Run the tests
pytest tests.py -v
```

## Expected Behavior
- `add_numbers(5, 10)` should return the integer `15`
- `concat_numbers_as_string(5, 10)` should return the string `"510"`
- Both functions should handle negative numbers correctly
- Return types must match the function signatures exactly

## Test Requirements
Your code must pass these tests:
- `add_numbers()` returns correct mathematical sum as integer
- `concat_numbers_as_string()` returns correct concatenated string
- Functions handle positive, negative, and zero values
- Return types are exactly as specified (int vs str)
- Functions work with various number combinations

## Common Mistakes to Avoid
- ❌ Returning a string from `add_numbers()`: should return int, not str
- ❌ Returning an int from `concat_numbers_as_string()`: should return str, not int
- ❌ Forgetting to convert integers to strings before concatenation
- ❌ Not handling negative numbers properly in string concatenation

## Type Conversion Reminder
```python
# Convert int to str
num = 42
text = str(num)  # "42"

# This is concatenation, not addition
str(5) + str(10)  # "510"

# This is addition, not concatenation  
5 + 10  # 15
```

## Next Steps
Once you master basic types and operations, Mission 3 will introduce you to lists and loops for handling collections of data!
