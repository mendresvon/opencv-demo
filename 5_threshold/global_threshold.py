import os
import cv2

img_path = os.path.join("..", "data", "bird.jpg")
img = cv2.imread(img_path)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY)

# thresh = cv2.blur(thresh, (3, 3))

cv2.imshow("img", img)
cv2.imshow("thresh", thresh)
cv2.waitKey(0)
