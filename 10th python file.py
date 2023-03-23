import json
from difflib import get_close_matches
data = json.load(open("https://raw.githubusercontent.com/ck12python/English-Dictionary/main/dictionary.json"))
def translate(w):
    w = w.lower()
    if w in data:
        return data (w)
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you maen % s instead? Enter Y if yes, enter N if no: " % get_close_matches(w, data.keys())[0])
        yn = yn.lower()
        if yn == "y":
            return data(get_close_matches(w, data.keys())[0])
        elif yn == "n":
            return "The word does not exist. Please double check it."
        else:
            return "We didnt understand your entery"
    else:
        return "The word does not exist. Please double check it."

word = input("Enter word: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
input('Press ENTER to exit')
    
            


        