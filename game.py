import pygame
from player import Player
class Game:
    def __init__(self):
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

        page = pygame.display
        self.screen = page.set_mode((500, 500))
        page.set_caption("Pendu")
        self.background = pygame.image.load("image_de_fond.png")
        self.player = Player()

    def run(self):
        clock = pygame.time.Clock

        run = True
        while run:
            #self.screen.blit(self.background, (0, 0))
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.nextStep()
            self.displayStep()
            pygame.display.update()
            #clock.tick(2)
                    # if text_rect.collidepoint(event.pos):
                    #     button_clicked = True
                    # else:
                    #     button_clicked = False
        pygame.quit()

    def displayStep(self):
        image = pygame.image.load(self.steps[self.step])
        self.screen.blit(image, (0, 0))

    def nextStep(self):
        if self.step < 9:
            self.step = self.step + 1
