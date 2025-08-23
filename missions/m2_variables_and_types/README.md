# Mission 2: Variables and Types

## Learning Objectives
- Understand Python's basic data types (str, int, float, bool)
- Learn variable assignment and naming conventions
- Practice working with dictionaries
- Understand string formatting and calculations

## Concepts Covered
- Variable assignment
- Data types: string, integer, float, boolean
- Dictionary creation and manipulation
- String formatting with f-strings
- Basic arithmetic operations
- Function parameters and return values

## Mission Description
In this mission, you'll work with Python's fundamental data types and learn how to store and manipulate different kinds of information. You'll create variables, perform calculations, and organize data using dictionaries.

## What You'll Build
Two main functions:
1. `create_variables()` - Creates and returns variables of different types
2. `calculate_info()` - Performs calculations and formats strings

## Key Code Concepts

### Variable Types
```python
name = "Alice"           # String (str)
age = 25                 # Integer (int)
height = 1.75            # Float (float)
is_student = True        # Boolean (bool)
```

### Dictionary Creation
```python
return {
    'name': name,
    'age': age,
    'height': height,
    'is_student': is_student
}
```

### String Formatting
```python
current_year = 2025
age = current_year - birth_year
return f"Hello {name}, you are {age} years old!"
```

## Tasks to Complete
1. ✅ Create variables of different types (string, int, float, bool)
2. ✅ Return them organized in a dictionary
3. ✅ Calculate a person's age from birth year
4. ✅ Format a greeting message with calculated values
5. ✅ Use proper variable naming conventions

## Variable Naming Best Practices
- Use lowercase with underscores: `birth_year`
- Be descriptive: `is_student` not `flag`
- Avoid Python keywords: `class`, `def`, `return`, etc.

## Running Your Code
```bash
# Run the script directly
python main.py

# Run the tests
pytest tests.py -v
```

## Expected Output
When you run `main.py`, you should see something like:
```
Variables created: {'name': 'Alice', 'age': 25, 'height': 1.75, 'is_student': True}
Hello Bob, you are 30 years old!
```

## Test Requirements
Your code must pass these tests:
- `create_variables()` returns a dictionary with correct keys
- Each variable has the correct data type
- `calculate_info()` correctly calculates age
- String formatting works properly
- Variables contain valid values (non-negative age, positive height, etc.)

## Common Mistakes to Avoid
- ❌ Using quotes around numbers: `age = "25"` (this makes it a string!)
- ❌ Forgetting to return the dictionary
- ❌ Incorrect key names in the dictionary
- ❌ Wrong calculation in age formula

## Next Steps
Once you master variables and types, Mission 3 will introduce you to lists and loops for handling multiple pieces of data!
