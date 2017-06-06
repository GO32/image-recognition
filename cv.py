import cv2
import os 

fileInput = input("Type HAAR cascade file path here: ")
filePath = os.path.abspath(fileInput)
faceCascade = cv2.CascadeClassifier(filePath)
camera = cv2.VideoCapture(0)

while True:
    ret, img = camera.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.3, 5)
    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x + w, y + h), (0,255,0), 3)
    
    cv2.imshow('img', img)
    if cv2.waitKey(0) & 0xff == ord('q'):
       break
camera.release()
cv2.destroyAllWindows()
