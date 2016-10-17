import cv2, glob, os
import numpy as np
i=1
path='/media/akhand/PADLE BETA/MenFace/'
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
if  face_cascade.empty():
    raise IOError('Unable   to	load the	face cascade classifier xml	file')
for filen in glob.glob('/media/akhand/PADLE BETA/Men/*.jpg'):
    h=0
    frame= cv2.imread(filen,0)
    face_rects=face_cascade.detectMultiScale( frame, 1.3, 5)
    for (x,y,w,h) in face_rects:
        frame=frame[y:y+h,x:x+w]
    name=path+str(i)+'.jpg'
    if(h!=0):
        cv2.imwrite(name,frame)
    i=i+1
    print(filen)
