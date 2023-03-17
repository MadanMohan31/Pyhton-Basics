# This code is designed to translate particular value

# Ex: vowels can be converted into #

def translator(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            if letter.isupper():
                translation = translation + "^*"
            else:
                translation = translation + "*"
                
        else:
            translation = translation + letter
    return translation

print(translator(input("Enter the Phrase : ")))
