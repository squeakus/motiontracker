from __future__ import print_function
import numpy as np
import cv2
import sys
import imutils


def main():
    #cap = cv2.VideoCapture('rtsp://admin:'+passwd+'@192.168.1.100:554')
    cap = cv2.VideoCapture(0)
    detector =  cv2.ORB_create()
    img = None

    print("video", cap.isOpened())
    framecnt = 0

    while(True):
        framecnt += 1
        ret, frame = cap.read()
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
    if len(sys.argv) < 1:
        print ("Usage %s" % sys.argv[0])
        sys.exit(1)

    main()
