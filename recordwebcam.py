import numpy as np
import cv2
import sys


def main(passwd):
    cap = cv2.VideoCapture('rtsp://admin:'+passwd+'@192.168.1.100:554')

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'DIVX')

    #the spec is for my webcam, the IP camera is 1080x1920
    out = cv2.VideoWriter('output.avi',fourcc, 20.0, (848,480))
    out = cv2.VideoWriter('output.avi',fourcc, 20.0, (1920,1080))

    while(cap.isOpened()):
        ret, frame = cap.read()

        if ret==True:
            # write the frame
            out.write(frame)

            cv2.imshow('frame',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    # Release everything if job is finished
    cap.release()
    out.release()
    cv2.destroyAllWindows()



if __name__ == '__main__':
    if len(sys.argv) < 2:
        print ("Usage %s <pass>" % sys.argv[0])
        sys.exit(1)

    main(sys.argv[1])
