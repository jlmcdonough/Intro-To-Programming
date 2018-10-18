def main():
    print("PYTHON GUESSING GAME.")
    animalName = "lion"
    userInput=""    
    guess=""
    while True:  #instructions state test is always true
        print("I am thinking of an animal.")        
        userInput = str(input("Enter your guess: "))
        guess = userInput.strip().lower()
        if(guess==animalName):
            print("You guessed correct! Congratulations!")
            break
        else:
            print("You guess was wrong please try again.")

main()
