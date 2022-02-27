import pygame_widgets
import pygame
import os
from pygame_widgets.button import Button
from pygame_widgets.dropdown import Dropdown
from pygame_widgets.textbox import TextBox
from player import Player
from objects.word import Word


class Game:
    def __init__(self):
        page = pygame.display
        self.screen = page.set_mode((1200, 700))
        page.set_caption("Pendu")
        self.step = 0
        self.steps = []
        self.steps.append('step/pendu1.png')
        self.steps.append('step/pendu2.png')
        self.steps.append('step/pendu3.png')
        self.steps.append('step/pendu4.png')
        self.steps.append('step/pendu5.png')
        self.steps.append('step/pendu6.png')
        self.steps.append('step/pendu7.png')
        self.steps.append('step/pendu8.png')
        self.steps.append('step/pendu9.png')
        self.steps.append('step/pendu10.png')

        self.background = pygame.image.load("image_de_fond.png")
        self.player = Player()
        # self.dialogBox = pygame.image.load("dialog_box.png")

        self.user_text = ''
        self.clock = pygame.time.Clock()
        self.myword = Word()#anticonstitutionnellement
        self.isWin = False

    def renderWords(self):
        posY = 70
        btnListe = []
        for tempword in self.myword.checkedWordsNoSuccess:
            btnListe.append(Button(
                self.screen,  # Surface to place button on
                800,  # X-coordinate of top left corner
                posY,  # Y-coordinate of top left corner
                len(tempword)*15,  # Width
                30,  # Height

                # Optional Parameters
                text=tempword,  # Text to display
                fontSize=30,  # Size of font
                margin=10,  # Minimum distance between text/image and edge of button
                inactiveColour=(200, 50, 0),  # Colour of button when not being interacted with
                hoverColour=(150, 0, 0),  # Colour of button when being hovered over
                pressedColour=(0, 200, 20),  # Colour of button when being clicked
                radius=20,  # Radius of border corners (leave empty for not curved)
                  # Function to call when clicked on
            ))
            posY+= 40
    def renderLetters(self):
        posY = 70
        btnListe = []
        for tempword in self.myword.checkedLettersNoSuccess:
            btnListe.append(Button(
                self.screen,  # Surface to place button on
                710,  # X-coordinate of top left corner
                posY,  # Y-coordinate of top left corner
                len(tempword)*15,  # Width
                30,  # Height

                # Optional Parameters
                text=tempword,  # Text to display
                fontSize=30,  # Size of font
                margin=10,  # Minimum distance between text/image and edge of button
                inactiveColour=(200, 50, 0),  # Colour of button when not being interacted with
                hoverColour=(150, 0, 0),  # Colour of button when being hovered over
                pressedColour=(0, 200, 20),  # Colour of button when being clicked
                radius=20,  # Radius of border corners (leave empty for not curved)
                  # Function to call when clicked on
            ))
            posY+= 40

    def output(self):
        text = self.textbox.getText()
        if text in self.myword.checkedWordsNoSuccess or text in self.myword.checkedLettersNoSuccess:
            print('nope')
        else:
            if len(text) > 1:
                self.isWin = self.myword.checkWord(text)
                if self.myword.checkWord(text):
                    self.myword.checkedLettersSuccess = list(self.myword.baseWord)
                    self.myword.updateActualWord()
                else:
                    self.myword.checkedWordsNoSuccess.append(text)
                    print(self.myword.checkedWordsNoSuccess)
                if not self.isWin:
                    self.nextStep()
            else:
                if not self.myword.checkLetter(text):
                    print(self.myword.checkedLettersNoSuccess)
                    self.nextStep()
            self.myword.updateActualWord()
            self.textbox.setText("")

    def checkText(self):
        text = self.textbox.getText()
        if len(text) > 25:
            self.textbox.setText(text[0:25])

        #
        # if len(text) > 1:
        #     self.textbox.setText(text[0])

    def run(self):
        self.myword.updateActualWord()
        self.textbox = TextBox(
            self.screen, 150, 600, 300, 40, fontSize=30,
            borderColour=(255, 0, 0), textColour=(0, 200, 0),
            onSubmit=self.output, radius=10, borderThickness=5,onTextChanged=self.checkText
        )
        run = True
        while run:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    run = False
            self.isWin = self.myword.checkWord(self.myword.actualWord)
            if self.isWin == True:
                print("Victory !")
            self.displayStep()
            button = Button(
                self.screen,  # Surface to place button on
                50,  # X-coordinate of top left corner
                500,  # Y-coordinate of top left corner
                600,  # Width
                50,  # Height

                # Optional Parameters
                text=self.myword.getWordToDisplay(),  # Text to display
                fontSize=40,  # Size of font
                margin=20,  # Minimum distance between text/image and edge of button
                inactiveColour=(200, 50, 0),  # Colour of button when not being interacted with
                hoverColour=(150, 0, 0),  # Colour of button when being hovered over
                pressedColour=(0, 200, 20),  # Colour of button when being clicked
                radius=20,  # Radius of border corners (leave empty for not curved)
                onClick=lambda: print('Click')  # Function to call when clicked on
            )
            self.renderWords()
            self.renderLetters()
            self.displayWord("Words:", 800, 30)
            self.displayWord("Letters:", 710, 30)
            pygame_widgets.update(events)
            pygame.display.update()
            self.clock.tick(30)
        pygame.quit()

    def start(self):

        self.dropdown = Dropdown(
            self.screen, 120, 10, 100, 50,
            name='Select Color',
            choices=[
                'Red',
                'Blue',
                'Yellow',
            ],
            borderRadius=3,
            colour=pygame.Color('green'),
            values=[1, 2, 'true'],
            direction='down', textHAlign='left'
        )
        start = True
        while start:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    start = False
            # self.displayStep()
            pygame_widgets.update(events)
            pygame.display.update()
            self.clock.tick(30)
        pygame.quit()

    def displayStep(self):
        image = pygame.image.load(self.steps[self.step])
        self.screen.blit(image, (0, 0))

    def nextStep(self):
        if self.step < 9:
            self.step = self.step + 1

    def displayWord(self, words, x, y):
        white = (255, 255, 255)
        black = (0, 0, 0)
        font = pygame.font.Font('freesansbold.ttf', 20)
        text = font.render(words, True, white, black)
        textRect = text.get_rect()
        textRect.center = (x, y)
        self.screen.blit(text, textRect)
