import cv2
img = cv2.imread('messi5.jpg', 1)
print(img.shape)
print(img.size)
print(img.dtype)
b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))

ball = img[280:340, 330:390]
img[270:330, 100:160] = ball

cv2.imshow('Messi', img)
k = cv2.waitKey(0) & 0xFF
if k == 27:
	cv2.destroyAllWindows()
elif k == ord('s'):
	cv2.imwrite('Messi_copy.png',img)
	cv2.destroyAllWindows()