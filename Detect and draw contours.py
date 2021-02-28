import cv2
img = cv2.imread('opencv-logo.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print("no. of contours: "+ str(len(contours)))
print(contours[0])

cv2.drawContours(img, contours, 9, (0, 255, 0, 3))
cv2.imshow('image', img)
cv2.imshow('image_gray', img_gray)

k = cv2.waitKey(0) & 0xFF
if k == 27:
	cv2.destroyAllWindows()
elif k == ord('s'):
	cv2.imwrite('lena_copy.png',img)
	cv2.destroyAllWindows()