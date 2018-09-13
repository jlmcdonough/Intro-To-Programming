#Joseph McDonough CMPT 120-113
#Lab 2 - Mad Libs
#9/6/18

def promptForWords():
	global noun = input("Enter a noun: ")
	global verb = input("Enter a verb: ")
	global adjective = input("Enter an adjective: ")
	global place = input("Enter a place: ")
   
def makeAndPrintSentence():
 print("Take your " + adjective + " " + noun + " and " + verb + " it at the " + place + "!")

def main():
	promptForWords()
	makeAndPrintSentence()

main()
    
