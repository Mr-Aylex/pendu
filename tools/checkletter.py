
def checkLetters(letter, word):
    indexs = []
    listLetter = list(word)
    index = 0
    for templetter in listLetter:
        if letter in listLetter:
            indexs.append(index)
        i+=1
    return indexs