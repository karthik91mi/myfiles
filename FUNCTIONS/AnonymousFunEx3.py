#Program for finding Wthether the word is vowel or not
#AnonymousFunEx3.py
vowel=lambda word: "Vowel Word" if 'a' in word.lower() or 'e' in word.lower() or 'i' in word.lower()  or 'o' in word.lower() or 'u' in word.lower() else "NOT Vowel Word"

#main progra
word=input("Enter word:")
res=vowel(word)
print("{} is {}".format(word,res))