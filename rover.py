#Joseph McDonough CMPT 120L-113
#September 6 2018
#rover.py

def main():
	distance = eval(input("How far is the light travelling? Just provide the number in miles. "))
speedOfLight = 186000 #in miles
time = distance / speedOfLight
#time = 34000000/186000
print("It would take ", time, " seconds for the Mars Curiosity rocer to send photos from Mars to Earth") 

main()

