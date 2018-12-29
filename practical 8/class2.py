"""
creat the following clas:
Student - derived from person
also has student_id

Musician - derived from person
also has play(text)

"""

class Person():
    def __init__(self,name = "",age = 0):
        self.name = name
        self.age = age

    def __str__(self):
        return "{} class {} age".format(self.name,self.age)

    def __add__(self, other):
        return "{} and {}".format(self.name,other.name)
    def __eq__(self, other):
        if self.name == other.name:
            return True
        else:
            False

class Student(Person):
    def __init__(self,name ="",age =0,student_id = 0):
        super().__init__(name,age)
        self.student_id = student_id


class Musicaian(Person):
    def play(self,text):
        print("Playing{}".format(text))


john = Student("Mozart",20,112345)
mozaer = Musicaian("Mozart",60)

print(john)
print(mozaer)

print(isinstance(john,Musicaian))# check type of variable


x = 10 + 5
print(x)

y = "abc"+ "def"
print(y)

z = john + mozaer
print(z)

print(john == mozaer)