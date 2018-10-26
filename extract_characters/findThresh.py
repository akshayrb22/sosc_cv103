import numpy as np
import cv2
import imutils


def nothing(x):
    pass


cv2.namedWindow('image')

cv2.createTrackbar('t','image',0,255,nothing)


while(1):

    image=cv2.imread('./14.jpg')
    resized = imutils.resize(image,width=500)
    ratio = image.shape[0] / float(resized.shape[0])
    t = cv2.getTrackbarPos('t','image')

    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.threshold(blurred, t, 255, cv2.THRESH_BINARY)[1]

    cv2.imshow('res',thresh)
    k = cv2.waitKey(5) & 0xFF
    if k == 32:
        break

cv2.destroyAllWindows()        
