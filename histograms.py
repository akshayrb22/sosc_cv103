import numpy as np
import cv2
import matplotlib.pyplot as plt

# Read the image.
image = cv2.imread("rick.png", 1)

# Conver the image to grey.
image_grey = cv2.imread("rick.png", 0)

# Display the image
cv2.imshow("Rick", image)
cv2.waitKey(0)

#Display the grey image
cv2.imshow("Rick Grey", image_grey)
cv2.waitKey(0)

hist = cv2.calcHist([image_grey], [0], None, [256], [0, 256])

plt.imshow(hist)

plt.hist(image_grey.ravel(), 256, [0,256])
plt.show()