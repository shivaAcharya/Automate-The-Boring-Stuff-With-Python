# English to Pig Latin
print('Enter English message to covert to Pig Latin: ')

message = input()

Vowels = ['a', 'e', 'i', 'o', 'u']

pigLatin = []

for word in message.split():

    #Separate Nonletters at the front of the word.
    prefixNonletters = ''

    while len(word) > 0 and not word[0].isalpha():
        prefixNonletters += word[0]
        word = word[1:]

    if len(word) == 0:
        pigLatin.append(prefixNonletters)
        continue

    #Separate Nonletters at the end of the word.
    suffixNonletters = ''

    while len(word) > 0 and not word[-1].isalpha():
        suffixNonletters += word[-1]
        word = word[:-1]


    wasUpper = word.isupper()
    wasTitle = word.istitle()

    #Convert all words to lower case

    word = word.lower()

    #Work with words that start with consonent letters.

    prefixConsonants = ''
    while len(word) > 0 and not word[0] in Vowels:
        prefixConsonants += word[0]
        word = word[1:]

    if prefixConsonants != '':
        word += prefixConsonants + 'ay'

    else:
        word += 'yay'

    if wasUpper:
        word = word.upper()

    if wasTitle:
        word = word.title()


    pigLatin.append(prefixNonletters + word + suffixNonletters)

print(' '.join(pigLatin))












