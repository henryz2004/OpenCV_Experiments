import cv2
import numpy
import math
import functools

def estimate_distance(dimension):
     if len(captured) == 0:
          return -1

     estimate = distance/(dimension[1]/facial_dimension[1])
     return estimate

face_cascade = cv2.CascadeClassifier(r"C:\Users\henry\AppData\Local\Programs\Python\Python37\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml")

camera = cv2.VideoCapture(0)

window = cv2.namedWindow("Main")

captured = []
facial_dimension = [0, 0]     # average w, h of faces
total_dimensions = [0, 0]
distance = 1

running_dims = []

while camera.isOpened():
     returned, picture = camera.read()
     if not returned:
          break

     gray_pic = cv2.cvtColor(picture, cv2.COLOR_BGR2GRAY)

     faces = face_cascade.detectMultiScale(gray_pic, 1.3, 5)

     for (x, y, w, h) in faces:
          cv2.rectangle(picture, (x, y), (x+w, y+h), (255, 255, 0), 2)
          running_dims.append((w, h))
          running_dims = running_dims[-10:]
          average_w = sum(x[0] for x in running_dims)/len(running_dims)
          average_h = sum(x[1] for x in running_dims)/len(running_dims)
          print("The estimated distance for face 0 is:", estimate_distance((average_w, average_h)))

     key = cv2.waitKey(10)
     
     if key == ord(' '):
          captured.append(picture)
          total_dimensions[0] += faces[0][2]
          total_dimensions[1] += faces[0][3]

          facial_dimension = list(map(lambda x: x/len(captured), total_dimensions))
          
          cv2.imshow("Recent capture", picture)
               
     if key == 27: break

     cv2.imshow("Main", picture)

     

cv2.destroyAllWindows()
camera.release()
