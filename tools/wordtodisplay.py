
def wordToDisplay(word, checkedletters):
    wordToDisplay = ""
    for templetter in list(word):
        if templetter in checkedletters:
            wordToDisplay += templetter
        else:
            wordToDisplay += '_'
    return wordToDisplay