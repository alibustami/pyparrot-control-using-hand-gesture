import cv2

from FingersCounter import FingersCounter

video = cv2.VideoCapture(0)
counter = FingersCounter(max_num_hands=2)

while True:
    ret, frame = video.read()
    if not ret:
        break
    fingers_counter, return_frame, score = counter.count_from_frame(frame)
    print(fingers_counter)
    cv2.imshow("Drone Controller", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
