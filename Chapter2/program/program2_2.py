import cv2 as cv
import sys

img = cv.imread('soccer.jpg')

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')

cv.imshow('Image Display', img)
print(type(img))
print(img.shape)

cv.waitKey()
cv.destroyAllWindows()
