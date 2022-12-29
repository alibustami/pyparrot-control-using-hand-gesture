"""Unit testing for the fingerscounter module."""
import os
import unittest
from unittest.mock import patch

import cv2

from src.FingersCounter import FingersCounter


class TestFingersCounter(unittest.TestCase):
    """Unit testing for the FingersCounter class."""

    def test_count_0(self):
        """Tests the count method."""
        image_path: str = os.path.join("tests", "fixtures", "hand_0_up.jpeg")
        image = cv2.imread(image_path)
        fingers_counter = FingersCounter()
        self.assertEqual(fingers_counter.count_from_frame(image)[0], 0)

    def test_count_1(self):
        """Tests the count method."""
        image_path: str = os.path.join("tests", "fixtures", "hand_1_up.jpeg")
        image = cv2.imread(image_path)
        fingers_counter = FingersCounter()
        self.assertEqual(fingers_counter.count_from_frame(image)[0], 1)

    def test_count_2(self):
        """Tests the count method."""
        image_path: str = os.path.join("tests", "fixtures", "hand_2_up.jpeg")
        image = cv2.imread(image_path)
        fingers_counter = FingersCounter()
        self.assertEqual(fingers_counter.count_from_frame(image)[0], 2)

    def test_count_3(self):
        """Tests the count method."""
        image_path: str = os.path.join("tests", "fixtures", "hand_3_up.jpeg")
        image = cv2.imread(image_path)
        fingers_counter = FingersCounter()
        self.assertEqual(fingers_counter.count_from_frame(image)[0], 3)

    def test_count_4(self):
        """Tests the count method."""
        image_path: str = os.path.join("tests", "fixtures", "hand_4_up.jpeg")
        image = cv2.imread(image_path)
        fingers_counter = FingersCounter()
        self.assertEqual(fingers_counter.count_from_frame(image)[0], 4)

    def test_count_5(self):
        """Tests the count method."""
        image_path: str = os.path.join("tests", "fixtures", "hand_5_up.jpeg")
        image = cv2.imread(image_path)
        fingers_counter = FingersCounter()
        self.assertEqual(fingers_counter.count_from_frame(image)[0], 4)
