import os 
import cv2
import numpy

camera = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    ret, img = camera.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale((1.3, 5), gray, img)

    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 3)
        _gray = gray[y:y+h, x:x+w]
        _color = img[y:y+h, x:x+w]
    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
camera.release()
cv2.destroyAllWindows()

