import pytest
import math
import sys
import os
sys.path.append(os.path.dirname(__file__))
from .main import (
    calculate_circle_area,
    calculate_rectangle_area,
    greet_user,
    calculate_total_cost,
    create_user_profile,
    fibonacci_sequence
)


def test_calculate_circle_area():
    """Test circle area calculation."""
    result = calculate_circle_area(5)
    expected = math.pi * 25
    assert abs(result - expected) < 0.001


def test_calculate_circle_area_zero():
    """Test circle area with radius 0."""
    result = calculate_circle_area(0)
    assert result == 0


def test_calculate_circle_area_negative():
    """Test circle area with negative radius raises error."""
    with pytest.raises(ValueError):
        calculate_circle_area(-5)


def test_calculate_rectangle_area():
    """Test rectangle area calculation."""
    result = calculate_rectangle_area(4, 6)
    assert result == 24


def test_calculate_rectangle_area_negative():
    """Test rectangle area with negative dimensions raises error."""
    with pytest.raises(ValueError):
        calculate_rectangle_area(-4, 6)
    
    with pytest.raises(ValueError):
        calculate_rectangle_area(4, -6)


def test_greet_user_default():
    """Test greeting with default parameters."""
    result = greet_user("Alice")
    assert result == "Hello, Alice!"


def test_greet_user_custom():
    """Test greeting with custom parameters."""
    result = greet_user("Bob", "Hi", ".")
    assert result == "Hi, Bob."


def test_calculate_total_cost():
    """Test total cost calculation."""
    result = calculate_total_cost(10.00, 20.00, 30.00)
    expected = 60.00 * 1.08  # Default 8% tax
    assert abs(result - expected) < 0.01


def test_calculate_total_cost_custom_tax():
    """Test total cost with custom tax rate."""
    result = calculate_total_cost(100.00, tax_rate=0.10)
    expected = 110.00
    assert result == expected


def test_calculate_total_cost_no_items():
    """Test total cost with no items."""
    result = calculate_total_cost()
    assert result == 0.0


def test_create_user_profile_minimal():
    """Test creating user profile with minimal data."""
    result = create_user_profile(name="John")
    
    assert result['name'] == "John"
    assert result['age'] == 0
    assert result['email'] == 'no-email@example.com'
    assert result['location'] == 'Unknown'
    assert result['occupation'] == 'Student'


def test_create_user_profile_complete():
    """Test creating user profile with complete data."""
    result = create_user_profile(
        name="Jane",
        age=30,
        email="jane@example.com",
        location="New York",
        occupation="Engineer",
        hobby="reading"
    )
    
    assert result['name'] == "Jane"
    assert result['age'] == 30
    assert result['email'] == "jane@example.com"
    assert result['location'] == "New York"
    assert result['occupation'] == "Engineer"
    assert result['hobby'] == "reading"


def test_create_user_profile_empty():
    """Test creating user profile with no data."""
    result = create_user_profile()
    
    assert result['name'] == 'Unknown'
    assert result['age'] == 0
    assert result['email'] == 'no-email@example.com'


def test_fibonacci_sequence():
    """Test Fibonacci sequence generation."""
    result = fibonacci_sequence(8)
    expected = [0, 1, 1, 2, 3, 5, 8, 13]
    assert result == expected


def test_fibonacci_sequence_edge_cases():
    """Test Fibonacci sequence edge cases."""
    assert fibonacci_sequence(0) == []
    assert fibonacci_sequence(1) == [0]
    assert fibonacci_sequence(2) == [0, 1]


def test_fibonacci_sequence_negative():
    """Test Fibonacci sequence with negative input raises error."""
    with pytest.raises(ValueError):
        fibonacci_sequence(-1)
