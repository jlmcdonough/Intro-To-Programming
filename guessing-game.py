def main():
	print("PYTHON GUESSING GAME.")
	animalName = "lion"
	guess=""	
	guessNorm=""
	while True:  #instructions state test is always true
		print("I am thinking of an animal.")		
		guess=str(input("Enter your guess: ")
		guessNorm=guess.strip().lower()
		if(guessNorm==animalName):
			print("You guessed correct! Congratulations!")
			break
		else:
			print("You guess was wrong please try again.")

main()
		
		
