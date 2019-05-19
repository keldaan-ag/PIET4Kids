import picamera
import datetime

camera = picamera.PiCamera()
camera.capture(str(datetime.datetime.now()) + '.jpg')