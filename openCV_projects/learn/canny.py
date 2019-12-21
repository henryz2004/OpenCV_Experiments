import cv2

cam = cv2.VideoCapture(0)

cv2.namedWindow("Original")
cv2.namedWindow("Canny")

minVal = 100
maxVal = 200
kernelSize = 3

def changeMin(val):
     global minVal

     minVal = min(val, maxVal-1)

def changeMax(val):
     global maxVal

     maxVal = max(val, minVal+1)

cv2.createTrackbar("Change minimum threshold", "Canny", 0, 255, changeMin)
cv2.createTrackbar("Change maximum threshold", "Canny", 0, 255, changeMax)

while cam.isOpened():
     ret, img = cam.read()
     if not ret:
          break

     edges = cv2.Canny(img, minVal, maxVal)#, kernelSize, True)
     cv2.imshow("Original", img)
     cv2.imshow("Canny", edges)

     key = cv2.waitKey(1)
     if key == 27:
          break

cv2.destroyAllWindows()
cam.release()
     

