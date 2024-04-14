import cv2 as cv
import sys

cap = cv.VideoCapture(0)

if not cap.isOpened():
    sys.exit('카메라 연결 실패')

global gray_flag
gray_flag = False
while True:
    ret, frame = cap.read()

    if not ret:
        print('프레임 획득에 실패하여 루프를 나갑니다')
        break

    if gray_flag:
        frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    cv.imshow('Video display', frame)

    key = cv.waitKey(1)
    if key == ord('g'):
        gray_flag = True
    elif key == ord('c'):
        gray_flag = False
    elif key == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
