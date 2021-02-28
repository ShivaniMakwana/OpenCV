import cv2
img = cv2.imread('lena.jpg', 1)
img = cv2.line(img,(0,0), (255,255), (147,96,44), 10)
img = cv2.rectangle(img, (384, 0), (512, 128), (0,0,255), 7)
img = cv2.circle(img, (447, 63), 63, (0,255,0), 6)
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'opencv', (10, 500), font, 4, (0, 255, 255), 4, cv2.LINE_AA)
cv2.imshow('lena', img)
k = cv2.waitKey(0) & 0xFF
if k == 27:
	cv2.destroyAllWindows()
elif k == ord('s'):
	cv2.imwrite('lena_copy.png',img)
	cv2.destroyAllWindows()