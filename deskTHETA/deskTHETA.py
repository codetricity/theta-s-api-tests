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

pictureButton = pygame.Rect(50, 120, 140, 80)
font = pygame.font.Font("fnt/Lato-Thin.ttf", 20)
pictureButton_text = font.render("Take Picture", True, DARK)
text_box = (pictureButton.left + 15, pictureButton.top + 23)

captureStartButton = pygame.Rect(200, 120, 140, 80)
captureStartButton_text = font.render("Take Video", True, DARK)
captureText_box = (captureStartButton.left + 15, captureStartButton.top + 23)

captureStopButton = pygame.Rect(200, 210, 140, 80)
captureStopButton_text = font.render("Stop Video", True, DARK)
captureStopText_box = (captureStopButton.left + 15, captureStopButton.top + 23)



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

    SCREEN.fill(WHITE) # blank out screen

    # draw take picture button
    pygame.draw.rect(SCREEN,GRAY, pictureButton)
    pygame.draw.rect(SCREEN, DARK, pictureButton, 1)
    SCREEN.blit(pictureButton_text, text_box)

    # draw take video button
    pygame.draw.rect(SCREEN,GRAY, captureStartButton)
    pygame.draw.rect(SCREEN, DARK, captureStartButton, 1)
    SCREEN.blit(captureStartButton_text, captureText_box)

    # draw stop video button
    pygame.draw.rect(SCREEN,GRAY, captureStopButton)
    pygame.draw.rect(SCREEN, DARK, captureStopButton, 1)
    SCREEN.blit(captureStopButton_text, captureStopText_box)

    # decorations
    SCREEN.blit(theta, theta_rect)
    SCREEN.blit(developers_logo, (10, 10))

    pygame.display.update()
