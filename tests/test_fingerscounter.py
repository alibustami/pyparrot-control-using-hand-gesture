"""Unit testing for the fingerscounter module."""
import unittest
from unittest.mock import patch

from src.FingersCounter import FingersCounter


class TestFingersCounter(unittest.TestCase):
    """Unit testing for the FingersCounter class."""

    @patch(
        "src.FingersCounter.FingersCounter.count_from_image", return_value=5
    )
    def test_count(self, mock_count):
        """Tests the count method."""
        fingers_counter = FingersCounter()
        image_path: str = "tests/fixtures/hand_5_up.jpeg"
        self.assertEqual(fingers_counter.count_from_image(image_path), 5)
