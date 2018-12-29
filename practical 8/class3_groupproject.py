"""
Create the following classes:
1. Pokemon: that has attributes of name, power (100 as default value). methods attack()
2. Electric: inherits from Pokemon
    - attack(): if attack Electric -> no change in power
                if attack Fire -> Electric increases power by 1
3. Fire: inherits from Pokemon
    - attack(): if attack Fire -> no change in power
                 if attack Electric -> Fire decrease power by 1
4. test program that initialise 1 Pikachu (of type Electric), 1 charmander (of type Fire)
    - randomly generate 10 attacks from from any of the character.
    - display the final power.
"""

class Pokemon():
    def __init__(self, name ="", power = 100,type = ""):
        self.name = name
        self.power = power
        self.type = type
    def __str__(self):
        return "I am {} power{} of {}".format(self.name,self.power,self.type)

    def attack(self,other):
        #isinstance (other,pokemon)
        print("attacking ....")
        return self.__str__()

"""
class Electric(Pokemon):
    def __init__(self,name ="",power =100,type =""):
        super().__init__(name,power,type)

    def attack1(self):
        if self.type =="Fire":
            self.power = self.power+ 1
        elif self.type == "Electric":
            self.power = self.power

class Fire(Pokemon):
    def __init__(self,name ="",power =100,type =""):
        super().__init__(name,power,type)

    def attack2(self):
        if self.type =="Fire":
            self.power = self.power
        elif self.type == "Electric":
            self.power = self.power - 1


pikachu = Electric("Pikachu",100,"Electric")
charmander = Fire("charmander",100,"Fire")

list =[pikachu,charmander]

"""


class Electric(Pokemon):
    def attack(self,other):
        if isinstance(other,Fire):
            self.power +=1
        return self.__str__()

class Fire(Pokemon):
    def attack2(self,other):
        if isinstance(other,Electric):
            self.power -=1
        return self.__str__()



pikachu = Electric("Pikachu",100,"Electric")
charmander = Fire("charmander",100,"Fire")

list =[pikachu,charmander]

import random


for i in range(10):
    rand = random.randrange(0,2)
    if rand == 0:
        print(list[0].attack(list[1]))
    else:
        print(list[1].attack2(list[0]))



