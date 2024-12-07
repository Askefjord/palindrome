palWord = input('Enter word: ')
palWord.lower()

if palWord == palWord[::-1]:
    print('Your word is palindrom!:', palWord)
else:
    print("This isn't palindrome. Let's try again")