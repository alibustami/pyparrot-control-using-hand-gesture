import sys

import cv2

from configs import load
from FingersCounter import FingersCounter

# project_name: str = load(key='project name')
# print(project_name)


counter = FingersCounter()

# image = cv2.imread("tests/fixtures/hand_1_up.jpeg")
# images = [f"tests/fixtures/hand_{i}_up.jpeg" for i in range(6)]
# for image in images:
#     image = cv2.imread(image)
#     counted_fingers, image = counter.count_from_frame(image)
#     print("*"*10)
# print(counted_fingers)

# while True:
#     cv2.imshow("image", image)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# cv2.destroyAllWindows()
# # while True:
# #     cv2.imshow("image", image)
# #     if cv2.waitKey(1) & 0xFF == ord('q'):
# #         break
# # cv2.destroyAllWindows()
video = cv2.VideoCapture(0)
while True:
    _, image = video.read()
    try:
        # image = cv2.resize(image, (640, 480))
        counted_fingers, image = counter.count_from_frame(image)
    except TypeError:
        print("No hand detected")
        continue
    # print(counted_fingers)
    cv2.imshow("image", image)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
