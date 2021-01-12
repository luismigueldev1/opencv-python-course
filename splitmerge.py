import cv2 as cv
import numpy as np

img = cv.imread("Photos/park.jpg")
cv.imshow("Park", img)

blank = np.zeros(img.shape[:2], dtype="uint8")

# spliting color channels
b, g, r = cv.split(img)


# merging blank images to color channels
blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])


# showing images
cv.imshow("Blue", blue)
cv.imshow("Green", green)
cv.imshow("Red", red)

# printing shapes
print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

# merging images
merged = cv.merge([b, g, r])
cv.imshow("Merged Image", merged)

cv.waitKey(0)
