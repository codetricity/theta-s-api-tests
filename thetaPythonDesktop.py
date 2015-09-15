import pygame, sys
import requests
import json
from thetaPythonTest import startSession, takePicture

WHITE = (255,255,255)
GRAY = (230, 230, 230)
GREEN = (100, 200, 50)
DARK = (64, 64, 64)


pygame.init()
SCREENSIZE = (800, 600)
SCREEN = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption("THETA S Unofficial Hacking Guide Example")

button = pygame.Rect(100, 120, 140, 80)
font = pygame.font.Font("fnt/Lato-Thin.ttf", 20)
button_text = font.render("Take Picture", True, DARK)
text_box = (button.left + 15, button.top + 23)

theta = pygame.image.load("img/ricoh-theta-s.png")
theta_rect = theta.get_rect()
theta_rect.right = SCREENSIZE[0] - 50
theta_rect.top = 60

developers_logo = pygame.image.load("img/theta_developers.png")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if button.collidepoint(mouse_pos):
                sid = startSession()
                takePicture(sid)

    SCREEN.fill(WHITE)
    pygame.draw.rect(SCREEN,GRAY, button)
    pygame.draw.rect(SCREEN, DARK, button, 1)
    SCREEN.blit(button_text, text_box)
    SCREEN.blit(theta, theta_rect)
    SCREEN.blit(developers_logo, (10, 10))

    pygame.display.update()
