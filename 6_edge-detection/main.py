import os
import cv2
import numpy as np

img_path = os.path.join('..', 'data', 'bird.jpg')
img = cv2.imread(img_path)

#img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# It is best practice to convert images to grayscale before edge detection
img_edge = cv2.Canny(img, 100, 200)

img_edge_d = cv2.dilate(img_edge, np.ones((3, 3), dtype=np.int8))

img_edge_e = cv2.erode(img_edge_d, np.ones((3, 3), dtype=np.int8))



cv2.imshow("img", img)
cv2.imshow("img_edge", img_edge)
cv2.imshow("img_edge_d", img_edge_d)
cv2.imshow("img_edge_e", img_edge_e)
cv2.waitKey(0)