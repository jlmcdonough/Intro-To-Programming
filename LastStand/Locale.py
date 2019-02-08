#Locale class
from random import randint

class Locale():

    def __init__(self, name, description, chance1, chance2):
        self.name = name
        self.description = description
        self.chance = int(randint(chance1,chance2))
        self.item = None
        self.hasBeen = False
        self.uses = 0

    def addItem(self,itemName, uses):
        self.item = itemName #want to set item by default to None, this adds items to locales that have them
        self.uses=uses

    def updateDescription(self,description):
        self.description = description
        



