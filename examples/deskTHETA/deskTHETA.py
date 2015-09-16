import pygame, sys
import requests
import json
from thetapylib import *

WHITE = (255,255,255)
GRAY = (230, 230, 230)
GREEN = (100, 200, 50)
DARK = (64, 64, 64)


pygame.init()
SCREENSIZE = (800, 600)
SCREEN = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption("THETA S Unofficial Hacking Guide Example")

font = pygame.font.Font("fnt/Lato-Bold.ttf", 20)

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

downloadIcon = pygame.image.load("icon/download.png")
downloadButton = downloadIcon.get_rect(topleft=(50,340))
downloadButton_text = font.render("Download", True, DARK)
downloadText_box = (downloadButton.left -15 , downloadButton.bottom)

theta = pygame.image.load("img/ricoh-theta-s.png")
theta_rect = theta.get_rect()
theta_rect.right = SCREENSIZE[0] - 50
theta_rect.top = 60

developers_logo = pygame.image.load("img/theta_developers.png")

sid = "SID_0001"

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
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

    # draw download button
    SCREEN.blit(downloadButton_text, downloadText_box)
    SCREEN.blit(downloadIcon, downloadButton)

    # decorations
    SCREEN.blit(theta, theta_rect)
    SCREEN.blit(developers_logo, (10, 10))

    pygame.display.update()
