import pytest
from main import (
    create_student_record, 
    update_grades, 
    create_class_roster, 
    find_top_student, 
    count_by_grade_range
)


def test_create_student_record():
    """Test creating a student record."""
    result = create_student_record("John", 20, [85, 90, 88])
    
    assert result['name'] == "John"
    assert result['age'] == 20
    assert result['grades'] == [85, 90, 88]
    assert result['average'] == 87.67


def test_create_student_record_empty_grades():
    """Test creating a student record with no grades."""
    result = create_student_record("Jane", 19, [])
    
    assert result['name'] == "Jane"
    assert result['age'] == 19
    assert result['grades'] == []
    assert result['average'] == 0


def test_update_grades():
    """Test updating a student's grades."""
    student = create_student_record("Alice", 20, [80, 85])
    updated = update_grades(student, 90)
    
    assert len(updated['grades']) == 3
    assert 90 in updated['grades']
    assert updated['average'] == 85.0


def test_create_class_roster():
    """Test creating a class roster."""
    roster = create_class_roster()
    
    assert isinstance(roster, dict)
    assert len(roster) >= 3
    assert '001' in roster
    assert '002' in roster
    assert '003' in roster
    
    # Check that each entry is a valid student record
    for student_id, student in roster.items():
        assert 'name' in student
        assert 'age' in student
        assert 'grades' in student
        assert 'average' in student


def test_find_top_student():
    """Test finding the top student."""
    roster = create_class_roster()
    top_id, top_student = find_top_student(roster)
    
    assert top_id is not None
    assert top_student is not None
    assert 'average' in top_student
    
    # Verify this is actually the highest average
    for student in roster.values():
        assert student['average'] <= top_student['average']


def test_find_top_student_empty_roster():
    """Test finding top student in empty roster."""
    top_id, top_student = find_top_student({})
    
    assert top_id is None
    assert top_student is None


def test_count_by_grade_range():
    """Test counting students by grade range."""
    roster = create_class_roster()
    counts = count_by_grade_range(roster)
    
    expected_keys = ['A (90-100)', 'B (80-89)', 'C (70-79)', 'D (60-69)', 'F (0-59)']
    for key in expected_keys:
        assert key in counts
        assert isinstance(counts[key], int)
        assert counts[key] >= 0
    
    # Total count should equal roster size
    total_count = sum(counts.values())
    assert total_count == len(roster)


def test_count_by_grade_range_empty():
    """Test counting grades with empty roster."""
    counts = count_by_grade_range({})
    
    for count in counts.values():
        assert count == 0
