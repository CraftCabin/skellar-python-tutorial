# Mission 5: Functions and Modules

Welcome to Mission 5! This mission focuses on creating and using functions, understanding different parameter types, and organizing code into modules.

## Learning Objectives

By the end of this mission, you will understand:

1. **Function Definition and Documentation**
   - Creating functions with clear parameter definitions
   - Writing docstrings for documentation
   - Implementing return values

2. **Parameter Types and Flexibility**
   - Default parameters for optional values
   - Variable arguments (*args)
   - Keyword arguments (**kwargs)

3. **Error Handling in Functions**
   - Validating input parameters
   - Raising appropriate exceptions
   - Handling edge cases

4. **Mathematical Operations**
   - Using the math module
   - Implementing mathematical formulas
   - Creating calculation functions

5. **Algorithm Implementation**
   - Recursive and iterative approaches
   - Sequence generation
   - Performance considerations

## Functions Implemented

### 1. Mathematical Calculations

#### `calculate_circle_area(radius)`
Calculates the area of a circle using the formula πr².

**Parameters:**
- `radius` (float): The radius of the circle

**Returns:**
- `float`: The area of the circle

**Features:**
- Input validation (no negative radius)
- Uses math.pi for precision
- Handles edge case of radius = 0

#### `calculate_rectangle_area(width, height)`
Calculates the area of a rectangle using width × height.

**Parameters:**
- `width` (float): The width of the rectangle
- `height` (float): The height of the rectangle

**Returns:**
- `float`: The area of the rectangle

**Features:**
- Validates both dimensions are positive
- Simple multiplication formula
- Clear error messages

### 2. String Operations with Defaults

#### `greet_user(name, greeting="Hello", punctuation="!")`
Creates a personalized greeting message.

**Parameters:**
- `name` (str): The name to greet
- `greeting` (str, optional): Custom greeting word (default: "Hello")
- `punctuation` (str, optional): Ending punctuation (default: "!")

**Returns:**
- `str`: Formatted greeting message

**Features:**
- Default parameters for flexibility
- String formatting
- Customizable components

### 3. Variable Arguments

#### `calculate_total_cost(*prices, tax_rate=0.08)`
Calculates total cost including tax for multiple items.

**Parameters:**
- `*prices`: Variable number of item prices
- `tax_rate` (float, optional): Tax rate as decimal (default: 0.08)

**Returns:**
- `float`: Total cost including tax

**Features:**
- Accepts any number of prices
- Configurable tax rate
- Handles empty price list

### 4. Keyword Arguments

#### `create_user_profile(**kwargs)`
Creates a user profile dictionary with flexible attributes.

**Parameters:**
- `**kwargs`: Any keyword arguments for profile data

**Returns:**
- `dict`: Complete user profile with defaults

**Features:**
- Default values for missing attributes
- Flexible profile creation
- Extensible design

### 5. Algorithm Implementation

#### `fibonacci_sequence(n)`
Generates the first n numbers in the Fibonacci sequence.

**Parameters:**
- `n` (int): Number of Fibonacci numbers to generate

**Returns:**
- `list`: List of Fibonacci numbers

**Features:**
- Input validation
- Efficient iterative algorithm
- Handles edge cases (n=0, n=1)

## Key Concepts Demonstrated

### Function Documentation
Every function includes:
- Clear docstrings explaining purpose
- Parameter descriptions with types
- Return value documentation
- Example usage when helpful

### Error Handling
Functions validate inputs and raise appropriate exceptions:
- `ValueError` for invalid numeric inputs
- Clear error messages describing the problem
- Defensive programming practices

### Default Parameters
Functions use default values to:
- Make functions easier to call
- Provide sensible defaults
- Maintain backward compatibility

### Variable Arguments
- `*args` allows functions to accept any number of positional arguments
- `**kwargs` allows functions to accept any number of keyword arguments
- Provides flexibility in function design

### Mathematical Operations
- Import and use the `math` module for constants like π
- Implement mathematical formulas accurately
- Handle floating-point precision considerations

## Running the Code

To run the main script:
```bash
python main.py
```

To run the tests:
```bash
pytest tests.py -v
```

## Testing Coverage

The test suite includes:
- **Normal operation tests**: Verify functions work with typical inputs
- **Edge case tests**: Test boundary conditions (zero values, minimal inputs)
- **Error handling tests**: Ensure proper exceptions are raised
- **Parameter variation tests**: Test different parameter combinations

## Next Steps

After completing this mission, you'll be ready for:
- Object-oriented programming with classes
- More complex algorithm implementations
- Module organization and imports
- Advanced Python features like decorators

## Common Patterns

This mission demonstrates several important Python patterns:
1. **Input validation**: Always check parameters before processing
2. **Default parameters**: Provide sensible defaults for optional parameters
3. **Flexible interfaces**: Use *args and **kwargs for adaptable functions
4. **Clear documentation**: Write docstrings for all public functions
5. **Error handling**: Raise exceptions for invalid inputs with clear messages

Practice these patterns in your own code to write more robust and maintainable Python programs!
