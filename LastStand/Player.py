#Player class
from random import randint

class Player():

    def __init__(self, userName, userGender):
        #Stuff that I had in each player class
        self.name = userName
        self.gender = userGender
        self.title = ""
        self.passion = ""
        self.college = ""
        self.tempJob = ""
        self.role = ""
        #user dictionary from game now in constructor
        self.score = 0
        self.inventory = []
        self.movesMade = 0
        self.locationName = ""
        self.locationDescription = ""
        self.injured = False

    def display(self):
        print("1) Soldier - good gun skills but struggles to make nutritious foods")
        print("2) Doctor - can make meaningful medicine from very little, yet cannot shoot a gun well")
        print("3) Chef - is excellent at making substantial food, but has difficulties making proper clothes")
        print("4) Tailor - can make the necessary clothes to survival the cold but doesn't know how to manage his meds")

    def assignRole(self, roleChosen):
        if (roleChosen == 1):
            self.role = "Soldier"
            self.title = "Corporal " + self.name
            self.passion = "weapons and defending those who cannot themselves"
            self.college = "the Citadel in South Carolina"
            self.tempJob = "for the London Police Department,"
        elif (roleChosen == 2):
            self.role = "Doctor"
            self.title = "Dr. " + self.name
            self.passion = "medicine and helping those who were sick"
            self.college = "Johns Hopkins University in Maryland"
            self.tempJob = "multiple jobs"
        elif (roleChosen == 3):
            self.role = "Chef"
            self.title = "Chef " + self.name
            self.passion = "cooking and using your imagination"
            self.college = "the Culinary Institute of America in New York"
            self.tempJob = "as the head chef in a fairly big restaurant"
        else:
            self.role = "Tailor"
            self.title  = self.name + " the Tailor"
            self.passion = "creating art with your clothes"
            self.college = "Marist College in New York"
            self.tempJob = "as a cashier at Matches Fashion"
        
    def welcome(self):
        print("\nWelcome to your new life " + self.title + ". GOOD LUCK!\n")
