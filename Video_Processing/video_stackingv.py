import cv2
import numpy as np

cap1 = cv2.VideoCapture("C:/Users/harsh/Videos/Screen Recordings/Screen Recording 2024-10-02 232552.mp4")
cap2 = cv2.VideoCapture("C:/Users/harsh/Videos/Screen Recordings/Screen Recording 2024-08-25 124145.mp4")

if not cap1.isOpened() or not cap2.isOpened():
    print("Error: Could not open video.")
    exit()

while True:
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()

    if not ret1 or not ret2:
        break

    frame1 = cv2.resize(frame1, (640, 360))
    frame2 = cv2.resize(frame2, (640, 360))

    v_concat = np.vstack((frame1, frame2))

    cv2.imshow('Concatenated Video', v_concat)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap1.release()
cap2.release()
cv2.destroyAllWindows()