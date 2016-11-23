from __future__ import print_function
import numpy as np
import cv2
import sys
import imutils
from imutils.video import VideoStream
import argparse
import time

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-p", "--picamera", type=int, default=-1,
        	help="whether or not the Raspberry Pi camera should be used")
    ap.add_argument("-d", "--detector", required=True,
        	help="choose detector: sift, surf, orb, akaze, brisk")
    args = vars(ap.parse_args())

    #set up detector
    detstr = args["detector"]
    print("Using", detstr, "for feature detection")

    if detstr == 'sift':
        detector = cv2.xfeatures2d.SIFT_create()
        norm = cv2.NORM_L2
    elif detstr == 'surf':
        detector = cv2.xfeatures2d.SURF_create()
        norm = cv2.NORM_L2
    elif detstr == 'orb':
        detector = cv2.ORB_create(100000)
        norm = cv2.NORM_HAMMING
    elif detstr == 'akaze':
        detector = cv2.AKAZE_create()
        norm = cv2.NORM_HAMMING
    elif detstr == 'brisk':
        detector = cv2.BRISK_create()
        norm = cv2.NORM_HAMMING
    elif detstr == 'daisy':
        detector = cv2.xfeatures2d.DAISY_create()
    elif detstr == 'freak':
        detector = cv2.xfeatures2d.FREAK_create()
        norm = cv2.NORM_HAMMING
    elif detstr == 'latch':
        detector = cv2.xfeatures2d.LATCH_create()
        norm = cv2.NORM_HAMMING
    elif detstr == 'lucid':
        detector = cv2.xfeatures2d.LUCID_create()
        norm = cv2.NORM_HAMMING
    elif detstr == 'vgg':
        detector = cv2.xfeatures2d.VGG_create()
        norm = cv2.NORM_HAMMING

    else:
        print("Cannot find detector",detstr)
        exit()

    #webcam or pycam?
    cap = VideoStream(usePiCamera=args["picamera"] > 0).start()
    print("letting camera warm up")
    time.sleep(2.0)

    img = None
    framecnt = 0
    while True:
        framecnt += 1
        frame = cap.read()
        frame = imutils.resize(frame, width=640)
        framecnt = 0

        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        kp = detector.detect(gray,None)
        img = cv2.drawKeypoints(gray,kp, frame, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

        # Display the resulting frame
        print("keypoints", len(kp))
        cv2.imshow('frame',img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.stop()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
