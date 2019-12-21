import numpy as np
import cv2
from matplotlib import pyplot as plt

image = cv2.imread("personsmall.jpg", 1)[..., ::-1]
plt.imshow(image, interpolation='bicubic')
plt.xticks([]), plt.yticks([])
plt.show()
