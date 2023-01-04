"""This is the main file of the project. It is used to control the drone with hand gestures."""
import cv2

from configs import load
from FingersCounter import FingersCounter
from utils import takeoff


def main():
    """
    The main function of the project.

    Raises
    ------
    Exception
        If the frame is not read correctly.
    """
    # takeoff the drone and initialize the fingers counter
    bepop, height = takeoff()
    counter = FingersCounter(max_num_hands=2)

    # initialize the video capture
    video = cv2.VideoCapture(0)

    # initialize the fingers counter
    fingers_counter: int = 0

    # initialize the drone controller
    duration: float = load(key="duration")

    while True:
        # Capture frame-by-frame
        ret, frame = video.read()

        # if the frame is not read correctly, break the loop
        if not ret:
            raise Exception("Could not read frame")
            break

        # count the fingers
        fingers_counter, return_frame = counter.count_from_frame(frame)

        # control the drone
        if fingers_counter == 0:  # land
            bepop.safe_land(height)
        elif fingers_counter == 1:  # hover in place
            bepop.fly_direct(
                roll=0, pitch=0, yaw=0, vertical_movement=0, duration=duration
            )
        elif fingers_counter == 2:  # pitch forward
            bepop.fly_direct(
                roll=0, pitch=1, yaw=0, vertical_movement=0, duration=duration
            )
        elif fingers_counter == 3:  # pitch backward
            bepop.fly_direct(
                roll=0, pitch=-1, yaw=0, vertical_movement=0, duration=duration
            )
        elif fingers_counter == 4:  # roll right
            bepop.fly_direct(
                roll=1, pitch=0, yaw=0, vertical_movement=0, duration=duration
            )
        elif fingers_counter == 5:  # roll left
            bepop.fly_direct(
                roll=-1, pitch=0, yaw=0, vertical_movement=0, duration=duration
            )
        elif fingers_counter == 6:  # yaw right
            bepop.fly_direct(
                roll=0, pitch=0, yaw=1, vertical_movement=0, duration=duration
            )
        elif fingers_counter == 7:  # yaw left
            bepop.fly_direct(
                roll=0, pitch=0, yaw=-1, vertical_movement=0, duration=duration
            )
        elif fingers_counter == 8:  # go up
            bepop.fly_direct(
                roll=0, pitch=0, yaw=0, vertical_movement=1, duration=duration
            )
        elif fingers_counter == 9:  # go down
            bepop.fly_direct(
                roll=0, pitch=0, yaw=0, vertical_movement=-1, duration=duration
            )

        # Display the resulting frame
        cv2.imshow("Drone Controller", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # When everything done, release the capture
    video.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
