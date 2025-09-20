import os
import cv2

img = cv2.imread(os.path.join('.', 'data', 'bird.jpg'))

resized_image = cv2.resize(img, (750, 500))

print(img.shape)
print(resized_image.shape)

cv2.imshow('img', img)
cv2.imshow('resized_image', resized_image)
cv2.waitKey(0)

