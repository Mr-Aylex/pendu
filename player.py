class Player:
    def __init__(self):
        self.name = ""
        self.score = 0
    
    @property
    def score(self):
        return self._score
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
    
    @name.score
    def score(self, score):
        self._score = score