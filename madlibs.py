#Joseph McDonough CMPT 120-113
#Lab 2 - Mad Libs
#9/6/18
'noun, verb, adjective, place'
def promptForWords():
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adjective = input("Enter an adjective: ")
    place = input("Enter a place: ")
   
def makeAndPrintSentence():
 print("Take your " + adjective + " " + noun + " and " + verb + " it at the " + place + "!")

def main():
	promptForWords()
	makeAndPrintSentence()


main()
    
