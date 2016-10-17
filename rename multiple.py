import glob, re, os
i=1
for filen in glob.glob('/media/akhand/PADLE BETA/Men/*.jpg'):
    newn='/media/akhand/PADLE BETA/Men/' +str(i)+ ".jpg"
    os.rename(filen,newn)
    i=i+1
