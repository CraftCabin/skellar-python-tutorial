import pytest
from main import hello_world


def test_hello_world():
    """Test that hello_world returns the expected greeting."""
    expected_output = "Hello, World!"
    assert hello_world() == expected_output


def test_hello_world_type():
    """Test that hello_world returns a string."""
    result = hello_world()
    assert isinstance(result, str)


def test_hello_world_not_empty():
    """Test that hello_world doesn't return an empty string."""
    result = hello_world()
    assert len(result) > 0
