"""
    The Function fastest_cars takes a list of cars as an argument and returns the fastets
    vehicle from the group.
"""
class Cars :
    def __init__(self, make: str, top_speed: int) :
        self.make = make
        self.top_speed = top_speed


# function to find the fastes car
def fastest_car(car : list) :
    speed = 0
    model = None
    for item in car :
        swift = item.top_speed
        if swift > speed :
            speed = swift
            model = item.make
        if speed > swift :
            print(model)


if __name__ == '__main__' :
    car1 = Cars('Nissan', 180)
    car2 = Cars('Volkwagen', 240)
    car3 = Cars('Corrolla', 190)
    my_cars = [car1, car2, car3]
    fastest_car(my_cars)