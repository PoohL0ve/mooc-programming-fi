
class Computer :
    """ The model class for creating simple computers """
    def __init__(self, model: str, speed: int) :
        self.model = model
        self.speed = speed

class LaptopComputer(Computer) :
    def __init__(self, model:str, speed:int, weigth: int) :
        super().__init__(model, speed)
        self.weigth = weigth 
    
    # string to be returned
    def __str__(self) :
        return f"{self.model}, {self.speed}MHz, {self.weigth}lbs"
    
# test for class implentation
my_notebook = LaptopComputer("Air Mac Pro 2", 2000, 5)
print(my_notebook)