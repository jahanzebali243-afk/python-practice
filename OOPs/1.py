class Dog :
    def __init__(self , name , color , number , parents_status):
        self.name = name
        self.color = color
        self.number = number
        self.parents_status = parents_status

my_dog = Dog("Boob" , "Brown" , 67 , "alive")
print (my_dog.name , my_dog.color , my_dog.number , my_dog.parents_status)