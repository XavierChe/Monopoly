import pygame
import time
import pyglet
from PIL import Image

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
gray = (50, 50, 50)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
blue2 = (135, 206, 250)
brown = (91, 60, 17)
rose = (253, 108, 158)
orange = (253, 108, 0)
window = pyglet.window.Window(visible=True, fullscreen=True, caption='Monopoly')

def text_format(message, textSize, textColor):
    newFont = pygame.font.SysFont ("Consolas", textSize)
    newText = newFont.render (message, True, textColor)
    return newText

def board(window_width= window.width, window_height = window.height):
    surface = pygame.display.set_mode((window_width,window_height))
    board_background_image = Image.open('./pictures/board.png').resize((window_width, window_height))
    board_background_image.save('./pictures/board_resized.png')
    board_background = pygame.image.load('./pictures/board_resized.png')
    surface.blit(board_background, (0,0))   

    pygame.display.flip()


if __name__ == "__main__":
    Go = True
    while Go:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                Go = False
            if event.type == pygame.QUIT:
                Go = False
        board()
    pygame.display.quit()
    pygame.quit()
