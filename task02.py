class Students:
    def __init__(self, name, age, kursi):
        self.name = name
        self.age = age
        self.kursi = kursi

    def introduce(self):
        return f"My name is {self.name} I am {self.age} studying in {self.kursi} course"
    
student = Students("Artur", 20, 3)
print(student.introduce())   
