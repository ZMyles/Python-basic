
# parent class
class Organism:
    name = "Unknown"
    species = "Unknown"
    legs = None
    arms = None
    dna = "Sequence A"
    origin = "Unkown"
    carbon_based = True

    def information(self):
        msg = "\nName: ()\n Species: {} \n Legs: {} \n Arms: {} \n DNA: {} Origin: {} \nCarbon Based: {}".format(self.name,self.legs,self.arms,self.dna,self.origin,self.carbon_based)
        print(msg)

        
#child class instance
class Human(Organism):
    name = "Pete"
    speices= "bird"
    legs= 2
    arms = 2
    origin = 'Earth'

    def ingenuity(self):
        msg = "Life is pain, \n So is death..."
        return msg

class Dog(Organism):
    name= "Doggo"
    species = "dog"
    legs = 2
    arms = 2
    dna = "Sequnce Aplha"
    origin = 'Mars'

    def bite(self):
        msg = "\n them teeth sharp!|"
        return msg
        
if __name__ == "__main__":
    human = Human()
    print(human.information())
    print(human.ingenutiy())

    dog = Dog()
    print(dog.information())
    print(dog.bite())
     
