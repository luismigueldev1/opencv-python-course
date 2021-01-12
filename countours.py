import cv2 as cv
import numpy as np

img = cv.imread("Photos/cats.jpg")
# cv.imshow("Cats", img)

# blank image with numpy
# blank = np.zeros((img.shape[0], img.shape[1]), dtype="uint8")
blank = np.zeros(img.shape, dtype="uint8")
#cv.imshow("Blank", blank)
print(img.shape)


# grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Gray Image", gray)

# blur
blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
# cv.imshow("Blur", blur)

# canny edges
canny = cv.Canny(blur, 125, 175)
cv.imshow("Canny Edges", canny)

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
#cv.imshow("Thresh", thresh)

contours, hierarchies = cv.findContours(
    canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

print(f'{len(contours)} contours found')

cv.drawContours(blank, contours, -1, (0, 0, 255), 1)
cv.imshow("Controus to blank", blank)

cv.waitKey(0)
