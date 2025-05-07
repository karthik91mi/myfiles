#Programing for accepting a word amd decide wehether It is Vowel word or not.
#IfElseEx2.py
word=input("Enterv a Word:")
if('a'in word.lower() or 'e'in word.lower() or 'i'in word.lower() or 'o' in word.lower() or 'u' in word.lower()):
    print("{} is Vowel Word".format(word))
else:
    print("{} is not Vowel Word".format(word))


