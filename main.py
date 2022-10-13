import random
from english_words import english_words_set

words = [*english_words_set]
score = 0

chosenWord = random.choice(words)

wordLength = len(chosenWord)
userWord = ["_"]*wordLength

print(" ".join(userWord))

while "".join(userWord) != chosenWord:
  userGuess = input("Guess a letter: ")
  userGuess = userGuess[0]

  if userGuess in chosenWord:
    for i in range(wordLength):
      if userGuess == chosenWord[i]:
        userWord[i] = userGuess
  
  print(" ".join(userWord))  
  score -= 1
  if "".join(userWord) == chosenWord:
    score += wordLength
    print("you win")
    print("your score is: "+str(score))
