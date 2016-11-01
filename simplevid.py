import numpy as np
import cv2
import sys


def main(passwd):
    cap = cv2.VideoCapture('rtsp://admin:'+passwd+'@192.168.1.100:554')

    print "video", cap.isOpened()
    while(cap.isOpened()):
        # Capture frame-by-frame
        ret, frame = cap.read()

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
    if len(sys.argv) < 2:
        print ("Usage %s <pass>" % sys.argv[0])
        sys.exit(1)

    main(sys.argv[1])
