
def checkLetters(letter, word):
    dictio = {}
    listLetter = list(word)
    index = 0
    for templetter in listLetter:
        if letter in listLetter:
            dictio[letter] = index
        i+=1
    return dictio