import pygame_textinput
import pygame
import pygame.locals as pl
pygame.init()

screen_width, screen_height = 500,500
main_screen = pygame.display.set_mode((screen_width,screen_height))

def text_format(message, textSize, textColor):
    newFont = pygame.font.SysFont("Consolas", textSize)
    newText = newFont.render(message, True, textColor)
    return newText

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
gray = (50, 50, 50)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)


class Text_input_box:
    def __init__(self,width = 200, height = 40, x_init = 10, y_init = 10, screen = None):
        self.manager = pygame_textinput.TextInputManager(validator=lambda input: len(input) <= 17)
        self.font = pygame.font.SysFont("Consolas", 20)
        self.textinput = pygame_textinput.TextInputVisualizer(manager=self.manager, font_object=self.font)
        self.width = width
        self.height = height
        self.x_init = x_init
        self.y_init = y_init
        self.clock = pygame.time.Clock()
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
        text_end = text_format(text_written, 20, black)
        text_end_rect = text_end.get_rect()
        self.screen.blit(text_end,
                              (self.x_init + 10 , self.y_init + 10))
        pygame.display.update()
        return text_written



if __name__ == "__main__":
    box1 = Text_input_box(screen= main_screen, x_init= 100, y_init= 100)
    text_receive = box1.show_box()
    print(text_receive)
    while True:
        pass



