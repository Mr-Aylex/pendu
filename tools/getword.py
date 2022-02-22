import requests
import random

def getword(theme):
    url = "https://twinword-word-graph-dictionary.p.rapidapi.com/theme/"
    querystring = {"entry":theme}

    headers = {
        'x-rapidapi-host': "twinword-word-graph-dictionary.p.rapidapi.com",
        'x-rapidapi-key': "2b1b0461eamsh1f96d9bf5adf252p1ee94fjsnac9beaa47f66"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    data = response.json()
    try:
        words = data['theme']
        word = words[random.randint(0, len(words)-1)]
        return word
    except:
        print('Unexpected response from api')