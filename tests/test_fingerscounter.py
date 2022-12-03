"""Unit testing for the fingerscounter module."""
import unittest
from unittest.mock import patch

from src.FingersCounter import FingersCounter


class TestFingersCounter(unittest.TestCase):
    """Unit testing for the FingersCounter class."""

    @patch(
        "src.FingersCounter.FingersCounter.count_from_image", return_value=0
    )
    def test_count_0(self, mock_count):
        """Tests the count method."""
        fingers_counter = FingersCounter()
        image_path: str = "tests/fixtures/hand_0_up.jpeg"
        self.assertEqual(fingers_counter.count_from_image(image_path), 0)

    @patch(
        "src.FingersCounter.FingersCounter.count_from_image", return_value=1
    )
    def test_count_1(self, mock_count):
        """Tests the count method."""
        fingers_counter = FingersCounter()
        image_path: str = "tests/fixtures/hand_1_up.jpeg"
        self.assertEqual(fingers_counter.count_from_image(image_path), 1)

    @patch(
        "src.FingersCounter.FingersCounter.count_from_image", return_value=2
    )
    def test_count_2(self, mock_count):
        """Tests the count method."""
        fingers_counter = FingersCounter()
        image_path: str = "tests/fixtures/hand_2_up.jpeg"
        self.assertEqual(fingers_counter.count_from_image(image_path), 2)

    @patch(
        "src.FingersCounter.FingersCounter.count_from_image", return_value=3
    )
    def test_count_3(self, mock_count):
        """Tests the count method."""
        fingers_counter = FingersCounter()
        image_path: str = "tests/fixtures/hand_3_up.jpeg"
        self.assertEqual(fingers_counter.count_from_image(image_path), 3)

    @patch(
        "src.FingersCounter.FingersCounter.count_from_image", return_value=4
    )
    def test_count_4(self, mock_count):
        """Tests the count method."""
        fingers_counter = FingersCounter()
        image_path: str = "tests/fixtures/hand_4_up.jpeg"
        self.assertEqual(fingers_counter.count_from_image(image_path), 4)

    @patch(
        "src.FingersCounter.FingersCounter.count_from_image", return_value=5
    )
    def test_count_5(self, mock_count):
        """Tests the count method."""
        fingers_counter = FingersCounter()
        image_path: str = "tests/fixtures/hand_5_up.jpeg"
        self.assertEqual(fingers_counter.count_from_image(image_path), 5)
