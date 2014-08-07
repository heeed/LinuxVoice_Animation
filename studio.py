#import libraries
import pibrella
import picamera
import time
import datetime

#declare variables

#declare functions
def takepic(pin):
    with picamera.PiCamera() as camera:
        pibrella.light.red.blink(0.1, 0.1)
        a = str(datetime.datetime.now())
        a = a[0:19]
        camera.rotation = 180
        camera.resolution = (640,480)
        camera.start_preview()
        camera.capture((a)+".jpg")
        camera.stop_preview()
        pibrella.light.red.off()

        
#main body of code

pibrella.button.pressed(takepic)
time.sleep(0.2)

