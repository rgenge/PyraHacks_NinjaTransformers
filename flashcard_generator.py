from posixpath import split
import numpy as np

class flashcard:
	def __init__(card, term, meaning):
		card.term = term
		card.meaning = meaning
	def __str__(card):
		return card.term+' ( '+card.meaning+' )'

cards = []

print("Let's begin creating your flashcards!")

while(True):
    term = input("enter a term: ")
    meaning = input("enter the term's meaning: ")
    Input = input("press any key to add a flashcard, or 1 to print: ")
    cards.append(flashcard(term, meaning))
    if Input == "1":
        break

# printing flashcards
print("Here are your flashcards:")
for i in cards:
	print(i)
    
save = input("press s to save cards into a .txt file, or any other key to exit: ")
if save == "s":
    np.savetxt("flashcards.txt", cards, fmt="%s")
    print("Your file has been saved to your device, it is called flashcards.txt!")
else:
    exit