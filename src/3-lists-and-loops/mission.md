# Mission 3: Lists and Loops

## Learning Objectives
- Master Python list creation and manipulation
- Learn different types of loops (for loops with range and iteration)
- Understand list methods (append, insert)
- Practice conditional logic with loops
- Implement basic algorithms (sum, filter)

## Concepts Covered
- List creation with `range()` and `list()`
- For loops and iteration
- List methods: `append()`, `insert()`
- Conditional statements (`if`, `%` modulo operator)
- List comprehension alternatives
- Algorithm implementation

## Mission Description
Lists are one of Python's most powerful data structures. In this mission, you'll learn to create, modify, and process lists using loops. You'll implement common algorithms like summing numbers and filtering data.

## What You'll Build
Four essential functions:
1. `create_number_list()` - Generate lists of numbers
2. `sum_list()` - Calculate totals using loops
3. `find_even_numbers()` - Filter data with conditions
4. `create_shopping_list()` - Manipulate lists with methods

## Key Code Concepts

### Creating Lists with Range
```python
# Create list from 1 to 5
numbers = list(range(1, 6))  # [1, 2, 3, 4, 5]
```

### For Loop Iteration
```python
total = 0
for number in numbers:
    total += number
```

### Conditional Filtering
```python
if number % 2 == 0:  # Check if even
    even_numbers.append(number)
```

### List Methods
```python
shopping_list.append("bananas")      # Add to end
shopping_list.insert(0, "tomatoes")  # Insert at beginning
```

## Tasks to Complete
1. ✅ Generate number lists using `range()`
2. ✅ Implement manual sum calculation with loops
3. ✅ Filter lists based on conditions (even numbers)
4. ✅ Manipulate lists with `append()` and `insert()`
5. ✅ Handle edge cases (empty lists)

## Algorithm Patterns

### Accumulator Pattern (Sum)
```python
total = 0                    # Initialize accumulator
for item in collection:      # Iterate through items
    total += item           # Update accumulator
return total                # Return result
```

### Filter Pattern
```python
result = []                 # Initialize result list
for item in collection:     # Iterate through items
    if condition(item):     # Check condition
        result.append(item) # Add if matches
return result              # Return filtered list
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
Numbers: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Sum: 55
Even numbers: [2, 4, 6, 8, 10]
Shopping list: ['tomatoes', 'apples', 'bread', 'milk', 'eggs', 'cheese', 'bananas']
```

## Test Requirements
Your code must pass these tests:
- Generate correct number ranges (inclusive of end)
- Calculate sums manually (don't use built-in `sum()`)
- Filter even numbers correctly using modulo operator
- Manipulate shopping lists with proper ordering
- Handle edge cases like empty lists and single numbers

## Common Mistakes to Avoid
- ❌ Using `range(1, 5)` when you want 1-5 inclusive (use `range(1, 6)`)
- ❌ Using built-in `sum()` instead of implementing your own loop
- ❌ Forgetting to initialize empty lists for results
- ❌ Modifying lists while iterating over them

## Performance Notes
- Lists are dynamic arrays - appending is usually O(1)
- Inserting at the beginning is O(n) - all elements shift
- For large datasets, consider more efficient data structures

## Next Steps
Mission 4 will introduce dictionaries for organizing related data with key-value pairs!
