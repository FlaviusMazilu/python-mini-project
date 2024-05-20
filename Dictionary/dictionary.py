"""docstring here"""
import json
from difflib import get_close_matches
DATA = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in DATA:
        return DATA[word]
    if word.title() in DATA:
        return DATA[word.title()]
    if word.upper() in DATA:
        return DATA[word.upper()]
    if len(get_close_matches(word, DATA.keys())) > 0:
        print("did you mean %s instead" %get_close_matches(word, DATA.keys())[0])
        decide = input("press y for yes or n for no: ")
        if decide == "y":
            return DATA[get_close_matches(word, DATA.keys())[0]]
        if decide == "n":
            return "pugger your paw steps on working keys "

        return "You have entered wrong input please enter just y or n"

    return print("You have entered wrong keys. Try again")


WORD = input("Enter the word you want to search: ")
OUTPUT = translate(WORD)
if isinstance(OUTPUT, list.__class__):
    for item in OUTPUT:
        print(item)
else:
    print(OUTPUT)
