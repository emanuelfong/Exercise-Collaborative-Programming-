class Dog:
    """An abstration of a dog.
    
    Attributes:
    name(str):dog's name
    breed(str):dog's breed
    age(int):dog's age in years
    """
    def __init__(self, name, breed, age):
        """Initializes a new dog Object.
       
       Args:
       (Never put "self") 
    name(str):dog's name
    breed(str):dog's breed
    age(int):dog's age in years 
       
        Side effects:
            Set attributes name, breed, and age
        """ 
        self.name = name
        self.breed = breed
        self.age = age
    
    def bark(self, dog2=None):
        """Communicate like a dog.
        Args:
        dog2(Dog,optional): another dog. Default: None
        
        Side Effects:
        Writes to stdout"""
        if dog2 == None:
            print(f"I'm {self.name} and I'm a dog.")
        else:
            print(f"Hey, {dog2.name}, how's it going?")

