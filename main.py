# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pygame
import socket
import sys
from game import Game
from tools.getword import getword #Return a word from chosen theme as STR
from tools.checkletter import checkLetters #Return list empty if chosen letter isn't in word, or indexs list if not empty
from tools.checkword import checkWord
from tools.wordtodisplay import wordToDisplay
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pygame.init()
    
    game = Game()
    game.run()
    




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# font = pygame.font.SysFont("Arial", 35)
    # text = font.render("exit", True, white)
    # text_clicked = font.render("Clicked", True, white)
    # text_rect = text_clicked.get_rect(center = (width/ 2 ,height /2))
    # button_clicked = False
    # run = True
    #
    #
    #     screen.fill((0,0,0))
    #     screen.blit(background, (0, 0))
    #     pygame.draw.rect(screen,(100,100,100), text_rect)
    #
    #     if button_clicked:
    #         print("c'est bon")
    #
    #         screen.blit(text_clicked, text_rect)
    #         button_clicked = False
    #         sys.exit()
    #     else:
    #         screen.blit(text,text_rect)
    #
    #     pygame.display.update()
    # pygame.quit()
    # quit()