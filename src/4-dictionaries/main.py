def create_student_record(name, age, grades):
    """
    Create a student record dictionary.
    
    Args:
        name (str): Student's name
        age (int): Student's age
        grades (list): List of grades
        
    Returns:
        dict: Student record with name, age, grades, and average
    """
    average = sum(grades) / len(grades) if grades else 0
    
    return {
        'name': name,
        'age': age,
        'grades': grades,
        'average': round(average, 2)
    }


def update_grades(student, new_grade):
    """
    Add a new grade to a student's record.
    
    Args:
        student (dict): Student record
        new_grade (float): New grade to add
        
    Returns:
        dict: Updated student record
    """
    student['grades'].append(new_grade)
    student['average'] = round(sum(student['grades']) / len(student['grades']), 2)
    return student


def create_class_roster():
    """
    Create a class roster with multiple students.
    
    Returns:
        dict: Dictionary where keys are student IDs and values are student records
    """
    roster = {}
    
    # Add some students
    roster['001'] = create_student_record("Alice", 20, [85, 92, 78, 95])
    roster['002'] = create_student_record("Bob", 19, [88, 84, 90, 87])
    roster['003'] = create_student_record("Charlie", 21, [92, 89, 95, 93])
    
    return roster


def find_top_student(roster):
    """
    Find the student with the highest average grade.
    
    Args:
        roster (dict): Class roster
        
    Returns:
        tuple: (student_id, student_record) of top student
    """
    if not roster:
        return None, None
    
    top_student_id = None
    highest_average = -1
    
    for student_id, student in roster.items():
        if student['average'] > highest_average:
            highest_average = student['average']
            top_student_id = student_id
    
    return top_student_id, roster[top_student_id]


def count_by_grade_range(roster):
    """
    Count students by grade ranges.
    
    Args:
        roster (dict): Class roster
        
    Returns:
        dict: Count of students in each grade range
    """
    ranges = {
        'A (90-100)': 0,
        'B (80-89)': 0,
        'C (70-79)': 0,
        'D (60-69)': 0,
        'F (0-59)': 0
    }
    
    for student in roster.values():
        average = student['average']
        if average >= 90:
            ranges['A (90-100)'] += 1
        elif average >= 80:
            ranges['B (80-89)'] += 1
        elif average >= 70:
            ranges['C (70-79)'] += 1
        elif average >= 60:
            ranges['D (60-69)'] += 1
        else:
            ranges['F (0-59)'] += 1
    
    return ranges


if __name__ == "__main__":
    # Test the functions
    student = create_student_record("John", 20, [85, 90, 88])
    print("Student:", student)
    
    updated_student = update_grades(student, 92)
    print("Updated student:", updated_student)
    
    roster = create_class_roster()
    print("Roster:", roster)
    
    top_id, top_student = find_top_student(roster)
    print(f"Top student: {top_id} - {top_student}")
    
    grade_counts = count_by_grade_range(roster)
    print("Grade distribution:", grade_counts)
