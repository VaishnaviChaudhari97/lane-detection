import numpy as np
import cv2

image = cv2.imread('C:/Users/vaish/OneDrive/Documents/AI Project/test_image.jpg')
lane_image = np.copy(image)
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
blur = cv2.GaussianBlur(gray,(5,5),0)
canny = cv2.Canny(gray, 50, 150)
cv2.imshow("result", canny)
cv2.waitKey(0)