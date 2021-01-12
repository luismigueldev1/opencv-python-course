import cv2 as cv
import numpy as np
import os

haar_cascade = cv.CascadeClassifier("data/haar_face.xml")

# features = np.load("features.npy", allow_pickle=True)
# labels = np.load("labels.npy")

# people
DIR = r'C:\Users\lrodve\Documents\Projects\opencv-course-freecodecamp\opencv-python\Faces\train'
people = []
for i in os.listdir(DIR):
    people.append(i)

print(people)
# load model
faces_recognizer = cv.face.LBPHFaceRecognizer_create()
faces_recognizer.read("face_trained.yml")

URL = r'C:\Users\lrodve\Documents\Projects\opencv-course-freecodecamp\opencv-python\Faces\val\madonna\p2.jpg'
img = cv.imread(URL)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Detect the face in the image
faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)
for (x, y, w, h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+w]
    label, confidence = faces_recognizer.predict(faces_roi)
    print(f"label = {people[label]} with a confidence of {confidence}")

    cv.putText(img, str(people[label]), (30, 30),
               cv.FONT_HERSHEY_COMPLEX, (1.0), (0, 255, 0), thickness=2)
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)

    cv.imshow("Detected Face", img)
    cv.waitKey(0)
