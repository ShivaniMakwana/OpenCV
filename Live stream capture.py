import cv2
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc,20.0, (640,680))
while(cap.isOpened()):
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	cv2.imshow('live stream', gray)
	out.write(frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
	print(cap.get(cv2.CAP_PROP_FRAME_WIDTH), cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
cap.release()
out.release()
cv2.destroyAllWindows()