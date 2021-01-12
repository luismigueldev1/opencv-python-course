import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype="uint8")
# cv.imshow("Blank", blank)

# paint the image a certain color
# blank[:] = 255, 0, 0
# cv.imshow("Blue", blank)

# draw square in a specific zone
# blank[0:250, 0:250] = 255, 0, 0
# cv.imshow("Blue", blank)

# draw rectangle in a specific zone
# cv.rectangle(blank, (0, 0), (250, 500), (255, 255, 0,), thickness = -1)  # or thickness=cv.FILLED
#cv.rectangle(blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2), (255, 255, 0,), thickness=-1)
#cv.imshow("Rectangle", blank)

# draw a circle in a specific zone
#cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (255, 0, 255), thickness=-1)
#cv.imshow("Circle", blank)


# draw a line
#cv.line(blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2), (255, 255, 255), thickness=3)
#cv.imshow("Line", blank)

# write text on image
cv.putText(blank, "Hello world from opencv", (0, 255), cv.FONT_HERSHEY_TRIPLEX,
           1.0, (0, 255, 0), thickness=2)
cv.imshow("Text", blank)

cv.waitKey(0)
