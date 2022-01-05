import pygame
import pyglet
#import pyscroll
#import pytmx
from pygame.locals import *


#======================================================================================================================
#======================================================================================================================
#======================================================================================================================
#======================================================================================================================
#======================================================================================================================
#======================================================================================================================
#======================================================================================================================
#======================================================================================================================



# INITIALISATION OF PYGAME          /!\ IMPORTANT
pygame.init()


# Text Renderer
def text_format(message, textSize, textColor):
    newFont = pygame.font.SysFont(None, textSize)
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


class Game_graphical ():
    def __init__(self,screen_width, screen_height):
        self.main_screen = pygame.display.set_mode((screen_width,screen_height))
        self.width = screen_width
        self.height = screen_height

    # BEGINNING OF THE GAME : MAIN MENU AND PLAYER SELECTION
    def run_main_menu(self):
        """Main menu of the game
        -> return 0 if new game
        -> return -1 if quit
        """
        play: bool = True
        selected = "start"
        game_on = True
        title_screen = pygame.image.load('pictures/title_screen.jpg')
        title_screen = title_screen.convert()
        while play:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    play = False
                    game_on = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        selected = "start"
                    if event.key == pygame.K_DOWN:
                        selected = "quit"
                    if event.key == pygame.K_RETURN:
                        if(selected == "start"):
                            play = False
                        elif(selected == "quit"):
                            play = False
                            game_on = False
                    if event.key == pygame.K_ESCAPE:
                        play = False
                        game_on = False
            if selected == "start":
                text_start = text_format("New Game", 50, red)
                text_quit = text_format("Quit", 50, black)
            if selected == "quit":
                text_start = text_format("New Game", 50, black)
                text_quit = text_format("Quit", 50, red)
            start_rect = text_start.get_rect()
            quit_rect = text_quit.get_rect()
            self.main_screen.fill(pygame.Color("white"))
            self.main_screen.blit(title_screen, (0, 0))
            self.main_screen.blit(text_start,(self.width/2 - (start_rect[2]/2), self.height/2))
            self.main_screen.blit(text_quit,(self.width/2 - (quit_rect[2]/2), self.height/2 + 100))
            pygame.display.update()
        self.main_screen.fill(pygame.Color("white"))
        pygame.display.update()
        if not game_on:
            return -1
        return 0

    def run_choose_your_character(self):
        """ choose the number of players
        -> return 2, 3, or 4 for the number of player
        -> return -1 for if echap
        -> return 0 if quit
        """
        play : bool = True
        selection_cursor = 0
        nb_players = -1
        title_screen = pygame.image.load('pictures/title_screen.jpg')
        title_screen = title_screen.convert()
        while play:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    play = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        selection_cursor = ((selection_cursor-1) % 3)
                    if event.key == pygame.K_DOWN:
                        selection_cursor = ((selection_cursor+1) % 3)
                    if event.key == pygame.K_RETURN:
                        if(selection_cursor == 0):
                            play = False
                            nb_players = 2
                        elif (selection_cursor == 1):
                            play = False
                            nb_players = 3
                        elif (selection_cursor == 2):
                            play = False
                            nb_players = 4
                    if event.key == pygame.K_ESCAPE:
                        play = False
                        nb_players = -1
            if selection_cursor == 0:
                player2 = text_format("2 players",50,red)
                player3 = text_format("3 players", 50, black)
                player4 = text_format("4 players", 50, black)
            if selection_cursor == 1:
                player2 = text_format("2 players",50,black)
                player3 = text_format("3 players", 50, red)
                player4 = text_format("4 players", 50, black)
            if selection_cursor == 2:
                player2 = text_format("2 players",50,black)
                player3 = text_format("3 players", 50, black)
                player4 = text_format("4 players", 50, red)
            player2_rect = player2.get_rect()
            player3_rect = player3.get_rect()
            player4_rect = player4.get_rect()
            self.main_screen.fill(pygame.Color("white"))
            self.main_screen.blit(title_screen, (0, 0))
            self.main_screen.blit(player2,(self.width/2 - (player2_rect[2]/2), self.height/2))
            self.main_screen.blit(player3,(self.width/2 - (player3_rect[2]/2), self.height/2 + 100))
            self.main_screen.blit(player4,(self.width/2 - (player4_rect[2]/2), self.height/2+ 200))
            pygame.display.update()
        self.main_screen.fill(pygame.Color("white"))
        pygame.display.update()
        return nb_players

    def enter_player_names (self, nb_player):
        title_screen = pygame.image.load('pictures/title_screen.jpg')
        title_screen = title_screen.convert()
        play : bool = True
        exit = -1
        while play:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    play = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        play = False
                        exit = 0
            self.main_screen.fill(pygame.Color("white"))
            self.main_screen.blit(title_screen, (0, 0))
            text_player1 = text_format("Player 1", 40, black)
            text_player2 = text_format("Player 2", 40, black)
            text_player3 = text_format("Player 3", 40, black)
            text_player4 = text_format("Player 4", 40, black)
            text_player1_rect = text_player1.get_rect()
            text_player2_rect = text_player2.get_rect()
            text_player3_rect = text_player3.get_rect()
            text_player4_rect = text_player4.get_rect()
            if (nb_player >= 2):
                self.main_screen.blit(text_player1,(self.width/2, self.height/2))
                self.main_screen.blit(text_player2, (self.width / 2, self.height / 2 + 70))
                pygame.draw.circle(self.main_screen,red,(self.width/2 - (text_player1_rect[2]), self.height/2 + (text_player1_rect[3]/2)),20)
                pygame.draw.circle(self.main_screen, green, (self.width / 2 - (text_player2_rect[2]), self.height / 2 + 70 + (text_player2_rect[3]/2)), 20)
            if (nb_player >= 3):
                self.main_screen.blit(text_player3, (self.width / 2, self.height / 2 + 140))
                pygame.draw.circle(self.main_screen, yellow, (self.width / 2 - (text_player3_rect[2]), self.height / 2 + 140 + (text_player3_rect[3]/2)), 20)
            if (nb_player >= 4):
                self.main_screen.blit(text_player4, (self.width / 2, self.height / 2 + 210))
                pygame.draw.circle(self.main_screen, blue, (self.width / 2 - (text_player4_rect[2]), self.height / 2 + 210 + (text_player4_rect[3]/2)), 20)
            text_continue = text_format("Press Enter to continue", 50, black)
            text_continue_rect = text_continue.get_rect()
            self.main_screen.blit(text_continue,(self.width/2 - (text_continue_rect[2]/2), self.height/2 + 300))
            pygame.display.update()
        self.main_screen.fill(pygame.Color("white"))
        pygame.display.update()
        return exit

    def begin_game(self):
        """Première partie du programme graphique. Menu principal + choix du nombre de joueurs
            => return le nombre de player (int)"""
        exit_condition = self.run_main_menu()
        if exit_condition != -1:
            nb_players = game.run_choose_your_character()
            if nb_players != -1:
                self.enter_player_names(nb_players)
                return nb_players
            elif nb_players == 0:
                self.end_game()
            else:
                return self.begin_game()



    # MAIN LOOP OF THE GAME
    pass



    # END OF THE GAME
    def end_game(self):
        pygame.quit()




#======================================================================================================================
#======================================================================================================================
#======================================================================================================================
#======================================================================================================================
#======================================================================================================================
#======================================================================================================================
#======================================================================================================================
#======================================================================================================================


# TEST
game = Game_graphical(1021,1021)
nb_player = game.begin_game()
game.end_game()
