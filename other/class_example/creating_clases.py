from tire import Tire

class Car:
    """
    Car models a car w/ tires and an engine
    my_car = Car()
    """

    def __init__(self, engine, tires):
        self.engine = engine
        self.tires = tires
    
    def description(self):
        return f"A car with an {self.engine} engine, and {self.tires} tires"
    
    def wheel_circumference(self):
        if len(self.tires) > 0:
            return self.tires[0].circumference()
        else:
            return 0
        
