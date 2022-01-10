import pygame_textinput
import pygame
import pygame.locals as pl
pygame.init()
from propriete import *

screen_width, screen_height = 500,500
main_screen = pygame.display.set_mode((screen_width,screen_height))

def text_format(message, textSize, textColor):
    newFont = pygame.font.SysFont("Consolas", textSize)
    newText = newFont.render(message, True, textColor)
    return newText


nb_lignes  = 10
screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
width, height = screen.get_size()

def print_text(screen,nb_ligne, text, textSize, textColor):
    txt = text_format(text, textSize, textColor)
    y_init = nb_ligne*height//(nb_lignes+1)
    x_init = (width-height) + 100
    screen.blit(txt, (x_init, y_init))

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
gray = (50, 50, 50)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)


class Text_input_box:
    def __init__(self,width = 200, height = 40, x_init = 10, y_init = 10, screen = None, visible_after : bool = True):
        self.manager = pygame_textinput.TextInputManager(validator=lambda input: len(input) <= 17)
        self.font = pygame.font.SysFont("Consolas", 20)
        self.textinput = pygame_textinput.TextInputVisualizer(manager=self.manager, font_object=self.font)
        self.width = width
        self.height = height
        self.x_init = x_init
        self.y_init = y_init
        self.clock = pygame.time.Clock()
        self.visible = visible_after
        if screen == None:
            self.screen = pygame.display.set_mode((self.width, self.height), pygame.NOFRAME)
        else:
            self.screen = screen

    def show_box (self):
        text_written = ""
        go = True
        while go:
            pygame.draw.rect(self.screen, white, pygame.Rect(self.x_init, self.y_init, self.width, self.height))
            events = pygame.event.get()
            # Feed it with events every frame
            self.textinput.update(events)
            # Blit its surface onto the screen
            self.screen.blit(self.textinput.surface, (self.x_init + 10 ,self.y_init + 10))
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        text_written = self.textinput.value
                        go = False
            pygame.display.update()
            self.clock.tick(40)
        pygame.draw.rect(self.screen, white, pygame.Rect(self.x_init, self.y_init, self.width, self.height))
        pygame.display.update()
        if self.visible:
            text_end = text_format(text_written, 20, black)
            self.screen.blit(text_end,
                              (self.x_init + 10 , self.y_init + 10))
            pygame.display.update()
        return text_written



if __name__ == "__main__":

    box1 = Text_input_box(screen= main_screen, x_init= 100, y_init= 100, visible_after= False)
    box2 = Text_input_box(screen=main_screen, x_init=100, y_init=150, visible_after=True)
    text_receive = box1.show_box()
    text_receive2 = box2.show_box()
    print(text_receive)


    go = True
    while go:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                go = False
            if event.type == pygame.QUIT:
                go = False
    pygame.quit()

