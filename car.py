from math import radians, sin, cos

class Car:
    """Car class
    Args:
    self(Car) is the intance of the class
    x is the starting x coordinate of the car; default float value is 0
    y is is the starting x coordinate of the car; default float value is 0
    heading is the start heading; defulat float value is 0"""
    
    """Side Effects:
   All parameter values change as the car's location changes"""
    def __init__(self , x = 0.0 ,  y = 0.0, heading = 0.0):
        self.x = x
        self.y = y
        self.heading = heading
        """Args:
        Degrees is the number of degrees the car is moving"""
    def turn(self , degrees):
        self.heading = (self.heading + degrees) % 360
            
    def drive(self , distance):
        """Drives the car 
        Args: 
        self(drive): instance of the car class
        distance is the amount of movement the car"""
        f = radians(self.heading)
        self.x += distance * sin(f) 
        self.y -= distance * cos(f)       
def sanity_check():
    """Shows the location of the car
    
    Return:
    My.Tesla is how I track how far and wide my car class moves"""
    myTesla = Car()
    myTesla.turn(90)
    myTesla.drive(10)
    myTesla.turn(30)
    myTesla.drive(20)
    print(f"""Location : {myTesla.x},{myTesla.y})\n""" 
          f""" Heading : {myTesla.heading}.""")
    return myTesla

if __name__ == "__main__":
    sanity_check() 