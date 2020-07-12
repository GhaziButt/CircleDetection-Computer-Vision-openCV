import numpy as np
import cv2 as cv
img = cv.imread('molly.jpg')
output = img.copy()
gray = cv.cvtColor(output, cv.COLOR_BGR2GRAY)
eo = cv.Canny(gray, 50, 150, apertureSize=3)
cv.imshow('edges', eo)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray = cv.medianBlur(gray, 5)
circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, 50, param1=150, param2=30, minRadius=0, maxRadius=0)
detected_circles = np.uint16(np.around(circles))
for (x, y ,r) in detected_circles[0, :]:
    cv.circle(output, (x, y), r, (0, 0, 0), 2)
    cv.circle(output, (x, y), 2, (255, 255, 255), 2)


cv.imshow('output',output)
cv.waitKey(0)
cv.destroyAllWindows()

