#Joseph McDonough
#CMPT 120L-113
#20 September 2018
#Lab 4 - Fibonacci Sequence

def fibonacciSequence(n):
    currentValue = 0
    nextValue = 1
    for x in range(n-1):
        previousValue = currentValue
        currentValue = nextValue
        nextValue += previousValue
                                                                                                 
    return nextValue

inputValue = int(input("Enter how many times you would like the Fibonacci sequence to run: "))
print("The fibonacci sequence after being ran" ,inputValue, "times, the value is" ,fibonacciSequence(inputValue))  
     
			
			
			
		
	
	 	

