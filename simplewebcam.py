#!/usr/bin/env python

from __future__ import print_function
import numpy as np
import imutils
import cv2
import sys


def main():
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--picamera", type=int, default=-1,
    help="whether or not the Raspberry Pi camera should be used")
args = vars(ap.parse_args())

# initialize the video stream and allow the cammera sensor to warmup
vs = VideoStream(usePiCamera=args["picamera"] > 0).start()
time.sleep(2.0)





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
    cap.stop()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    if len(sys.argv) < 1:
        print ("Usage %s" % sys.argv[0])
        sys.exit(1)

    main()
