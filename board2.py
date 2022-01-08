import pygame
import time
import pyglet

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

def board(window_width= window.width, window_height = window.height):
    surface = pygame.display.set_mode((window_width,window_height))
    pygame.draw.rect(surface, white, pygame.Rect(0, 0,window_height//11 - 2,window_height//11))
    pygame.draw.rect(surface, white, pygame.Rect(window_height//11 +2, 0,window_height//11 - 2,window_height//11))
    pygame.draw.rect(surface, white, pygame.Rect(2*window_height//11 +2, 0,window_height//11 - 2,window_height//11))
    pygame.draw.rect(surface, white, pygame.Rect(3*window_height//11 +2, 0,window_height//11 - 2,window_height//11))
    pygame.draw.rect(surface, white, pygame.Rect(4*window_height//11 +2, 0,window_height//11 - 2,window_height//11))
    pygame.draw.rect(surface, white, pygame.Rect(5*window_height//11 +2, 0,window_height//11 - 2,window_height//11))
    pygame.draw.rect(surface, white, pygame.Rect(6*window_height//11 +2, 0,window_height//11 - 2,window_height//11))
    pygame.draw.rect(surface, white, pygame.Rect(7*window_height//11 +2, 0,window_height//11 - 2,window_height//11))
    pygame.draw.rect(surface, white, pygame.Rect(8*window_height//11 +2, 0,window_height//11 - 2,window_height//11))
    pygame.draw.rect(surface, white, pygame.Rect(9*window_height//11 +2, 0,window_height//11 - 2,window_height//11))
    pygame.draw.rect(surface, white, pygame.Rect(10*window_height//11 +2, 0,window_height//11 - 2,window_height//11))

    pygame.draw.rect(surface, white, pygame.Rect(0, 10 * window_height // 11, window_height // 11 - 2, window_height // 11))
    pygame.draw.rect(surface, white, pygame.Rect(window_height//11 +2, 10*window_height//11,window_height//11 - 2,window_height//11))
    pygame.draw.rect(surface, white, pygame.Rect(2*window_height//11 +2, 10*window_height//11,window_height//11 - 2,window_height//11))
    pygame.draw.rect(surface, white, pygame.Rect(3*window_height//11 +2, 10*window_height//11,window_height//11 - 2,window_height//11))
    pygame.draw.rect(surface, white, pygame.Rect(4*window_height//11 +2, 10*window_height//11,window_height//11 - 2,window_height//11))
    pygame.draw.rect(surface, white, pygame.Rect(5*window_height//11 +2, 10*window_height//11,window_height//11 - 2,window_height//11))
    pygame.draw.rect(surface, white, pygame.Rect(6*window_height//11 +2, 10*window_height//11,window_height//11 - 2,window_height//11))
    pygame.draw.rect(surface, white, pygame.Rect(7*window_height//11 +2, 10*window_height//11,window_height//11 - 2,window_height//11))
    pygame.draw.rect(surface, white, pygame.Rect(8*window_height//11 +2, 10*window_height//11,window_height//11 - 2,window_height//11))
    pygame.draw.rect(surface, white, pygame.Rect(9*window_height//11 +2, 10*window_height//11,window_height//11 - 2,window_height//11))
    pygame.draw.rect(surface, white, pygame.Rect(10*window_height//11 +2, 10*window_height//11,window_height//11 - 2,window_height//11))

    pygame.draw.rect(surface, white, pygame.Rect(0, window_height//11 + 2,window_height//11 - 2,window_height//11 - 2))
    pygame.draw.rect(surface, white, pygame.Rect(0, 2*window_height // 11 + 2, window_height // 11 - 2, window_height // 11 - 2))
    pygame.draw.rect(surface, white, pygame.Rect(0, 3 * window_height // 11 + 2, window_height // 11 - 2, window_height // 11 - 2))
    pygame.draw.rect(surface, white,pygame.Rect(0, 4 * window_height // 11 + 2, window_height // 11 - 2, window_height // 11 - 2))
    pygame.draw.rect(surface, white,pygame.Rect(0, 5 * window_height // 11 + 2, window_height // 11 - 2, window_height // 11 - 2))
    pygame.draw.rect(surface, white,pygame.Rect(0, 6 * window_height // 11 + 2, window_height // 11 - 2, window_height // 11 - 2))
    pygame.draw.rect(surface, white,pygame.Rect(0, 7 * window_height // 11 + 2, window_height // 11 - 2, window_height // 11 - 2))
    pygame.draw.rect(surface, white,pygame.Rect(0, 8 * window_height // 11 + 2, window_height // 11 - 2, window_height // 11 - 2))
    pygame.draw.rect(surface, white,pygame.Rect(0, 9 * window_height // 11 , window_height // 11 - 2, window_height // 11 - 2))

    pygame.draw.rect(surface, white,pygame.Rect(10*window_height//11 +2, window_height//11 + 2 ,window_height//11 - 2,window_height//11 - 2))
    pygame.draw.rect(surface, white,pygame.Rect(10 * window_height // 11 + 2, 2*window_height // 11 + 2, window_height // 11 - 2,window_height // 11 - 2))
    pygame.draw.rect(surface, white,pygame.Rect(10 * window_height // 11 + 2, 3*window_height // 11 + 2, window_height // 11 - 2,window_height // 11 - 2))
    pygame.draw.rect(surface, white,pygame.Rect(10 * window_height // 11 + 2, 4*window_height // 11 + 2, window_height // 11 - 2,window_height // 11 - 2))
    pygame.draw.rect(surface, white,pygame.Rect(10 * window_height // 11 + 2, 5*window_height // 11 + 2, window_height // 11 - 2,window_height // 11 - 2))
    pygame.draw.rect(surface, white,pygame.Rect(10 * window_height // 11 + 2, 6*window_height // 11 + 2, window_height // 11 - 2,window_height // 11 - 2))
    pygame.draw.rect(surface, white,pygame.Rect(10 * window_height // 11 + 2, 7*window_height // 11 + 2, window_height // 11 - 2,window_height // 11 - 2))
    pygame.draw.rect(surface, white,pygame.Rect(10 * window_height // 11 + 2, 8*window_height // 11 + 2, window_height // 11 - 2,window_height // 11 - 2))
    pygame.draw.rect(surface, white,pygame.Rect(10 * window_height // 11 + 2, 9*window_height // 11 + 2, window_height // 11 - 2,window_height // 11 - 4))

    pygame.draw.rect(surface, white, pygame.Rect(window_height + 2 , 0, window_width - window_height - 2,window_height - 2))
    pygame.draw.rect(surface, white, pygame.Rect(3*window_height//11, 4*window_height//11, 5*window_height//11, 3*window_height//11))

    pygame.draw.rect(surface, blue2,pygame.Rect(window.height // 11 + 2, 10 * window.height // 11, window.height // 11 - 2,window.height // 33 + 1))
    pygame.draw.rect(surface, blue2,pygame.Rect(2*window.height // 11 + 2, 10 * window.height // 11, window.height // 11 - 2,window.height // 33 + 1))
    pygame.draw.rect(surface, blue2,pygame.Rect(4*window.height // 11 + 2, 10 * window.height // 11, window.height // 11 - 2,window.height // 33 + 1))

    pygame.draw.rect(surface, brown,pygame.Rect(7 * window.height // 11 + 2, 10 * window.height // 11, window.height // 11 - 2,window.height // 33 + 1))
    pygame.draw.rect(surface, brown,pygame.Rect(9 * window.height // 11 + 2, 10 * window.height // 11, window.height // 11 - 2,window.height // 33 + 1))

    pygame.draw.rect(surface, red,pygame.Rect(window.height // 11 + 2, 2 * window.height // 33, window.height // 11 - 2,window.height // 33 + 1))
    pygame.draw.rect(surface, red,pygame.Rect(3*window.height // 11 + 2, 2 * window.height // 33, window.height // 11 - 2,window.height // 33 + 1))
    pygame.draw.rect(surface, red,pygame.Rect(4*window.height // 11 + 2, 2 * window.height // 33, window.height // 11 - 2,window.height // 33 + 1))
    pygame.draw.rect(surface, yellow,pygame.Rect(6*window.height // 11 + 2, 2 * window.height // 33, window.height // 11 - 2,window.height // 33 + 1))
    pygame.draw.rect(surface, yellow,pygame.Rect(7 * window.height // 11 + 2, 2 * window.height // 33, window.height // 11 - 2,window.height // 33 + 1))
    pygame.draw.rect(surface, yellow,pygame.Rect(9 * window.height // 11 + 2, 2 * window.height // 33, window.height // 11 - 2,window.height // 33 + 1))

    pygame.draw.rect(surface, rose, pygame.Rect(2 * window.height // 33, 9 * window.height // 11 , window.height // 33-1,window.height // 11-2))
    pygame.draw.rect(surface, rose, pygame.Rect(2 * window.height // 33, 7 * window.height // 11 +2, window.height // 33-1,window.height // 11-2))
    pygame.draw.rect(surface, rose, pygame.Rect(2 * window.height // 33, 6 * window.height // 11 +2, window.height // 33-1,window.height // 11-2))

    pygame.draw.rect(surface, orange, pygame.Rect(2 * window.height // 33, 4 * window.height // 11 +2, window.height // 33-1,window.height // 11-2))
    pygame.draw.rect(surface, orange, pygame.Rect(2 * window.height // 33, 2 * window.height // 11 +2, window.height // 33-1,window.height // 11-2))
    pygame.draw.rect(surface, orange, pygame.Rect(2 * window.height // 33, 1 * window.height // 11 +2, window.height // 33-1,window.height // 11-2))

    pygame.draw.rect(surface, blue, pygame.Rect(30 * window.height // 33+2, 9 * window.height // 11 , window.height // 33-1,window.height // 11-2))
    pygame.draw.rect(surface, blue, pygame.Rect(30 * window.height // 33+2, 7 * window.height // 11 +2, window.height // 33-1,window.height // 11-2))

    pygame.draw.rect(surface, green, pygame.Rect(30 * window.height // 33+2, 4 * window.height // 11 +2, window.height // 33-1,window.height // 11-2))
    pygame.draw.rect(surface, green, pygame.Rect(30 * window.height // 33+2, 2 * window.height // 11 +2, window.height // 33-1,window.height // 11-2))
    pygame.draw.rect(surface, green, pygame.Rect(30 * window.height // 33+2, 1 * window.height // 11 +2, window.height // 33-1,window.height // 11-2))


    pygame.display.flip()

board()

