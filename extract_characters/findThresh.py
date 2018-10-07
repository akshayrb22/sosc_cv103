import numpy as np
import cv2
import imutils

cap=cv2.VideoCapture(1)
def nothing(x):
    pass


cv2.namedWindow('image')
# cv2.createTrackbar('H','image',0,255,nothing)
# cv2.createTrackbar('S','image',0,255,nothing)
# cv2.createTrackbar('V','image',0,255,nothing)
# cv2.createTrackbar('h','image',0,255,nothing)
# cv2.createTrackbar('s','image',0,255,nothing)
# cv2.createTrackbar('v','image',0,255,nothing)
cv2.createTrackbar('t','image',0,255,nothing)


while(1):

    image=cv2.imread('./11.jpg')
    resized = imutils.resize(image,width=500)
    ratio = image.shape[0] / float(resized.shape[0])
    # hsv = cv2.cvtColor(resized, cv2.COLOR_BGR2HSV)



    # H = cv2.getTrackbarPos('H','image')
    # S = cv2.getTrackbarPos('S','image')
    # V = cv2.getTrackbarPos('V','image')

    # h = cv2.getTrackbarPos('h','image')
    # s = cv2.getTrackbarPos('s','image')
    # v = cv2.getTrackbarPos('v','image')
    t = cv2.getTrackbarPos('t','image')


    # lower_blue = np.array([h,s,v])
    # upper_blue = np.array([48,25,126])

    # mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # res = cv2.bitwise_and(resized,resized, mask= mask)
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.threshold(blurred, t, 255, cv2.THRESH_BINARY)[1]

    #edges = cv2.Canny(thresh,0,0)

                    
    # cnts = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL,
    #     cv2.CHAIN_APPROX_SIMPLE)
    # cnts = cnts[0] if imutils.is_cv2() else cnts[1]

    # # loop over the contours
    # for c in cnts:
    #         # compute the center of the contour, then detect the name of the
    #         M = cv2.moments(c)
            

    #         if M["m00"] > 0:
    #             cX = int((M["m10"] / M["m00"]+ 1e-7) * ratio)
    #             cY = int((M["m01"] / M["m00"]+ 1e-7) * ratio)
                
    #             # multiply the contour (x, y)-coordinates by the resize ratio,
    #             # then draw the contours and the name of the shape on the image
    #             c = c.astype("float")
    #             c *= ratio
    #             c = c.astype("int")
    #             area=cv2.contourArea(c)
    #             if(area>20):
    #                 cv2.drawContours(resized, [c], -1, (0, 255, 0), 2)
    #                 cv2.putText(resized, ' town hall', (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 255, 255), 2)
    #                 cv2.circle(resized, (cX, cY),3 , (0, 0, 0), -1)

    # cv2.imshow('frame',edges)
    cv2.imshow('res',thresh)
    k = cv2.waitKey(5) & 0xFF
    if k == 32:
        break

cv2.destroyAllWindows()        
