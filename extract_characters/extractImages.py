from pyimagesearch.shapedetector import ShapeDetector
import argparse
import imutils
import cv2

image = cv2.imread('./test.jpg')


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.threshold(blurred, 230, 255, cv2.THRESH_BINARY)[1]

edges = cv2.Canny(thresh,0,0)


cnts = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]
sd = ShapeDetector()

print(len(cnts))
i = 0

for c in cnts:

	M = cv2.moments(c) 
	try:
		i += 1
		cX = int((M["m10"] / M["m00"]+ 1e-7))
		cY = int((M["m01"] / M["m00"]))
	except:
		continue

	shape = sd.detect(c)


	c = c.astype("float")
	c = c.astype("int")

	x, y, width, height = cv2.boundingRect(c)
	roi = image[y+3:y+height-3, x+3:x+width-3]

	cv2.imwrite("./data/image"+str(i)+".jpg",roi)

