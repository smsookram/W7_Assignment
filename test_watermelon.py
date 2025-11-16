import pytest
from watermelon import can_split_watermelon

def test_even_number_greater_than_2():
  """Test that an even number greater than 2 returns True."""
  assert can_split_watermelon(8) is True

def test_odd_number_returns_false():
  """ Test that any odd number returns False. """
  assert can_split_watermelon(7) is False

def test_edge_case_two_returns_false():
  """ Test that 2 returns False because its cannot be split
  into two positive integers. """
  assert can_split_watermelon(2) is False
