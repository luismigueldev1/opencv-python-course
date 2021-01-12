import cv2 as cv


def rescaleFrame(frame, scale=0.75):
    # Images, Videos and live video
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def changeRes(width, height):
    # live video
    capture.set(3, width)
    capture.set(4, height)


# Reading Images
img = cv.imread("Photos/cat_large.jpg")
cv.imshow("Cat", rescaleFrame(img, 0.2))
cv.waitKey(0)


# Reading Videos
capture = cv.VideoCapture("Videos/dog.mp4")

while True:
    isTrue, frame = capture.read()
    frame_resize = rescaleFrame(frame, 0.2)

    # show videos
    cv.imshow("Original Video", frame)
    cv.imshow("Video Resized", frame_resize)

    if cv.waitKey(20) & 0xFF == ord("d"):
        break

capture.release()
cv.destroyAllWindows()
