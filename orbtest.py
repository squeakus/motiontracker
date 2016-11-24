import cv2
import numpy as np

img = cv2.imread('sifttest.jpg')
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

orb = cv2.ORB_create()
kp = orb.detect(gray,None)

out = None

out = cv2.drawKeypoints(gray,kp, out, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imwrite('orb_keypoints.jpg',out)
