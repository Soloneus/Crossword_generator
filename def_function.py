from bs4 import BeautifulSoup
import requests

#word = input()

def def_word(word):
    url = "https://www.britannica.com/dictionary/" + word

    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")

    first_def = doc.find_all(class_ = "def_text")
    second_def  = doc.find_all(class_ = "un_text")
    if (len(first_def) == 0):
        if (len(second_def) == 0):
            return 1 #erorr
        else:
            first_def = doc.find_all(class_ = "un_text") #klasa inna
    # czasami złą definicję zwraca [0] bo dodane jest coś na poczatku
    if len(first_def[0].text) < 10:
        definition = first_def[1].text
    else:
        definition = first_def[0].text
    return definition

#print(def_word(word))

