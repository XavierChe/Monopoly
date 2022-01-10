import pygame
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


def text_format(message, textSize, textColor):
    newFont = pygame.font.SysFont ("Consolas", textSize)
    newText = newFont.render (message, True, textColor)
    return newText

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

    def label(surface, name, x_init, y_init):
        name_prop = text_format(name, 10, black)
        rec_prop = name_prop.get_rect()
        surface.blit(name_prop, (x_init - (rec_prop[2] / 2), y_init ))

    label(surface,'Prison', window.height // 22, 21*window.height // 22)
    label(surface,'Start',21 * window.height // 22, 21*window.height // 22)
    label(surface,'Free Park',window.height // 22, window.height // 22)
    label(surface,'Go Prison', 21 * window.height // 22,  window.height // 22)
    label(surface,'Montparnasse', 11 * window.height // 22, 21*window.height /22)
    label(surface,'St Lazare', 21 * window.height // 22, 11 * window.height // 22)
    label(surface,'Lyon',window.height // 22, 11 * window.height // 22)
    label(surface,'Est', 11*window.height//22, window.height//22)

    label(surface,'Chance',7 * window.height // 22, 21*window.height // 22)
    label(surface,'Chance', 21 * window.height // 22, 13*window.height // 22)
    label(surface,'Chance', 5 * window.height // 22, window.height // 22)
    label(surface,'Chance', 17 * window.height // 22, 21*window.height // 22)
    label(surface,'Chance', 21 * window.height // 22, 7*window.height // 22)
    label(surface,'Chance', window.height // 22, 7*window.height // 22)
    label(surface,'Chance', 11 * window.height // 22, 11*window.height // 22)

    label(surface,'Belleville', 19* window.height // 22, 21*window.height // 22)
    label(surface,'Lecourbe', 15 * window.height // 22, 21*window.height // 22)
    label(surface,'Vaugirard', 9 * window.height // 22, 21*window.height // 22)
    label(surface,'Courcelles', 5 * window.height // 22, 21*window.height // 22)
    label(surface,'République', 3 * window.height // 22, 21*window.height // 22)

    label(surface,'La Villette', window.height // 22, 19*window.height // 22)
    label(surface,'Neuilly', window.height // 22, 15 * window.height // 22)
    label(surface,'Paradis', window.height // 22, 13 * window.height // 22)
    label(surface,'Mozart', window.height // 22, 9 * window.height // 22)
    label(surface,'St Michel', window.height // 22, 5 * window.height // 22)
    label(surface,'Pigalle', window.height // 22, 3 * window.height // 22)

    label(surface,'Matignon', 3*window.height // 22,  window.height // 22)
    label(surface,'Malsherbes', 7 * window.height // 22, window.height // 22)
    label(surface,'H. Martin', 9 * window.height // 22, window.height // 22)
    label(surface,'St Honoré', 13 * window.height // 22, window.height // 22)
    label(surface,'La Bourse', 15 * window.height // 22, window.height // 22)
    label(surface,'La Fayette', 19 * window.height // 22, window.height // 22)

    label(surface,'Paix', 21 * window.height // 22, 19 * window.height // 22)
    label(surface,'Champs', 21 * window.height // 22, 15 * window.height // 22)
    label(surface,'Capucines', 21 * window.height // 22, 9 * window.height // 22)
    label(surface,'Foch', 21 * window.height // 22, 5 * window.height // 22)
    label(surface,'Breteuil', 21 * window.height // 22, 3 * window.height // 22)

    label(surface, 'Impôts', 13 * window.height // 22, 21 * window.height // 22)
    label(surface, 'Electricité', window.height // 22, 17 * window.height // 22)
    label(surface, 'Eau', 17*window.height // 22,  window.height // 22)
    label(surface, 'Taxe', 21 * window.height // 22, 17 * window.height // 22)


    pygame.display.flip()


if __name__ == "__main__":
    Go = True
    while Go:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                Go = False
            if event.type == pygame.QUIT:
                Go = False
        coord = [(21 * height // 22, 21 * height // 22), (19 * height // 22, 21 * height // 22),
                 (17 * height // 22, 21 * height // 22), (15 * height // 22, 21 * height // 22),
                 (13 * height // 22, 21 * height // 22), (11 * height // 22, 21 * height // 22),
                 (9 * height // 22, 21 * height // 22), (7 * height // 22, 21 * height // 22),
                 (5 * height // 22, 21 * height // 22), (3 * height // 22, 21 * height // 22),
                 (height // 22, 21 * height // 22), (height // 22, 19 * height // 22),
                 (height // 22, 17 * height // 22), (height // 22, 15 * height // 22),
                 (height // 22, 13 * height // 22), (height // 22, 11 * height // 22), (height // 22, 9 * height // 22),
                 (height // 22, 7 * height // 22), (height // 22, 5 * height // 22), (height // 22, 3 * height // 22),
                 (height // 22, height // 22), (3 * height // 22, height // 22), (5 * height // 22, height // 22),
                 (7 * height // 22, height // 22), (9 * height // 22, height // 22), (11 * height // 22, height // 22),
                 (13 * height // 22, height // 22), (15 * height // 22, height // 22),
                 (17 * height // 22, height // 22), (19 * height // 22, height // 22),
                 (21 * height // 22, height // 22), (21 * height // 22, 3 * height // 22),
                 (21 * height // 22, 5 * height // 22), (21 * height // 22, 7 * height // 22),
                 (21 * height // 22, 9 * height // 22), (21 * height // 22, 11 * height // 22),
                 (21 * height // 22, 13 * height // 22), (21 * height // 22, 15 * height // 22),
                 (21 * height // 22, 17 * height // 22), (21 * height // 22, 19 * height // 22)]
        board()
    pygame.quit()
