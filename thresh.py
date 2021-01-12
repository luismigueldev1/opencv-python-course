import cv2 as cv

img = cv.imread("Photos/cats.jpg")
cv.imshow("Cats", img)

# BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# Simple Thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow("Simple Thresholding", thresh)

# Simple Thresholding inverse
threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow("Simple Thresholding Inverse", thresh_inv)


# Adapative Thresholding
adaptive_thesh = cv.adaptiveThreshold(
    gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow("Adapative Threshold", adaptive_thesh)

# Adapative Thresholding INVERSE
adaptive_thesh_inv = cv.adaptiveThreshold(
    gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 11, 3)
cv.imshow("Adapative Threshold INVERSE", adaptive_thesh_inv)

# Adapative Thresholding
adaptive_thesh_inv = cv.adaptiveThreshold(
    gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow("Adapative Threshold Guassian ", adaptive_thesh_inv)

cv.waitKey(0)
