from ctypes import sizeof


class Word:
    def __init__(self, baseWord):
        self.baseWord = baseWord.lower()
        self.actualWord = self.baseWord
        self.checkedLettersSuccess = []
        self.checkedLettersNoSuccess = []
    
    @property
    def baseWord(self):
        return self._baseWord
    
    @property
    def actualWord(self):
        return self._actualWord
    
    @property
    def len(self):
        return self._len
    
    @property
    def checkedLettersSuccess(self):
        return self._checkedLettersSuccess
    
    @property
    def checkedLettersNoSuccess(self):
        return self._checkedLettersNoSuccess
    
    @baseWord.setter
    def baseWord(self, baseWord):
        self._baseWord = baseWord
    
    @actualWord.setter
    def actualWord(self, actualWord):
        self._actualWord = actualWord
    
    @checkedLettersSuccess.setter
    def checkedLettersSuccess(self, checkedLettersSuccessList):
        self._checkedLettersSuccess = checkedLettersSuccessList
    
    @checkedLettersNoSuccess.setter
    def checkedLettersNoSuccess(self, checkedLettersNoSuccessList):
        self._checkedLettersNoSuccess = checkedLettersNoSuccessList
    
    def checkLetter(self, letter):
        word = self.baseWord
        for tempLetter in list(word):
            if letter == tempLetter:
                self.checkedLettersSuccess.append(letter)
                return True
        self.checkedLettersNoSuccess.append(letter)
        return False

    def checkWord(self, wordTried):
        word = self.baseWord
        if word == wordTried:
            return True
        return False
    
    
    
    def updateActualWord(self):
        word = self.baseWord
        checkedletters = self.checkedLettersSuccess
        wordToDisplay = ""
        for templetter in list(word):
            if templetter in checkedletters:
                wordToDisplay += templetter
            else:
                wordToDisplay += '_'
        self.actualWord = wordToDisplay
        
    
    def getWordLen(self):
        return len(self.baseWord)