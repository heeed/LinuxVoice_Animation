#import libraries
import pibrella
import picamera
import time
import datetime
import pygame

#Pygame setup
pygame.init()

w = 640
h = 480

size = (w,h)
screen = pygame.display.set_mode(size)

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
        img = camera.capture((a)+".jpg")
        camera.stop_preview()
        pibrella.light.red.off()
	img = pygame.image.load("./2014-08-07 16:40:07.jpg")
	screen.blit(img,(0,0))
	pygame.display.flip()
	time.sleep(3)
	pygame.quit()

        
#main body of code

pibrella.button.pressed(takepic)
time.sleep(0.2)

