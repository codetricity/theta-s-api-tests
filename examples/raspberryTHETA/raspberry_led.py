import pygame, sys
import requests #better alternative to urllib2
import json
# customized python library for THETA S
from thetapylib import * 
import time
# for Raspberry Pi input output pins
import RPi.GPIO as GPIO

# test LEDs to show camera state such as timer.  
# Set to False if you are not using LEDs 
LED = True

if LED:
    GPIO.setmode(GPIO.BCM)
    led_01 = 12
    led_02 = 18
    led_03 = 23
    led_04 = 25
    leds = [led_01, led_02, led_03, led_04]
    for led in leds:
        GPIO.setup(led, GPIO.OUT)
        GPIO.output(led, False)

WHITE = (255,255,255)
GRAY = (230, 230, 230)
GREEN = (100, 200, 50)
DARK = (64, 64, 64)


pygame.init()
SCREENSIZE = (800, 600)
SCREEN = pygame.display.set_mode(SCREENSIZE, pygame.FULLSCREEN)
pygame.display.set_caption("THETA S Unofficial Hacking Guide Example")

font = pygame.font.Font("fnt/Lato-Bold.ttf", 20)
timer_font = pygame.font.Font("fnt/Lato-Bold.ttf", 48)
clock = pygame.time.Clock()
FPS = 20

pictureIcon = pygame.image.load("icon/camera_icon2.png")
pictureButton = pictureIcon.get_rect(topleft=(50,120))
pictureButton_text = font.render("Take Picture", True, DARK)
text_box = (pictureButton.left -24, pictureButton.bottom)

captureStartIcon = pygame.image.load("icon/video.png")
captureStartButton = captureStartIcon.get_rect(topleft=(200, 120))
captureStartButton_text = font.render("Take Video", True, DARK)
captureText_box = (captureStartButton.left - 15, captureStartButton.bottom)

captureStopIcon = pygame.image.load("icon/stop_icon.png")
captureStopButton = captureStopIcon.get_rect(topleft=(200, 230))
captureStopButton_text = font.render("Stop Video", True, DARK)
captureStopText_box = (captureStopButton.left - 15, captureStopButton.bottom)

timerIcon = pygame.image.load("icon/timer_icon.png")
timerButton = timerIcon.get_rect(topleft=(50, 230))
timerButton_text = font.render("Timer 15s", True, DARK)
timerText_box = (timerButton.left - 15, timerButton.bottom)

downloadIcon = pygame.image.load("icon/download.png")
downloadButton = downloadIcon.get_rect(topleft=(50,340))
downloadButton_text = font.render("Download", True, DARK)
downloadText_box = (downloadButton.left -15 , downloadButton.bottom)

# text placement pos for timer countdown
countdown_pos = (320, 230)

theta = pygame.image.load("img/ricoh-theta-s.png")
theta_rect = theta.get_rect()
theta_rect.right = SCREENSIZE[0] - 50
theta_rect.top = 60

developers_logo = pygame.image.load("img/theta_developers.png")

sid = "SID_0001"
delay_on = False

max_step = 20
wait_step = max_step
# captureMode will either be image or _video
mode = "image"
startSession()
sid = getSid()
mode = getMode(sid)
print(mode)


while True:
    if LED:
        # power is on
        GPIO.output(led_01, True)       
        # get camera mode, video or image
        if mode == "image":
            GPIO.output(led_02, True)
            GPIO.output(led_03, False)
        if mode == "_video":
            GPIO.output(led_03, True)
            GPIO.output(led_02, False)
        if wait_step > 0:
            wait_step -= 1
        else:
            sid = getSid()
            mode = getMode(sid)
            wait_step = max_step

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                GPIO.cleanup()
                pygame.quit()
                sys.exit()
                                
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if pictureButton.collidepoint(mouse_pos):
                sid = startSession()
                takePicture(sid)
            if captureStartButton.collidepoint(mouse_pos):
                sid = startSession()
                startCapture(sid)
            if captureStopButton.collidepoint(mouse_pos):
                stopCapture(sid)
            if downloadButton.collidepoint(mouse_pos):
                fileUri = latestFileUri()
                getImage(fileUri)
            if timerButton.collidepoint(mouse_pos):
                start = time.clock()
                delay_on = True

                
## set up keyboard presses for FLIRC USB controller that
## maps an remote controller like an Apple controller
## or any TV remote for easy picture taking.
## Map the FLICR as follows:
## p = take picture
## v = start video capture (or automatic picture if in image mode)
## s = stop video capture or auto-picture
## d = delay
## m = change capture mode

        if not delay_on:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    sid = startSession()
                    takePicture(sid)
                if event.key == pygame.K_v:
                    print("start video capture")
                    sid = startSession()
                    startCapture(sid)
                if event.key == pygame.K_s:
                    print("stop video capture")
                    stopCapture(sid)
                if event.key == pygame.K_d:
                    start = time.clock()
                    delay_on = True
                if event.key == pygame.K_m:
                    # change capture mode
                    pass
            

    if delay_on:
        elapsed = time.clock() - start
        if LED:
            GPIO.output(led_04, True)
        if elapsed > 15:
            if LED:
                GPIO.output(led_04, False)
            delay_on = False
            sid = startSession()
            takePicture(sid)
            
            


    SCREEN.fill(WHITE) # blank out screen

    # draw take picture button
    SCREEN.blit(pictureIcon, pictureButton)
    SCREEN.blit(pictureButton_text, text_box)

    # draw take video button
    SCREEN.blit(captureStartButton_text, captureText_box)
    SCREEN.blit(captureStartIcon, captureStartButton)

    # draw stop video button
    SCREEN.blit(captureStopButton_text, captureStopText_box)
    SCREEN.blit(captureStopIcon, captureStopButton)

    # draw timer button
    SCREEN.blit(timerButton_text, timerText_box)
    SCREEN.blit(timerIcon, timerButton)


    # draw download button
    SCREEN.blit(downloadButton_text, downloadText_box)
    SCREEN.blit(downloadIcon, downloadButton)

    # draw countdown shutter timer
    if delay_on: # only display if timer button pressed
        countdown_text = timer_font.render("Timer: " + str(int(15 - elapsed)), True, DARK)
        SCREEN.blit(countdown_text, countdown_pos)

    # decorations
    SCREEN.blit(theta, theta_rect)
    SCREEN.blit(developers_logo, (10, 10))

    clock.tick(FPS)
    pygame.display.update()
