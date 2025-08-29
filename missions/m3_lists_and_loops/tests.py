import pytest
import sys
import os
sys.path.append(os.path.dirname(__file__))
from .main import sort_lists, find_max_and_min_in_list, add_number_for_each_element


def test_sort_lists():
    """Test sorting a list of integers."""
    # Test basic sorting
    result = sort_lists([3, 1, 4, 1, 5, 9, 2, 6])
    expected = [1, 1, 2, 3, 4, 5, 6, 9]
    assert result == expected
    assert isinstance(result, list)
    
    # Test already sorted list
    result = sort_lists([1, 2, 3, 4, 5])
    expected = [1, 2, 3, 4, 5]
    assert result == expected
    
    # Test reverse sorted list
    result = sort_lists([5, 4, 3, 2, 1])
    expected = [1, 2, 3, 4, 5]
    assert result == expected


def test_sort_lists_edge_cases():
    """Test sorting edge cases."""
    # Test single element
    result = sort_lists([42])
    assert result == [42]
    
    # Test empty list
    result = sort_lists([])
    assert result == []
    
    # Test negative numbers
    result = sort_lists([-3, -1, -5, -2])
    expected = [-5, -3, -2, -1]
    assert result == expected


def test_find_max_and_min_in_list():
    """Test finding maximum and minimum values in a list."""
    # Test basic case
    result = find_max_and_min_in_list([3, 1, 4, 1, 5, 9, 2, 6])
    assert result == (9, 1)  # (max, min)
    assert isinstance(result, tuple)
    assert len(result) == 2
    
    # Test single element
    result = find_max_and_min_in_list([42])
    assert result == (42, 42)
    
    # Test negative numbers
    result = find_max_and_min_in_list([-3, -1, -5, -2])
    assert result == (-1, -5)


def test_find_max_and_min_same_values():
    """Test max and min when all values are the same."""
    result = find_max_and_min_in_list([5, 5, 5, 5])
    assert result == (5, 5)


def test_add_number_for_each_element():
    """Test adding a number to each element in a list."""
    # Test basic addition
    result = add_number_for_each_element([1, 2, 3, 4, 5], 10)
    expected = [11, 12, 13, 14, 15]
    assert result == expected
    assert isinstance(result, list)
    
    # Test adding zero
    result = add_number_for_each_element([1, 2, 3], 0)
    expected = [1, 2, 3]
    assert result == expected
    
    # Test adding negative number
    result = add_number_for_each_element([5, 10, 15], -3)
    expected = [2, 7, 12]
    assert result == expected


def test_add_number_edge_cases():
    """Test adding number to edge case lists."""
    # Test empty list
    result = add_number_for_each_element([], 5)
    assert result == []
    
    # Test single element
    result = add_number_for_each_element([10], 5)
    assert result == [15]
    
    # Test negative numbers in list
    result = add_number_for_each_element([-1, -2, -3], 10)
    expected = [9, 8, 7]
    assert result == expected


def test_return_types():
    """Test that functions return correct types."""
    # sort_lists should return list
    result = sort_lists([3, 1, 2])
    assert isinstance(result, list)
    
    # find_max_and_min_in_list should return tuple
    result = find_max_and_min_in_list([1, 2, 3])
    assert isinstance(result, tuple)
    assert len(result) == 2
    
    # add_number_for_each_element should return list
    result = add_number_for_each_element([1, 2], 1)
    assert isinstance(result, list)
