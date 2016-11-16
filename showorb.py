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
    args = vars(ap.parse_args())
    cap = VideoStream(usePiCamera=args["picamera"] > 0).start()
    print("letting camera warm up")
    time.sleep(2.0)

    detector =  cv2.ORB_create()
    img = None
    framecnt = 0

    while(True):
        framecnt += 1
        frame = cap.read()
        frame = imutils.resize(frame, width=640)

        framecnt = 0

        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        kp = detector.detect(gray,None)
        img  = cv2.drawKeypoints(gray, kp, frame,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        #cv2.imwrite('orb_keypoints.jpg',img)
        # Display the resulting frame
        print("keypoints", len(kp))
        cv2.imshow('frame',img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
