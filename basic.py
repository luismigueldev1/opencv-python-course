import cv2 as cv

img = cv.imread("Photos/park.jpg")
cv.imshow("Image", img)

# Converting to grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Gray Image", gray)

# Blur
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
# cv.imshow("Blur", blur)

# Edge cascade
# cany = cv.Canny(img, 125, 175)
cany = cv.Canny(blur, 125, 175)
cv.imshow("Canny", cany)

# Dilating the image
dilated = cv.dilate(cany, (7, 7), iterations=3)
cv.imshow("Dilated", dilated)

# Eroding
eroded = cv.erode(dilated, (7, 7), iterations=3)
cv.imshow("Eroded", eroded)

# Resize
resize = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow("Resized", resize)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow("Cropped", cropped)

cv.waitKey(0)
