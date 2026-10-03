#Make a class Person with name and age. Then make Teacher(Person) that adds a subject attribute and a method teach() that prints "X teaches Y". Use super().__init__().

class Person :
    def __init__(self , name , age):
        self.name = name
        self.age = age
class teacher (Person) :
    def __init__(self, name, teach):
        super().__init__(name, teach)
        self.name = name
        self.teach = teach

t1 = teacher("Jahanzeb" , "Math")
print (f"{t1.name} teaches {t1.teach}" )

