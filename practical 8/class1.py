
class Fruit:
    __secretVar = 50 #hidden variable that can only accessed within the same class

    def __init__(self,name, calorie):
        self.calorie = calorie #instance attribute
        self.name = name

    def __str__(self):
        return "This is fruit{} with calories {}".format(self.name,self.calorie )

    def isHighCalories(self):
        if self.calorie > 100 :
            return True
        else:
            return False



    def revealSecret(self):
        print(self.__secretVar)


class AsianFruit(Fruit):
    def __init__(self,name,calorie):
        super().__init__(name,calorie) #follow the init() from superclass

    def isHighCalories(self): #overriding chuyen huong , under the condition that name, input, return must be the same as super
        if self.calorie > 80:
            return True
        else:
            return False



"""
oop, two very important relationship
1. is a relationship( AsianFruit is a Fruit ---> inheritance)
2. has-a relationship(Fruit has a calories ----> composition)
"""

# Polymorph
fruit = [Fruit("Rockmelon",60), AsianFruit("Durian",70)]




kiwi = Fruit("Kiwi",38)
#print(kiwi.calorie)
#kiwi.revealSecret()
print(kiwi)

fruit.append(kiwi)
print(fruit)
for each in fruit:
    print(each.isHighCalories())#polymorphism, dynamic binding