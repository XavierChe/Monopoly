import pygame_textinput
import pygame
pygame.init()


if __name__ == '__main__':

    # Create TextInput-object
    textinput = pygame_textinput.TextInputVisualizer()

    screen = pygame.display.set_mode((1000, 200))
    clock = pygame.time.Clock()

    text_written = "-----ERROR-----"
    go = True

    while go:
        screen.fill((225, 225, 225))

        events = pygame.event.get()

        # Feed it with events every frame
        textinput.update(events)
        # Blit its surface onto the screen
        screen.blit(textinput.surface, (10, 10))

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    text_written = textinput.value
                    go = False
            if event.type == pygame.QUIT:
                go = False

        pygame.display.update()
        clock.tick(30)

    print(text_written)
    pygame.quit()
