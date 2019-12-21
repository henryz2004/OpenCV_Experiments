import numpy as np
import cv2

img = cv2.imread("person.jpg", 0)
print(img)

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('persongray.jpg', img)
