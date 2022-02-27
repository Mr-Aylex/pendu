class Turn:
    def __init__(self, playerList):
        self.tour = 0
        self.tourMax = len(playerList)
        self.playerList = playerList
        self.player = self.playerList[0]

    @property
    def tour(self):
        return self._tour

    @tour.setter
    def tour(self, tour):
        self._tour = tour

    @property
    def tourMax(self):
        return self._tourMax

    @tourMax.setter
    def tourMax(self, tourMax):
        self._tourMax = tourMax

    @property
    def playerList(self):
        return self._playerList

    @playerList.setter
    def playerList(self, playerList):
        self._playerList = playerList

    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, player):
        self._player = player

    def next(self):
        if self.tour < self.tourMax - 1:
            self.tour += 1
        else:
            self.tour = 0
        self.player = self.playerList[self.tour]

    def __str__(self):
        return str(self.tour)
