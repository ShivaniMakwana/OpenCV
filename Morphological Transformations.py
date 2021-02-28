import cv2
import numpy as np

img = cv2.imread('smarties.png', cv2.IMREAD_GRAYSCALE)
_, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)
kernal = np.ones((5,5), np.uint8)

dilation = cv2.dilate(mask, kernal, iterations=2)
erosion = cv2.erode(mask, kernal, iterations=1)
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal)
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal)
titles = ['image', 'mask', 'dilation', 'erosion', 'opening', 'closing']
images = [img, mask, dilation, erosion, opening, closing]

for i in range(6):
	cv2.imshow(titles[i], images[i])
	cv2.waitKey(0)