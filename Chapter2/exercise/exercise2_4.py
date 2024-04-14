import cv2 as cv
import sys

img = cv.imread('hockey.jpg')

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')

img_0 = cv.resize(img, dsize=(0, 0), fx=0.1, fy=0.1)
img_1 = cv.resize(img, dsize=(0, 0), fx=0.2, fy=0.2)
img_2 = cv.resize(img, dsize=(0, 0), fx=0.3, fy=0.3)
img_3 = cv.resize(img, dsize=(0, 0), fx=0.4, fy=0.4)
img_4 = cv.resize(img, dsize=(0, 0), fx=0.5, fy=0.5)
img_5 = cv.resize(img, dsize=(0, 0), fx=0.6, fy=0.6)
img_6 = cv.resize(img, dsize=(0, 0), fx=0.7, fy=0.7)
img_7 = cv.resize(img, dsize=(0, 0), fx=0.8, fy=0.8)
img_8 = cv.resize(img, dsize=(0, 0), fx=0.9, fy=0.9)
img_9 = cv.resize(img, dsize=(0, 0), fx=1, fy=1)

cv.imshow('img x 0.1', img_0)
cv.imshow('img x 0.2', img_1)
cv.imshow('img x 0.3', img_2)
cv.imshow('img x 0.4', img_3)
cv.imshow('img x 0.5', img_4)
cv.imshow('img x 0.6', img_5)
cv.imshow('img x 0.7', img_6)
cv.imshow('img x 0.8', img_7)
cv.imshow('img x 0.9', img_8)
cv.imshow('img x 1.0', img_9)

key = cv.waitKey()
if key == ord('q'):
    cv.destroyAllWindows()
