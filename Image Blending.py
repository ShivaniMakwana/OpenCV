import cv2
import numpy as np
apple = cv2.imread('apple.jpg', 1)
orange = cv2.imread('orange.jpg', 1)
print(apple.shape)
print(orange.shape)

apple_orange = np.hstack((apple[:, :256], orange[:, 256:]))

#generate gaussian pyramid for apple
apple_copy = apple.copy()
gp_apple = [apple_copy]
for i in range(6):
	apple_copy = cv2.pyrDown(apple_copy)
	gp_apple.append(apple_copy)

#generate gaussian pyramid for orange
orange_copy = orange.copy()
gp_orange = [orange_copy]
for i in range(6):
	orange_copy = cv2.pyrDown(orange_copy)
	gp_orange.append(orange_copy)

#generate Laplassian pyramid for apple
apple_copy = gp_apple[5]
lp_apple = [apple_copy]
for i in range(5, 0, -1):
	gaussian_expanded = cv2.pyrUp(gp_apple[i])
	laplassian = cv2.subtract(gp_apple[i-1], gaussian_expanded)
	lp_apple.append(laplassian)

#generate Laplassian pyramid for orange
orange_copy = gp_orange[5]
lp_orange = [orange_copy]
for i in range(5, 0, -1):
	gaussian_expanded = cv2.pyrUp(gp_orange[i])
	laplassian = cv2.subtract(gp_orange[i-1], gaussian_expanded)
	lp_orange.append(laplassian)

#Now add left and right halves of images in each other
apple_orange_pyramid = []
n = 0
for apple_lap, orange_lap in zip(lp_apple, lp_orange):
	n += 1
	cols, rows, ch = apple_lap.shape
	laplassian = np.hstack((apple_lap[:, 0:int(cols/2)], orange_lap[:, int(cols/2):]))
	apple_orange_pyramid.append(laplassian)


#Now reconstruct
apple_orange_reconstruct = apple_orange_pyramid[0]
for i in range(1,6):
	apple_orange_reconstruct = cv2.pyrUp(apple_orange_reconstruct)
	apple_orange_reconstruct = cv2.add(apple_orange_pyramid[i], apple_orange_reconstruct)



cv2.imshow('image', apple_orange_reconstruct)
k = cv2.waitKey(0) & 0xFF
if k == 27:
	cv2.destroyAllWindows()
elif k == ord('s'):
	cv2.imwrite('combine.png',img)
	cv2.destroyAllWindows()