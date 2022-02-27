import pygame_widgets
import pygame
import json
from pygame_widgets.button import Button
from pygame_widgets.dropdown import Dropdown
from pygame_widgets.textbox import TextBox
from pygame_widgets.combobox import ComboBox
from player import Player
from objects.word import Word
from objects.turn import Turn


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
        self.myword = Word()  # anticonstitutionnellement
        self.isWin = False

    def renderWords(self):
        posY = 70
        btnListe = []
        for tempword in self.myword.checkedWordsNoSuccess:
            btnListe.append(Button(
                self.screen,  # Surface to place button on
                800,  # X-coordinate of top left corner
                posY,  # Y-coordinate of top left corner
                len(tempword) * 15,  # Width
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
            posY += 40

    def renderLetters(self):
        posY = 70
        btnListe = []
        for tempword in self.myword.checkedLettersNoSuccess:
            btnListe.append(Button(
                self.screen,  # Surface to place button on
                710,  # X-coordinate of top left corner
                posY,  # Y-coordinate of top left corner
                len(tempword) * 15,  # Width
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
            posY += 40

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
                    self.tour.player.score += 3
                    self.tour.player.totalScore += 3
                    self.tour.player.UpdatePlayerStats()
                else:
                    self.myword.checkedWordsNoSuccess.append(text)
                    print(self.myword.checkedWordsNoSuccess)
                if not self.isWin:
                    self.nextStep()
                else:
                    self.tour.player.gamesWin += 1
                    self.tour.player.UpdatePlayerStats()
            else:
                if not self.myword.checkLetter(text):
                    print(self.myword.checkedLettersNoSuccess)
                    self.nextStep()
                else:
                    self.tour.player.score += 1
                    self.tour.player.totalScore += 1
                    self.tour.player.UpdatePlayerStats()
            self.tour.next()
            self.myword.updateActualWord()
            self.textbox.setText("")

    def checkText(self):
        text = self.textbox.getText()
        if len(text) > 25:
            self.textbox.setText(text[0:25])

    def run(self, players):
        playersObj = []
        for name in players:
            playersObj.append(Player.initPlayer(Player.getPlayerStats(name)))

        self.tour = Turn(playersObj)
        self.myword.updateActualWord()
        self.textbox = TextBox(
            self.screen, 150, 600, 300, 40, fontSize=30,
            borderColour=(255, 0, 0), textColour=(0, 200, 0),
            onSubmit=self.output, radius=10, borderThickness=5, onTextChanged=self.checkText
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
            pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(410, 0, 300, 100))
            self.renderTitle("Joueur: " + str(self.tour.player.name), 560, 30)
            self.renderTitle("Score: " + str(self.tour.player.score), 540, 60)
            self.renderTitle("Score globale: " + str(self.tour.player.totalScore), 580, 90)

            self.renderTitle("Words:", 820, 30)
            self.renderTitle("Letters:", 730, 30)
            pygame_widgets.update(events)
            pygame.display.update()
            self.clock.tick(30)
        pygame.quit()

    def print_value(self):
        print(self.dropdown.getSelected())

    # def initGame(self):

    def start(self):
        textPlayer = []
        textPlayer.append(self.renderComboBox(300, 200))
        textPlayer.append(self.renderComboBox(300, 300))
        textPlayer.append(self.renderComboBox(300, 400))
        textPlayer.append(self.renderComboBox(300, 500))
        # self.dropdown = Dropdown(
        #     self.screen, 120, 10, 100, 50, name='Select Color',
        #     choices=[
        #         'Red',
        #         'Blue',
        #         'Yellow',
        #     ],
        #     borderRadius=3,
        #     colour=pygame.Color('green'),
        #     values=[1, 2, 'true'], direction='down',
        #     textHAlign='left'
        # )
        self.button = Button(
            self.screen, 550, 500, 100, 50, text="Jouer",  # Text to display
            fontSize=40,  # Size of font
            margin=20,  # Minimum distance between text/image and edge of button
            inactiveColour=(200, 50, 0),  # Colour of button when not being interacted with
            hoverColour=(150, 0, 0),  # Colour of button when being hovered over
            pressedColour=(0, 200, 20),  # Colour of button when being clicked
            radius=20,  # Radius of border corners (leave empty for not curved)
            onClick=lambda: print('Click')  # Function to call when clicked on
        )
        start = True
        players = []
        while start:
            events = pygame.event.get()
            for event in events:
                if self.button.clicked:
                    for text in textPlayer:
                        name = text.getText()
                        if not name == "":
                            if name not in Player.listPlayers():
                                Player.addPlayerToStats(name)
                            players.append(name)
                        text.hide()
                        text.disable()

                    start = False
                    self.button.hide()

                    self.button.disable()

                if event.type == pygame.QUIT:
                    pygame.quit()
                    start = False
            # se

            self.screen.fill((0, 0, 0))
            self.renderTitle('joueur 1', 350, 170)
            self.renderTitle('joueur 2', 350, 270)
            self.renderTitle('joueur 3', 350, 370)
            self.renderTitle('joueur 4', 350, 470)
            pygame_widgets.update(events)
            pygame.display.update()
        return players

    def displayStep(self):
        image = pygame.image.load(self.steps[self.step])
        self.screen.blit(image, (0, 0))

    def nextStep(self):
        if self.step < 9:
            self.step = self.step + 1

    def renderTitle(self, words, x, y):
        white = (255, 255, 255)
        black = (0, 0, 0)
        font = pygame.font.Font('freesansbold.ttf', 20)
        text = font.render(words, True, white, black)
        textRect = text.get_rect()
        textRect.center = (x, y)
        self.screen.blit(text, textRect)

    def renderComboBox(self, x, y):
        comboBox = ComboBox(
            self.screen, x, y, 250, 50, name='Select Color',
            choices=Player.listPlayers(),  #
            maxResults=4, textColour=(255, 255, 255),
            font=pygame.font.SysFont('calibri', 30),
            borderRadius=3, colour=(0, 0, 200), direction='down',
            textHAlign='left'
        )
        return comboBox
