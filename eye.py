import cv2
eye=cv2.CascadeClassifier('haarcascade_eye.xml')
video=cv2.VideoCapture(0)
while 1:
    success,image=video.read()
    gimg=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    eye_=eye.detectMultiScale(gimg,1.2,4)
    for (x,y,w,h) in eye_:
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow('EYE_Detection',image)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
video.release()
cv2.destroyAllWindows()
