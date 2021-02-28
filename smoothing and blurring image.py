import cv2
import numpy as np

img = cv2.imread('lena.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

kernel = np.ones((5,5), np.float32)/25

dst = cv2.filter2D(img, -1, kernel)
blur = cv2.blur(img, (5,5))
gblur = cv2.GaussianBlur(img, (5,5), 0)
median = cv2.medianBlur(img, 5)
bilateralFilters = cv2.bilateralFilter(img, 9,75,75)

titles = ['image', 'dst', 'blur', 'gblur', 'median', 'bilateralFilters']
images = [img, dst, blur, gblur, median, bilateralFilters]

for i in range(6):
	cv2.imshow(titles[i], images[i])
	cv2.waitKey(0)