import numpy as np
import cv2

img  = cv2.imread("fb1.jpg")

# Edges
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 7)

# color
color = cv2.bilateralFilter(img, 9, 300, 300)

# Cartoon
cartoon = cv2.bitwise_and(color, color, mask=edges)

cv2.imshow("image",img)
cv2.imshow("cartoon", cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()