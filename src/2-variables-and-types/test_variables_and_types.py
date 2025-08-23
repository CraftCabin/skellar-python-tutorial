import pytest
import sys
import os
sys.path.append(os.path.dirname(__file__))
from main import create_variables, calculate_info


def test_create_variables():
    """Test that create_variables returns the correct types and structure."""
    result = create_variables()
    
    assert isinstance(result, dict)
    assert 'name' in result
    assert 'age' in result
    assert 'height' in result
    assert 'is_student' in result
    
    assert isinstance(result['name'], str)
    assert isinstance(result['age'], int)
    assert isinstance(result['height'], float)
    assert isinstance(result['is_student'], bool)


def test_calculate_info():
    """Test that calculate_info returns correct formatted string."""
    result = calculate_info("John", 2000)
    expected = "Hello John, you are 25 years old!"
    assert result == expected


def test_calculate_info_different_year():
    """Test calculate_info with a different birth year."""
    result = calculate_info("Jane", 1990)
    expected = "Hello Jane, you are 35 years old!"
    assert result == expected


def test_variable_types():
    """Test that variables have the expected types."""
    variables = create_variables()
    
    # Test specific type requirements
    assert len(variables['name']) > 0  # Name should not be empty
    assert variables['age'] >= 0  # Age should be non-negative
    assert variables['height'] > 0  # Height should be positive
