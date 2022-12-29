"""This module contains the FingersCounter class."""
import time
from typing import Any, List, Union

import cv2
import mediapipe as mp
import numpy as np

from src.configs import load


class FingersCounter:
    """
    This class is responsible for counting the fingers in a given image.

    Attributes
    ----------
    max_num_hands : int
        The maximum number of hands to detect.

    Methods
    -------
    count_from_frame(image: np.array)
        Counts the fingers in a given image.
    """

    def __init__(self, max_num_hands: int = 2,) -> List[Union[int, np.array]]:
        """
        Constructs all the necessary attributes for the FingersCounter object.

        Parameters
        ----------
        max_num_hands : int
            The maximum number of hands to detect.

        Returns
        -------
        List[Union[int, np.array]]
            The number of fingers and the image with the hand annotations.
        """
        min_detection_confidence = load(key="min detection confidence")
        min_tracking_confidence = load(key="min tracking confidence")
        self.mp_drawing = mp.solutions.drawing_utils
        # self.mp_hands = mp.solutions.hands
        self.min_detection_confidence = min_detection_confidence
        self.min_tracking_confidence = min_tracking_confidence
        self.max_num_hands = max_num_hands

    def count_from_frame(
        self, image: np.array
    ) -> List[Union[int, np.array, float]]:
        """
        Counts the fingers in a given image.

        Parameters
        ----------
        image : np.array
            The image to count the fingers in.

        Returns
        -------
        List[Union[int, np.array, float]]
            The number of fingers, the image with the hand annotations and the time it took to count the fingers.
        """
        score: float = 0.0
        start_time = time.time()
        with mp.solutions.hands.Hands(
            min_detection_confidence=self.min_detection_confidence,
            min_tracking_confidence=self.min_tracking_confidence,
            max_num_hands=self.max_num_hands,
        ) as hands:
            # for better performance, optionally mark the image as not writeable to pass by reference
            image.flags.writeable = False
            converted_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = hands.process(converted_image)

            # Draw the hand annotations on the image
            image.flags.writeable = True
            # image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            # initialize set counter to 0 for each captured frame
            fingers_counter: int = 0

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    hand_index = results.multi_hand_landmarks.index(
                        hand_landmarks
                    )
                    hand_label = (
                        results.multi_handedness[hand_index]
                        .classification[0]
                        .label
                    )
                    score = (
                        results.multi_handedness[hand_index]
                        .classification[0]
                        .score
                    )

                    # set variable to keep landmarks potitions (x, y)
                    hand_landmarks_list: list = []

                    # fill the with x and y coordinates of the each landmarks
                    for landmarks in hand_landmarks.landmark:
                        hand_landmarks_list.append((landmarks.x, landmarks.y))

                    # get the hand bounding box
                    height, width, _ = image.shape
                    x_min: int = int(hand_landmarks_list[4][0] * width)
                    y_min: int = int(hand_landmarks_list[12][1] * height)
                    x_max: int = int(hand_landmarks_list[20][0] * width)
                    y_max: int = int(hand_landmarks_list[0][1] * height)

                    # test conditions to count fingers
                    if (
                        hand_label == "Left"
                        and hand_landmarks_list[4][0]
                        > hand_landmarks_list[3][0]
                    ):
                        fingers_counter += 1
                    elif (
                        hand_label == "Right"
                        and hand_landmarks_list[4][0]
                        < hand_landmarks_list[3][0]
                    ):
                        fingers_counter += 1

                    # the y coordinates of the finger tip must be lower than the pip y coordinate

                    if (
                        hand_landmarks_list[8][1] < hand_landmarks_list[6][1]
                    ):  # index
                        fingers_counter += 1
                    if (
                        hand_landmarks_list[12][1] < hand_landmarks_list[10][1]
                    ):  # middle
                        fingers_counter += 1
                    if (
                        hand_landmarks_list[16][1] < hand_landmarks_list[14][1]
                    ):  # ring
                        fingers_counter += 1
                    if (
                        hand_landmarks_list[20][1] < hand_landmarks_list[18][1]
                    ):  # pinky
                        fingers_counter += 1
                self.mp_drawing.draw_landmarks(
                    image, hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS
                )
                cv2.putText(
                    img=image,
                    text=str(fingers_counter),
                    org=(10, 50),
                    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=1,
                    color=(0, 0, 255),  # red
                    thickness=2,
                    lineType=cv2.LINE_AA,
                )
                cv2.putText(
                    img=image,
                    text=str(score),
                    org=(10, 100),
                    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=1,
                    color=(0, 0, 255),  # red
                    thickness=2,
                    lineType=cv2.LINE_AA,
                )
                cv2.rectangle(
                    img=image,
                    pt1=(x_min, y_min),
                    pt2=(x_max, y_max),
                    color=(255, 255, 0),  # yellow
                    thickness=2,
                )
        end_time = time.time()
        fps = 1 / (end_time - start_time)
        print(fps)
        # print(end_time - start_time)
        return [fingers_counter, image, score]
