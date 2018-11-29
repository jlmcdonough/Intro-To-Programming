class Product:
	def __init__(self, name, price, quantity):
		self.name = name
		self.price = price
		self.quantity = quantity

	def testStock(self, checkStock):
		if(self.quantity>=checkStock):
			return True
		else:
			return False

	def findTotal(self, amount):
		totalPrice = self.price * amount
		return totalPrice
	
	def fixStock(self, amount):
		self.quantity-=amount

ultrasonicRF = Product("Ultrasonic range finder", 2.50, 4)
servoMotor = Product("Servo motor", 14.99, 10)
servoController = Product("Servo controller", 44.95, 5)
microcontroller = Product("Microcontroller Board", 34.95, 7)
laserRF = Product("Laser range finder", 149.99, 2)
lithiumPB = Product("Lithium polymer battery", 8.99, 8)

products = [ultrasonicRF, servoMotor, servoController, microcontroller, laserRF, lithiumPB]

def printStock():
    print()
    print("Available Products")
    print("------------------")
    for i in range(0,len(products)):
        if products[i.testStock(1)]:
            print(str(i)+")",products[i.name], "$", products[i.price])
    print()
    
def main():
    cash = float(input("How much money do you have? $"))
    while cash > 0:
        printStock()
        vals = input("Enter product ID and quantity you wish to buy: ").split(" ")
        if vals[0] == "quit":
            break
        prodId = int(vals[0])
        count = int(vals[1])
        if products[prodId.quantity] >= count:
            if cash >= products[prodId.price] * count:
                products[prodId.quantity] -= count
                cash -= products[prodId.price] * count
                print("You purchased", count, products[prodId.name]+".")
                print("You have $", "{0:.2f}".format(cash), "remaining.")
            else:
                print("Sorry, you cannot afford that product.")
        else:
            print("Sorry, we are sold out of", products[prodId.name])
main()
