#Joseph McDonough
#CMPT 120L-113
#Lab 4 pi.py

import math
n = int(input("Enter to how many decimal places you want pi to go: "))
global answer
answer = 4
denominator = 3	
for x in range(n):
	if(x%2==0):
		answer-= 4/denominator
	else:
		answer+=4/denominator
	denominator+=2

print(answer)
print(math.pi)

 
