import cv2

face = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
capture = cv2.VideoCapture(0)
cv2.namedWindow('Camera')
while True:
    ret, frame = capture.read()
    gary = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    faces = face.detectMultiScale(gary, 1.1, 3, 0, (10, 10), (800, 800))
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (20, 155, 255), 1)
    cv2.imshow('Camera', frame)
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break
capture.release()
cv2.destroyAllWindows()
