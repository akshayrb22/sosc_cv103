import os
import cv2
import imutils

filesnames = ['image69.jpg', 'image123.jpg', 'image2.jpg', 'rotateimg.py', 'image95.jpg', 'image77.jpg', 'image1.jpg', 'image144.jpg', 'image74.jpg', 'image54.jpg', 'image13.jpg', 'image62.jpg', 'image9.jpg', 'image23.jpg', 'image35.jpg', 'image57.jpg', 'image19.jpg', 'image86.jpg', 'image61.jpg', 'image131.jpg', 'image44.jpg', 'image10.jpg', 'image97.jpg', 'image134.jpg', 'image108.jpg', 'image114.jpg', 'image96.jpg', 'image18.jpg', 'image40.jpg', 'image106.jpg', 'image107.jpg', 'image51.jpg', 'image45.jpg', 'image120.jpg', 'image12.jpg', 'image125.jpg', 'image141.jpg', 'image103.jpg', 'image46.jpg', 'image34.jpg', 'image56.jpg', 'image67.jpg', 'image3.jpg', 'image70.jpg', 'image116.jpg', 'image112.jpg', 'image82.jpg', 'image5.jpg', 'image20.jpg', 'image109.jpg', 'image139.jpg', 'image119.jpg', 'image8.jpg', 'image93.jpg', 'image53.jpg', 'image101.jpg', 'image6.jpg', 'image117.jpg', 'image118.jpg', 'image110.jpg', 'image43.jpg', 'image49.jpg', 'image58.jpg', 'image4.jpg', 'image27.jpg', 'image38.jpg', 'image104.jpg', 'image59.jpg', 'image37.jpg', 'image115.jpg', 'image32.jpg', 'image122.jpg', 'image30.jpg', 'image121.jpg', 'image29.jpg', 'image41.jpg', 'image14.jpg', 'image138.jpg', 'image102.jpg', 'image136.jpg', 'image99.jpg', 'image52.jpg', 'image31.jpg', 'image113.jpg', 'image105.jpg', 'image33.jpg', 'image128.jpg', 'image149.jpg', 'image65.jpg', 'image24.jpg', 'image129.jpg', 'image63.jpg', 'image60.jpg', 'image66.jpg', 'image55.jpg', 'image68.jpg', 'image132.jpg', 'image150.jpg', 'image79.jpg', 'image88.jpg', 'image78.jpg', 'image16.jpg', 'image64.jpg', 'image126.jpg', 'image17.jpg', 'image87.jpg', 'image21.jpg', 'image26.jpg', 'image84.jpg', 'image81.jpg', 'image137.jpg', 'image90.jpg', 'image130.jpg', 'image89.jpg', 'image75.jpg', 'image42.jpg', 'image98.jpg', 'image73.jpg', 'image124.jpg', 'image72.jpg', 'image85.jpg', 'image140.jpg', 'image83.jpg', 'image111.jpg', 'image15.jpg', 'image135.jpg', 'image91.jpg', 'image94.jpg', 'image133.jpg', 'image48.jpg', 'image76.jpg', 'image127.jpg', 'image28.jpg', 'image11.jpg', 'image36.jpg', 'image22.jpg', 'image39.jpg', 'image145.jpg', 'image25.jpg', 'image80.jpg', 'image71.jpg', 'image92.jpg', 'image100.jpg', 'image47.jpg', 'image7.jpg', 'image50.jpg']

for name in filesnames:
	try:
		image = cv2.imread(name)
		rotated = imutils.rotate(image, 180)
		cv2.imwrite(name,rotated)
	except Exception:
		pass
