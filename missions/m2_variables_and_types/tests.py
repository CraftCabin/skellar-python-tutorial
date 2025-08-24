import pytest
import sys
import os
sys.path.append(os.path.dirname(__file__))
from .main import add_numbers, concat_numbers_as_string


def test_add_numbers():
    """Test that add_numbers correctly adds two integers."""
    # Test basic addition
    result = add_numbers(5, 10)
    assert result == 15
    assert isinstance(result, int)
    
    # Test with different numbers
    result = add_numbers(3, 7)
    assert result == 10
    assert isinstance(result, int)
    
    # Test with zero
    result = add_numbers(0, 5)
    assert result == 5
    assert isinstance(result, int)
    
    # Test with negative numbers
    result = add_numbers(-5, 10)
    assert result == 5
    assert isinstance(result, int)


def test_add_numbers_negative():
    """Test add_numbers with negative numbers."""
    result = add_numbers(-3, -7)
    assert result == -10
    assert isinstance(result, int)


def test_concat_numbers_as_string():
    """Test that concat_numbers_as_string correctly concatenates numbers as strings."""
    # Test basic concatenation
    result = concat_numbers_as_string(5, 10)
    assert result == "510"
    assert isinstance(result, str)
    
    # Test with different numbers
    result = concat_numbers_as_string(1, 2)
    assert result == "12"
    assert isinstance(result, str)
    
    # Test with zero
    result = concat_numbers_as_string(0, 5)
    assert result == "05"
    assert isinstance(result, str)
    
    # Test with larger numbers
    result = concat_numbers_as_string(123, 456)
    assert result == "123456"
    assert isinstance(result, str)


def test_concat_numbers_with_negative():
    """Test concat_numbers_as_string with negative numbers."""
    result = concat_numbers_as_string(-5, 10)
    assert result == "-510"
    assert isinstance(result, str)
    
    result = concat_numbers_as_string(5, -10)
    assert result == "5-10"
    assert isinstance(result, str)