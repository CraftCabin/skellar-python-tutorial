import pytest
import sys
import os
sys.path.append(os.path.dirname(__file__))
from .main import mission


def test_hello_world(capsys):
    """Test that hello_world prints the expected greeting."""
    mission()
    captured = capsys.readouterr()
    expected_output = "Hello, World!\n"
    assert captured.out == expected_output
