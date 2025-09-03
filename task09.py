class Temprature:
    def __init__(self, celsius):
        self.celsius = celsius


    @property
    def celsius(self):
        return self.celsius   
    
    @property
    def fahrenheit(self):
        return (self.celsius * 9/5) + 32
    
temp = Temprature(0)

print(temp.celsius)
print(temp.fahrenheit)
