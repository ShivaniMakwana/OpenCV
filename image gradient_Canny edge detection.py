import cv2
import numpy as np
img = cv2.imread('messi5.jpg', 1)

lap = cv2.Laplacian(img, cv2.CV_64F)
lag = np.uint8(np.absolute(lap))

sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobelx = np.uint8(np.absolute(sobelX))

sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)
sobely = np.uint8(np.absolute(sobelY))

sobelCombined = cv2.bitwise_or(sobelx, sobely)
canny = cv2.Canny(img, 100, 200)

titles = ['image', 'Laplacian', 'sobelx', 'sobely', 'sobelCombined', 'Canny']
images = [img, lag, sobelx, sobely, sobelCombined, canny]

for i in range(6):
	cv2.imshow(titles[i], images[i])
	cv2.waitKey(0)