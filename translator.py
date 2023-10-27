#vowles ->g

def translate(phrase):
    tranlation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                tranlation = tranlation + "G"
            else:
             tranlation=tranlation+"g"
        else:
            tranlation=tranlation+letter
    return tranlation

print(translate(input("enter the sentence:  ")))
