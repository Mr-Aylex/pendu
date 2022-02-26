# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from objects.word import Word
import pygame
import socket
import sys
from game import Game
from tools.getword import getword #Return a word from chosen theme as STR
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pygame.init()
    
    myword = Word("salut")
    print(myword.actualWord)
    myword.checkLetter('a')
    myword.updateActualWord()
    myword.checkLetter('z')
    myword.updateActualWord()
    print(myword.actualWord)
    myword.checkLetter('u')
    myword.checkLetter('o')
    myword.updateActualWord()
    print(myword.actualWord)
    
    isWin = myword.checkWord(myword.actualWord)
    if isWin == True:
        print("Victory !")
    else:
        print("Not win Yet !")
    
    myword.checkedLettersSuccess = ['s', 'a', 'l', 'u', 't']
    myword.updateActualWord()
    isWin = myword.checkWord(myword.actualWord)
    if isWin == True:
        print("Victory !")
    else:
        print("Not win Yet !")
    
    
    
    # game = Game()
    # game.run()
    




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