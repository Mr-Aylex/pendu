import json


class Player:
    def __init__(self):
        self.name = ""
        self.score = 0
        self.totalScore = 0
        self.gamesWin = 0

    @property
    def score(self):
        return self._score

    @property
    def name(self):
        return self._name

    @property
    def totalScore(self):
        return self._totalScore

    @property
    def gamesWin(self):
        return self._gamesWin

    @name.setter
    def name(self, name):
        self._name = name

    @score.setter
    def score(self, score):
        self._score = score

    @totalScore.setter
    def totalScore(self, totalScore):
        self._totalScore = totalScore

    @gamesWin.setter
    def gamesWin(self, value):
        self._gamesWin = value

    def UpdatePlayerStats(self):
        stats = self.readPlayersStats()
        playerStats = {self.name: {"gamesWin": self.gamesWin, "totalScore": self.totalScore}}
        for element in enumerate(stats):
            dictionnaire = element[1]
            index = element[0]
            if self.name in dictionnaire:
                stats[index] = playerStats
        with open("players.json", "w") as file:
            json.dump(stats, file)

    @classmethod
    def getPlayerStats(cls, name):
        globalStats = Player.readPlayersStats()
        player = False
        for tempPlayer in globalStats:
            if name in tempPlayer.keys():
                player = tempPlayer

        return player

    @classmethod
    def readPlayersStats(cls):
        jsonfile = open("players.json", "r")
        stats = json.load(jsonfile)
        jsonfile.close()
        return stats

    @classmethod
    def listPlayers(cls):
        globalStats = Player.readPlayersStats()
        listPlayersNames = []
        for tempPlayer in globalStats:
            for key, value in tempPlayer.items():
                listPlayersNames.append(key)
        return listPlayersNames

    @classmethod
    def addPlayerToStats(cls, name):
        jsonfile = open("players.json", "r")
        stats = json.load(jsonfile)
        jsonfile.close()
        playerStats = {name: {"gamesWin": 0, "totalScore": 0}}
        stats.append(playerStats)
        with open("players.json", "w") as file:
            json.dump(stats, file)

    @classmethod
    def initPlayer(cls, dict):
        player = Player()
        for cle, valeur in dict.items():
            player.name = cle
            player.gamesWin = valeur["gamesWin"]
            player.totalScore = valeur["totalScore"]
        return player
