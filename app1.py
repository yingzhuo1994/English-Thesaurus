import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        # proper noun search
        # title() method will convert the first letter to uppercase and the rest to lowercase. 
        return data[w.title()]
    elif w.upper() in data:
        # acronym search
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        close_match = get_close_matches(w, data.keys())[0]
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % close_match)
        if yn == "Y":
            return close_match
        elif yn == "N":
            return "The word doesn't exit. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
