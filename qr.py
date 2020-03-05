import cv2
import pyzbar.pyzbar as pyz
import numpy as np

cam = cv2.VideoCapture(0)

dcObj=[]
key = -1
while dcObj == [] and key != 113: #int value for q
    ret,frame = cam.read()
    cv2.imshow('QRSCAN', frame)
    dcObj = pyz.decode(frame)
    key = cv2.waitKey(1)  
if key != 113:
    print("Recycled object: ", dcObj[0].data.decode('ASCII'))
else: 
    print ("QR not detected")  
cam.release()