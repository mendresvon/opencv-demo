import os
import cv2

img_path = os.path.join('..', 'data', 'whiteboard.jpg')
img = cv2.imread(img_path)

print(img.shape)

# line
cv2.line(img, (100, 150), (300, 450), (0, 255, 0), 3)

# rectangle
cv2.rectangle(img, (200, 350), (600, 450), (0, 0, 255), 3)

# circle
cv2.circle(img, (300, 200), 100, (255, 0, 0), 10)

# text
cv2.putText(img, "Hey you!", (550, 400), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)

cv2.imshow("img", img)
cv2.waitKey(0)