import numpy as np
import cv2

cv2.namedWindow('frame', cv2.WINDOW_NORMAL)

source = cv2.VideoCapture('video.mp4')
frames = []

while True:

    data, frame = source.read()
    if data:
        frames.append(frame)
    else:
        break

source.release()

play = True
paused = False
i = 0

while play:
    frame = frames[i]

    size = cv2.getWindowImageRect("frame")
    cv2.imshow('frame', cv2.resize(frame, (size[2], size[3]), interpolation=cv2.INTER_CUBIC))
    
    key = cv2.waitKey(33) & 0xFF
    if key == ord('q'):
        break
    if key == ord('0'):
        i = 0
    elif key == ord(' '):
        paused = not paused
    elif key == ord('a'):
        i = max(0, i-240)
    elif key == ord('d'):
        i += 240
    elif key == ord('j'):
        i = max(0, i-1)
    elif key == ord('k'):
        i += 1

    if not paused:
        i += 1
        i %= len(frames)

cv2.destroyAllWindows()
