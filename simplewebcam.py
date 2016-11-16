#!/usr/bin/env python

from __future__ import print_function
import numpy as np
import imutils
import cv2
import sys


def main():
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FPS,10)
    print("video", cap.isOpened())
    while(cap.isOpened()):
        # Capture frame-by-frame
        ret, frame = cap.read()
        #reduce image size for rpi

        frame = imutils.resize(frame, width=640)
        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the resulting frame
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    if len(sys.argv) < 1:
        print ("Usage %s" % sys.argv[0])
        sys.exit(1)

    main()
