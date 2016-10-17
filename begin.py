import cv2
import numpy as np
import scipy.io as sio

a=b=c=0
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
if  face_cascade.empty():
    raise IOError('Unable   to	load the	face cascade classifier xml	file')
cap=cv2.VideoCapture(0)
scaling_factor = 0.5

while(True):
    ret, tframe= cap.read()
    Liveframe=cv2.resize(tframe,None,fx=scaling_factor,fy=scaling_factor,interpolation=cv2.INTER_AREA)
    frame=cv2.cvtColor(Liveframe,cv2.COLOR_BGR2GRAY)
    face_rects=face_cascade.detectMultiScale( frame, 1.3, 5)
    for (x,y,w,h) in face_rects:
        frame=frame[y:y+h,x:x+w]
        a,b,c=x,w,y
    rows,cols=frame.shape[:2]
    if rows<40:
        frame=cv2.resize(frame,(40,40),interpolation=cv2.INTER_CUBIC)
    else:
        frame=cv2.resize(frame,(40,40),interpolation=cv2.INTER_AREA)

    frame=np.reshape(frame,(1,1600))
    frame=np.c_[np.array([[1]]), frame]

    theta=sio.loadmat('theta.mat')['theta']

    val=frame.dot(theta)
    if(val[0][0]<0):
        sex='male'
    else:
        sex='female'
  
    cv2.putText(Liveframe,sex, (a+b,c), cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
    cv2.imshow('Gender Detector', Liveframe)
    c=cv2.waitKey(1)
    if c==27:
        break
cap.release()
cv2.destroyAllWindows
        
