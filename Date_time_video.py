import cv2
import datetime
cap = cv2.VideoCapture(0)

while(cap.isOpened()):
	ret, frame = cap.read()
	if ret == True:
		font = cv2.FONT_HERSHEY_SIMPLEX
		date_time = str(datetime.datetime.now())
		frame = cv2.putText(frame, date_time, (10,50), font, 1, (0, 255, 255), 2, cv2.LINE_AA)
	cv2.imshow('live stream', frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
	print(cap.get(cv2.CAP_PROP_FRAME_WIDTH), cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
cap.release()
cv2.destroyAllWindows()