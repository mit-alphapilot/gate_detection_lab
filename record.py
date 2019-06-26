#!/usr/bin/python
import cv2 
import numpy as np

OUTFILE_DIR = 'data' # make sure this folder exists

cv2.namedWindow('frames')

# setup middle camera
cap = cv2.VideoCapture(2)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

i = 0 

# main body
while True:
    ret, frame = cap.read()
    if i % 10 == 0:
        cv2.imshow('frames', frame)
    outfile = '%s/%08d.png' % (OUTFILE_DIR, i)
    cv2.imwrite(outfile, frame)
    print('Wrote %s' % outfile)
    i += 1
    cv2.waitKey(100) # sleep 100ms (i.e. 10 FPS)

# clean up
cap.release()
cv2.destroyAllWindows()
