from __future__ import print_function
import numpy as np
import cv2
import sys
import datetime
import imutils
import time


def main(passwd):
    camera = cv2.VideoCapture('rtsp://admin:' + passwd + '@192.168.1.100:554')
    min_area = 500

    # divx encoding
    fourcc = cv2.VideoWriter_fourcc(*'DIVX')
    # webcam 848x480, IP camera 1080x1920, resized 640x360
    out = cv2.VideoWriter('movement.avi', fourcc, 20.0, (640, 360))

    # initialize the first frame in the video stream
    firstFrame = None

    while(camera.isOpened()):
        # capture frame-by-frame
        grabbed, frame = camera.read()
        text = "Clear"
        if not grabbed:
            break
        # Our operations on the frame come here
        frame = imutils.resize(frame, width=640)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)
        # if the first frame is None, initialize it
        if firstFrame is None:
            firstFrame = gray
            continue

        frameDelta = cv2.absdiff(firstFrame, gray)
        thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]

        # dilate the thresholded image to fill in holes, then find contours
        # on thresholded image
        thresh = cv2.dilate(thresh, None, iterations=2)
        (_, cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                                        cv2.CHAIN_APPROX_SIMPLE)

        # loop over the contours
        if len(cnts) > 0:
            out.write(frame)

        for c in cnts:
            if cv2.contourArea(c) < min_area:
                continue
            # compute the bounding box for the contour, draw it on the frame,
            # and update the text
            (x, y, w, h) = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            text = "Recording"

        # draw the text and timestamp on the frame
        cv2.putText(frame, text, (10, 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
                    (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)

        # show the frame and record if the user presses a key
        cv2.imshow("Security Feed", frame)
        #cv2.imshow("Thresh", thresh)
        #cv2.imshow("Frame Delta", frameDelta)
        key = cv2.waitKey(1) & 0xFF

        # if the `q` key is pressed, break from the lop
        if key == ord("q"):
            break

        # Display the resulting frame
        # cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    camera.release()
    cv2.destroyAllWindows()
    out.release()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print ("Usage %s <pass>" % sys.argv[0])
        sys.exit(1)

    main(sys.argv[1])
