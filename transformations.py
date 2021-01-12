import cv2 as cv
import numpy as np

img = cv.imread("Photos/park.jpg")
cv.imshow("Park", img)

# Translate


def translate(img, x, y):
    # -x --> left
    # -y --> up
    # x --> right
    # y --> down
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)


# show a image translate
translated = translate(img, 100, -100)
#cv.imshow("TranslateImage", translated)


# Rotate

def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)


# show a image rotate
rotated = rotate(img, 45)
#cv.imshow("Rotated", rotated)

rotated_rotated = rotate(img, -180)
#cv.imshow("Rotated Rotated", rotated_rotated)


# Resizing
resize = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
#cv.imshow("Resize", resize)

# Flipping
flip = cv.flip(img, 1)
#cv.imshow("Flip", flip)

# Cropping
cropped = img[200:400, 300:400]
cv.imshow("Cropped", cropped)
cv.waitKey(0)
