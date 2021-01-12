import os
import cv2 as cv
import numpy as np

DIR = r'C:\Users\lrodve\Documents\Projects\opencv-course-freecodecamp\opencv-python\Faces\train'
haar_cascade = cv.CascadeClassifier("data/haar_face.xml")

# get all directories and append to array
people = []
for i in os.listdir(DIR):
    people.append(i)

features = []
labels = []


def created_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(
                gray, scaleFactor=1.1, minNeighbors=4)

            for (x, y, w, h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)


created_train()
print("Training done -------------------")

# Covert array to np.array
features = np.array(features, dtype="object")
labels = np.array(labels)

faces_recognizer = cv.face.LBPHFaceRecognizer_create()

# Train the recognizer on the features list and the label list
faces_recognizer.train(features, labels)

# Saving training
faces_recognizer.save("face_trained.yml")
np.save("features.npy", features)
np.save("labels.npy", labels)
