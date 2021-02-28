import cv2
import numpy as np
def nothing(x):
	print(x)

while(True):
	frame = cv2.imread('smarties.png', 1)
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	l_b = np.array([110,50,50])
	u_b = np.array([130, 255, 255])

	mask = cv2.inRange(hsv, l_b, u_b)
	res = cv2.bitwise_and(frame, frame, mask=mask)

	cv2.imshow('frame', frame)
	cv2.imshow('mask', mask)
	cv2.imshow('result', res)
	k = cv2.waitKey(0) & 0xFF
	if k == 27:
		cv2.destroyAllWindows()