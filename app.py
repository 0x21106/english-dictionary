import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys(), cutoff = 0.8)) > 0:
        if(word == get_close_matches(word, data.keys(), cutoff = 0.8)[0]):
            return data[word]
        else:
            yn = input(f"Did you mean \"{get_close_matches(word, data.keys(), cutoff = 0.8)[0]}\" instead? Enter Y if yes, or N if no: ")
            if yn.upper().replace(" ", "") == "Y":
                return data[get_close_matches(word, data.keys(), cutoff = 0.8)[0]]
            elif yn.upper().replace(" ", "") == "N":
                return "The word doesn't exist. Please double check it."
            else:
                return f"I don't understand your entry: \"{yn}\""
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter word: ")

output = translate(word)

if isinstance(output, list):
    for item in output:
        print(item)
else:
    print(output)