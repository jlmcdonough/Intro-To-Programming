#Joseph McDonough
#CMPT 120L-113
#20 September 2018
#Lab 4 - Fibonacci Sequence

def fibonacciSequence(n):
	currentValue = 1
	previousValue = 1
	global nextValue
	#nextValue = 2
	if(n>2):	
		for x in range(n-2):
			nextValue = currentValue+previousValue
			currentValue=previousValue
			#x++
	else:
		return 1
	return nextValue


inputValue = input("Enter how many times you would like the Fibonacci sequence to run: ")
print("The fibonacci sequence after being ran " + inputValue + " times, the value is " + fibonacciSequence(inputValue))  

			
			
			
		
	
	 	

