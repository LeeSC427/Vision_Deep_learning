import cv2 as cv
import numpy as np
import sys

img = cv.imread('girl_laughing.jpg')

if img is None:
    sys.exit('파일을 찾을 수 없습니다')

def draw(event, x, y, flags, param):
    global ix, iy

    if event == cv.EVENT_LBUTTONDOWN:
        cv.rectangle(img, (x, y), (x+200, y+200), (255, 0, 0), 2)
    if event == cv.EVENT_MBUTTONDOWN:
        ix, iy = x, y
    elif event == cv.EVENT_MBUTTONUP:
        dist = np.sqrt(pow(ix-x, 2) + pow(iy-y, 2))
        cv.circle(img, (ix, iy), int(dist), (0, 0, 255), 2)

    cv.imshow('Drawing', img)

cv.namedWindow('Drawing')
cv.imshow('Drawing', img)

cv.setMouseCallback('Drawing', draw)

while(True):
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break
