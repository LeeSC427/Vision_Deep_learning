import cv2 as cv
import sys

img1 = cv.imread('soccer.jpg')
img2 = cv.imread('hockey.jpg')

if (img1 is None) or (img2 is None):
    sys.exit('파일을 찾을 수 없습니다.')

cv.imshow('Soccer', img1)
cv.imshow('Hockey', img2)

key = cv.waitKey()
if key == ord('q'):
    cv.destroyAllWindows()
