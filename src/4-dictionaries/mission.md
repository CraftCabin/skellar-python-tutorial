# Mission 4: Dictionaries

## Learning Objectives
- Master dictionary creation and manipulation
- Learn to work with nested data structures
- Understand key-value pair relationships
- Practice data analysis and aggregation
- Implement real-world data management scenarios

## Concepts Covered
- Dictionary creation and access
- Nested dictionaries and complex data structures
- Dictionary methods and operations
- Data aggregation and analysis
- Searching and filtering dictionary data
- Grade classification and statistics

## Mission Description
Dictionaries are Python's key-value data structure, perfect for organizing related information. In this mission, you'll build a student management system that demonstrates real-world dictionary usage for data storage, retrieval, and analysis.

## What You'll Build
A complete student management system with:
1. `create_student_record()` - Build individual student profiles
2. `update_grades()` - Modify existing records
3. `create_class_roster()` - Manage multiple students
4. `find_top_student()` - Search and analyze data
5. `count_by_grade_range()` - Aggregate and classify data

## Key Code Concepts

### Dictionary Creation
```python
student = {
    'name': name,
    'age': age,
    'grades': grades,
    'average': round(average, 2)
}
```

### Dictionary Access and Modification
```python
student['grades'].append(new_grade)          # Modify nested list
student['average'] = calculate_new_average() # Update value
```

### Iterating Through Dictionaries
```python
for student_id, student in roster.items():
    # Access both key and value
    print(f"Student {student_id}: {student['name']}")
```

### Dictionary Comprehension Alternative
```python
# Finding maximum value
highest_average = -1
top_student_id = None
for student_id, student in roster.items():
    if student['average'] > highest_average:
        highest_average = student['average']
        top_student_id = student_id
```

## Tasks to Complete
1. ✅ Create structured student records with calculated averages
2. ✅ Update existing records and recalculate derived values
3. ✅ Build and manage collections of related records
4. ✅ Search data to find optimal records
5. ✅ Classify and count data by ranges

## Data Structure Design

### Student Record Structure
```python
{
    'name': str,        # Student's full name
    'age': int,         # Student's age
    'grades': [float],  # List of individual grades
    'average': float    # Calculated average (rounded to 2 decimals)
}
```

### Class Roster Structure
```python
{
    'student_id': student_record,
    'student_id': student_record,
    ...
}
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
Student: {'name': 'John', 'age': 20, 'grades': [85, 90, 88], 'average': 87.67}
Updated student: {'name': 'John', 'age': 20, 'grades': [85, 90, 88, 92], 'average': 88.75}
Roster: {'001': {...}, '002': {...}, '003': {...}}
Top student: 003 - {'name': 'Charlie', 'age': 21, 'grades': [92, 89, 95, 93], 'average': 92.25}
Grade distribution: {'A (90-100)': 1, 'B (80-89)': 2, 'C (70-79)': 0, 'D (60-69)': 0, 'F (0-59)': 0}
```

## Test Requirements
Your code must pass these tests:
- Create properly structured student records with correct averages
- Handle empty grade lists (average should be 0)
- Update grades and recalculate averages correctly
- Find the student with the highest average
- Count students in correct grade ranges
- Handle edge cases like empty rosters

## Common Mistakes to Avoid
- ❌ Forgetting to recalculate averages after adding grades
- ❌ Not handling division by zero for empty grade lists
- ❌ Incorrect grade range boundaries (90+ is A, 80-89 is B, etc.)
- ❌ Modifying original data when returning copies

## Real-World Applications
This pattern is used in:
- Student information systems
- Employee management databases
- Customer relationship management (CRM)
- Inventory tracking systems
- Any scenario requiring structured data with relationships

## Performance Considerations
- Dictionary lookups are O(1) average case
- Iterating through all values is O(n)
- Consider using `collections.defaultdict` for automatic initialization
- For large datasets, consider database solutions

## Next Steps
Mission 5 will teach you advanced function concepts including parameters, error handling, and modular design!
