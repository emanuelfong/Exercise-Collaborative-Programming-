class Robot:
    """Robot is the parent class"""
    def __init__(self,name):
        self.name=name
        self.hp=100
            
        def take_damage(self,amt):
                self.hp -= amt
                
                  
        def attack(self,other):
            other.take_damage(10)
                
                
class Strongbot(Robot):
    pass
    """Strongbot has inherited the methods from Robot:
    init
    attack
    take_damage"""
    def attack(self,other):
        other.take_damage(20)
    
    def take_damage(self,amt):
        super().take_damage(amt//2)
        """Super function lets you use the methods of thr parent class"""