def main():
    print("PYTHON GUESSING GAME.")
    animalName = "lion"
    userInput=""    
    guess=""
    doYouLike = ""
    while True:  #instructions state test is always true
        print("I am thinking of an animal.")        
        userInput = str(input("Enter your guess: "))
        guess = userInput.strip().lower()
        if(guess==animalName):
            print("You guessed correct! Congratulations!")
            doYouLike = str(input("Do you like this animal (Y/N): "))
            yOrN = doYouLike.lower().strip()
            if(yOrN=="y"):
                print("I'm glad I picked something you liked.")
            else:
                print("Sorry to hear, maybe you will like the next one.")
            break
        elif(guess[0]=="q"):
            break
        else:
            print("You guess was wrong please try again.")

main()
