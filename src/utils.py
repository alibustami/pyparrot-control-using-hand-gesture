"""Utility functions for the project."""
from typing import Callable, List

from pyparrot import Bebop

from configs import load


def takeoff() -> List[Callable, int]:
    """Takeoff the drone to a given height.

    Returns
    -------
    List[Callable, int]
        A list of the drone and the height.
    """
    # initialize the drone
    bebop = Bebop()

    # connect to the drone
    bebop.connect(10)

    # for indoor safety
    bebop.set_max_tilt(5)  # 5 degrees
    bebop.set_max_vertical_speed(1)  # 1 m/s
    bebop.set_hull_protection(1)  # 1 = on, 0 = off

    # take off
    height: int = load(key="takeoff altitude")
    bebop.safe_takeoff(height)

    return [bebop, height]
