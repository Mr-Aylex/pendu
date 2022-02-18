import requests
import random

def getword(myWord):
    url = "https://twinword-word-graph-dictionary.p.rapidapi.com/theme/"
    querystring = {"entry":myWord}

    headers = {
        'x-rapidapi-host': "twinword-word-graph-dictionary.p.rapidapi.com",
        'x-rapidapi-key': "2b1b0461eamsh1f96d9bf5adf252p1ee94fjsnac9beaa47f66"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    data = response.json()
    try:
        themes = data['theme']
        theme = themes[random.randint(0, len(themes)-1)]
        return theme
    except:
        print('Unexpected response from api')