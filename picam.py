from picamera import PiCamera
from picamera.array import PiRGBArray



from time import sleep
camera = PiCamera()
camera.resolution = (640,480)
camera.framerate = 16
rawCapture = PiRGBArray(camera, size=(640,480))

camera.start_preview()
sleep(10)
camera.stop_preview()

