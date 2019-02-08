# CMPT 120 - Lab #6
# Joseph McDonough
# 25 October 2018
###

def showIntro():
    print("Welcome to the Arithmetic Engine!")
    print("=================================\n")
    print('Valid commands are "add", "mult", "sub", "div", "pow", and "quit".\n')

def showOutro():
    print("\nThank you for using the Arithmetic Engine…")
    print("\nPlease come back again soon!")

def doLoop():
    while True:
        cmd = input("What computation do you want to perform? ")
        cmd=cmd.strip().lower()
        if(cmd=="add" or cmd=="sub" or cmd=="mult" or cmd=="div" or cmd=="pow"):    
            try:
                num1 = int(input("Enter the first number: "))
                num2 = int(input("Enter the second number: "))
                if (cmd == "add"):
                    result = num1 + num2
                elif (cmd == "sub"):
                    result = num1 - num2
                elif (cmd == "mult"):
                    result = num1 * num2
                elif (cmd == "div"):
                    result = num1 // num2
                elif (cmd == "pow"):
                    result = num1**num2
                print("The result is " + str(result) + ".\n")
            except:
                print("Those aren't numbers. Please try again.")
                continue
        elif (cmd == "quit"):
            break
        else:
            print(cmd + " is not a valid command.")
            continue
        
def main():
    showIntro()
    doLoop()
    showOutro()

main()
