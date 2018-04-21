# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 16:45:33 2017

@author: LENOVO-PC
"""

import cv2
import serial,time

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
ser = serial.Serial('com7', 11250)
#time.sleep(1)
#winName1 = "Live feed"

winName = "Face Detected"

cv2.startWindowThread()
cv2.namedWindow(winName)

while True:
    facecount =1
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for(x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)
        facecount=0
    if facecount == 0:
        ser.write(b'1')
        time.sleep(0.8)
    else:
        ser.write(b'2')
        time.sleep(0.8)
    cv2.imshow(winName, frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

ser.close()
cap.release()
cv2.destroyWindow(winName)