import pygame, sys
import requests
import json
from thetaPythonTest import startSession, takePicture

WHITE = (255,255,255)
GRAY = (230, 230, 230)
GREEN = (100, 200, 50)
DARK = (64, 64, 64)


pygame.init()
SCREEN = pygame.display.set_mode((800, 600))

button = pygame.Rect(100, 100, 140, 80)
font = pygame.font.Font("fnt/Lato-Thin.ttf", 20)
button_text = font.render("Take Picture", True, DARK)
text_box = (button.left + 15, button.top + 23)

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

    pygame.display.update()
