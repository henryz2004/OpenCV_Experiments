import cv2
import numpy
face_cascade = cv2.CascadeClassifier(r"C:\Users\henry\AppData\Local\Programs\Python\Python37\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(r"C:\Users\henry\AppData\Local\Programs\Python\Python37\Lib\site-packages\cv2\data\haarcascade_eye.xml")
ref = cv2.imread("cropped.jpg")

gray = cv2.cvtColor(ref, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)    # X, Y, width, height

for (x, y, w, h) in faces:
     cv2.rectangle(ref, (x, y), (x+w, y+h), (255, 255, 0), 2)

#cv2.imshow("my image", ref)
#cv2.waitKey(0)


cam = cv2.VideoCapture(0)
last = -1
while cam.isOpened():
     ret, image = cam.read()
     if not ret:
          break

     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
     faces = face_cascade.detectMultiScale(gray, 1.3, 5)
     padding = 0
     
     for i, (x, y, w, h) in enumerate(faces):
          if w <= 0 or h <= 0: continue
          
          face = image[y:y+h, x:x+w]
          gray_face = gray[y:y+h, x:x+w]
          eyes = eye_cascade.detectMultiScale(gray_face)

          for (ex, ey, ew, eh) in eyes:
               cv2.rectangle(face, (ex+padding, ey+padding), (ex+ew+padding, ey+eh+padding), (0, 255, 255), 2)

          cv2.rectangle(image, (x, y), (x+w, y+h), (255, 255, 0), 2)
          
          cv2.imshow(f"Face {i}", image)
     if last > 1:
          for i in range(len(faces), last):
               cv2.destroyWindow(f"Face {i}")

     last = len(faces)

     key = cv2.waitKey(15)
     if key == 27:
          break

cv2.destroyAllWindows()
cam.release()
