import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("Photos/park.jpg")
#cv.imshow("Park", img)
plt.imshow(img)
plt.show()

# BGR to grayscale
#gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow("Gray Park", gray)

# BGR to HSV
#hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
#cv.imshow("HSV Park", hsv)

# BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("LAB Park", lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
#cv.imshow("RGB ", rgb)
plt.imshow(rgb)
plt.show()

# HSV to BGR
#hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
#cv.imshow("HSV -> BGR", hsv_bgr)

# LAB to BGR
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow("LAB -> BGR", lab_bgr)

cv.waitKey(0)
