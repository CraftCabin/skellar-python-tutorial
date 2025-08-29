# Mission 3: Lists and Loops

## Learning Objectives
- Master Python list manipulation and processing
- Learn list sorting and comparison operations
- Understand tuple returns for multiple values
- Practice loops for list transformation
- Implement common list algorithms

## Concepts Covered
- List sorting algorithms
- Finding maximum and minimum values in lists
- List transformation with loops
- Tuple return types for multiple values
- List comprehension alternatives
- Edge case handling (empty lists)

## Mission Description
Lists are fundamental data structures in Python. In this mission, you'll implement three essential list processing functions that demonstrate sorting, analysis, and transformation operations commonly used in programming.

## What You'll Build
Three core functions:
1. `sort_lists()` - Sort a list of integers in ascending order
2. `find_max_and_min_in_list()` - Find both maximum and minimum values
3. `add_number_for_each_element()` - Transform list by adding value to each element

## Key Code Concepts

### List Sorting
```python
# Manual sorting or using built-in sorted()
sorted_list = sorted(original_list)
# Returns a new sorted list
```

### Finding Extremes
```python
# Finding max and min manually
max_val = max(given_list)
min_val = min(given_list)
return (max_val, min_val)  # Return as tuple
```

### List Transformation
```python
# Transform each element
result = []
for element in given_list:
    result.append(element + number)
return result
```

## Tasks to Complete
1. ✅ Implement list sorting (ascending order)
2. ✅ Find maximum and minimum values in a list
3. ✅ Return multiple values using tuples
4. ✅ Transform lists by adding values to each element
5. ✅ Handle edge cases (empty lists, single elements)

## Function Specifications

### `sort_lists(given_list: list[int]) -> list`
- **Input**: List of integers
- **Output**: New list with elements sorted in ascending order
- **Example**: `[3, 1, 4, 1, 5]` → `[1, 1, 3, 4, 5]`

### `find_max_and_min_in_list(given_list: list[int]) -> (int, int)`
- **Input**: List of integers
- **Output**: Tuple of (maximum, minimum) values
- **Example**: `[3, 1, 4, 1, 5]` → `(5, 1)`

### `add_number_for_each_element(given_list: list[int], number: int) -> list[int]`
- **Input**: List of integers and a number to add
- **Output**: New list with number added to each element
- **Example**: `[1, 2, 3], 10` → `[11, 12, 13]`

## Algorithm Patterns

### Sorting Pattern
```python
# Option 1: Use built-in sorting
return sorted(given_list)

# Option 2: Manual implementation
# (bubble sort, selection sort, etc.)
```

### Min/Max Finding Pattern
```python
if not given_list:  # Handle empty list
    return None
    
max_val = given_list[0]
min_val = given_list[0]
for element in given_list:
    if element > max_val:
        max_val = element
    if element < min_val:
        min_val = element
return (max_val, min_val)
```

### Transformation Pattern
```python
result = []
for element in given_list:
    transformed = element + number
    result.append(transformed)
return result
```

## Running Your Code
```bash
# Run the script directly
python main.py

# Run the tests
pytest tests.py -v
```

## Expected Examples
```python
# Sorting
sort_lists([3, 1, 4, 1, 5, 9, 2, 6])  # [1, 1, 2, 3, 4, 5, 6, 9]

# Finding extremes
find_max_and_min_in_list([3, 1, 4, 1, 5])  # (5, 1)

# Adding to each element
add_number_for_each_element([1, 2, 3], 10)  # [11, 12, 13]
```

## Test Requirements
Your code must pass these tests:
- Sort lists correctly in ascending order
- Find accurate maximum and minimum values
- Return tuple with (max, min) format
- Transform lists by adding numbers to each element
- Handle edge cases: empty lists, single elements, negative numbers
- Return correct data types (list, tuple) as specified

## Common Mistakes to Avoid
- ❌ Modifying the original list instead of returning a new one
- ❌ Returning wrong tuple order (should be max, min)
- ❌ Not handling empty lists properly
- ❌ Forgetting to return correct data types
- ❌ Using incorrect loop patterns for transformation

## Edge Cases to Consider
- **Empty lists**: Return appropriate empty results
- **Single element**: Max and min are the same value
- **Negative numbers**: Handle negative values correctly
- **Duplicate values**: Maintain all duplicates in sorting

## Performance Notes
- Built-in `sorted()` is highly optimized (Timsort algorithm)
- Manual sorting helps understand algorithms but is slower
- List transformation creates new lists (memory consideration)

## Next Steps
Mission 4 will introduce dictionaries for key-value data organization and more complex data structures!
