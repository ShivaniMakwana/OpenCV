import cv2
def click_event(event, x, y, flags, params):
	if event == cv2.EVENT_LBUTTONDOWN:
		print(x, y)
		font = cv2.FONT_HERSHEY_SIMPLEX
		strxy = str(x) + " " + str(y)
		cv2.putText(img, strxy, (10,50), font, 1, (0, 255, 255), 2, cv2.LINE_AA)
		cv2.imshow("image", img)
img = cv2.imread('lena.jpg', 1)
cv2.imshow('image', img)
cv2.setMouseCallback('image', click_event)
k = cv2.waitKey(0) & 0xFF
if k == 27:
	cv2.destroyAllWindows()
elif k == ord('s'):
	cv2.imwrite('lena_copy.png',img)
	cv2.destroyAllWindows()