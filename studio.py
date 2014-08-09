#import libraries
import pibrella
import picamera
import time
import datetime
import pygame

#Pygame setup
pygame.init()



#declare variables

#declare functions
def takepic(pin):
    w = 640
    h = 480

    size = (w,h)
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
    screen = pygame.display.set_mode(size)    
    img = pygame.image.load((a)+".jpg")
    screen.blit(img,(0,0))
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()

        
#main body of code

pibrella.button.pressed(takepic)
time.sleep(0.2)

