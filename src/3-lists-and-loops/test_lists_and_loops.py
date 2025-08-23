import pytest
import sys
import os
sys.path.append(os.path.dirname(__file__))
from main import create_number_list, sum_list, find_even_numbers, create_shopping_list


def test_create_number_list():
    """Test creating a number list."""
    result = create_number_list(1, 5)
    expected = [1, 2, 3, 4, 5]
    assert result == expected


def test_create_number_list_single():
    """Test creating a number list with single number."""
    result = create_number_list(5, 5)
    expected = [5]
    assert result == expected


def test_sum_list():
    """Test summing a list of numbers."""
    numbers = [1, 2, 3, 4, 5]
    result = sum_list(numbers)
    assert result == 15


def test_sum_list_empty():
    """Test summing an empty list."""
    result = sum_list([])
    assert result == 0


def test_find_even_numbers():
    """Test finding even numbers in a list."""
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    result = find_even_numbers(numbers)
    expected = [2, 4, 6, 8]
    assert result == expected


def test_find_even_numbers_none():
    """Test finding even numbers when there are none."""
    numbers = [1, 3, 5, 7]
    result = find_even_numbers(numbers)
    assert result == []


def test_create_shopping_list():
    """Test creating and manipulating shopping list."""
    result = create_shopping_list()
    
    assert isinstance(result, list)
    assert len(result) >= 5
    assert "tomatoes" in result
    assert "bananas" in result
    assert result[0] == "tomatoes"  # Should be inserted at beginning


def test_shopping_list_content():
    """Test that shopping list contains expected items."""
    result = create_shopping_list()
    
    expected_items = ["apples", "bread", "milk", "eggs", "cheese", "bananas", "tomatoes"]
    for item in expected_items:
        assert item in result
