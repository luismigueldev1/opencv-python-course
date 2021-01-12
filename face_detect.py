import cv2 as cv

# read image
img = cv.imread("Photos/group 1.jpg")
#cv.imshow("Person", img)

# image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow("Person gray", gray)

#
haar_cascade = cv.CascadeClassifier("data/haar_face.xml")
faces_rect = haar_cascade.detectMultiScale(
    gray, scaleFactor=1.1, minNeighbors=1)

print(f'Numbe of faces found: {len(faces_rect)}')

for (x, y, w, h) in faces_rect:
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 1)
cv.imshow("Detected Faces", img)

cv.waitKey(0)
