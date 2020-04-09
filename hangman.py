import random

movies = ['the godfather', 'back to the future', 'rocky', 'die hard', 'mad max', 'raging bull', 'ghostbusters', 'dick tracy', 'batman', 'home alone']
books = ['the lord of the rings', 'harry potter', 'the bible', 'the little prince', 'the alchemist', 'the davinci code', 'the stranger', 'the pilgrim', 'the pelican brief', 'the secret']
world_cities = ['london', 'paris', 'new york', 'mexico city', 'berlin', 'madrid', 'los angeles', 'rio de janeiro', 'dubai', 'milan']
body_parts = ['head', 'nose', 'arms', 'fingers', 'nails', 'eyes', 'feet', 'legs', 'chest', 'ears']
celebrities = ['leonardo dicaprio', 'jennifer aniston', 'brad pitt', 'charlize theron', 'nicole kidman', 'ana de armas', 'al pacino', 'robert deniro', 'johnny deep', 'bradley copper', 'jennifer lawrence']
categories = [movies, books, world_cities, body_parts, celebrities]

print("Categories are [0] Movies, [1] Books, [2] World Cities, [3] Body Parts, [4] Celereties")
choose_category = (int(input("Please Choose a Category: ")))
print("CAUTION! SPACEBAR counts as part of the WORD")

randomword = ""
hidden_word = ""

def startGame(choose_category):
	global hidden_word, randomword
	for i, c in enumerate(categories, 0):
		if i == choose_category:
			randomword = random.choice(c)
			for letter in randomword:	
				hidden_word += letter.replace(letter, '*')
			return print(hidden_word)
			
def hangmanPlay(randomword):
	global hidden_word
	user_chances = 10
	user_inputs = []
	while user_chances != 0:
		user_guesses = str(input("Introduce a Letter: "))
		if user_guesses not in randomword:
			user_chances -= 1
			print("Letter", user_guesses.upper(), "is not in the word we are looking for...")
			print("You only have", user_chances, "to go")
			print(hidden_word)
			if user_chances == 0:
				print('The word was:', randomword.upper())
			continue
		if user_guesses in randomword:
			print("You got it right", user_guesses.capitalize(), "is", randomword.count(user_guesses), "time(s) in the word")
	
		if user_guesses == randomword:
			print("You've Won")
			print(randomword.upper(), 'is the match')
			break

startGame(choose_category)	
hangmanPlay(randomword)

