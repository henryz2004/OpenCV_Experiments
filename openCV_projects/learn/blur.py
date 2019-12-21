import cv2

cam = cv2.VideoCapture(0)

while True:
     ret, img = cam.read()
     if not ret:
          break
     
     cv2.imshow('canny Edge', img)
     cv2.imshow('denoised', cv2.GaussianBlur(img, (5,5), 0))

     if cv2.waitKey(1) == 27:
          break
cv2.destroyAllWindows()
cam.release()
