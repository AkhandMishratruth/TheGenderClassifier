import cv2, glob, os
import numpy as np
i=1
path='/media/akhand/PADLE BETA/projects and exp/FACE classifier/Men Resize/'
for filee in glob.glob('/media/akhand/PADLE BETA/projects and exp/FACE classifier/MenFace/*.jpg'):
    filen=cv2.imread(filee)
    name=path+str(i)+'.jpg'
    rows,cols=filen.shape[:2]
    if rows<40:
        filen=cv2.resize(filen,(40,40),interpolation=cv2.INTER_CUBIC)
    else:
        filen=cv2.resize(filen,(40,40),interpolation=cv2.INTER_AREA)
    cv2.imwrite(name,filen)
    i=i+1
    print(filen)
    



