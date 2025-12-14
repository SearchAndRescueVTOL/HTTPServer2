import pytest
from app import hello_world, main


def test_hello_world():
    """Test that hello_world returns the correct message."""
    result = hello_world()
    assert result == "Hello, World!"
    assert isinstance(result, str)


def test_main():
    """Test that main returns the correct message."""
    result = main()
    assert result == "Hello, World!"


def test_hello_world_not_empty():
    """Test that hello_world doesn't return an empty string."""
    result = hello_world()
    assert len(result) > 0
