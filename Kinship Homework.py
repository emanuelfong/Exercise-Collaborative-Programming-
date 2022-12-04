import argparse 
import json
import relationships
import sys

class Person:
    """Gives a identity to the people we want to see if they have a relationship
    with each other.
    """
    def __init__(self,name,gender,parents,spouse):
        """Gives the attributes for the Person class
        
        Args:
        name- name of the person
        gender- gender of the person
        parents- who the parents of the person is
        spouse- who the spouse of the person is
        
        """
        self.name = name
        self.gender = gender
        self.parents = list()
        self.spouse = None
        
    def add_parent(self,parents):
        self.parents.append(parents)
        
    def set_spouse(self,spouse): 
        self.spouse = spouse
        
    def connections(self):
        """To identify connections to relatives who might be lowesr common relatives
        
        
        Returns:
        cdict- dictionary of connections that follows parent and spouse connections
        """
        cdict = {self:""}
        queue1 = [self]
        
        while len(queue1) !=0:
            person = (queue1.pop(0))
            personpath = {cdict[person] :person}
            
        for parents in person.parents:
            if parents not in cdict:
                x=cdict[person.parents]= personpath + "P"
                queue1.append(x)
            elif "S" not in personpath.values() and person.spouse == True and person.spouse not in cdict.keys():
                y = cdict[self.spouse] = personpath + "S"
                queue1.append(y)
                return cdict
    
    def relation_to(self):
        """
        
        """
        x = Person()
        
        person1 = self.connections
        person2 = self.connections
        
        
        
        
class Family():
    """Keeps tracks of all the person instances created.
    """
    def __init__(self,people):
        """Creates the instance of the Family class "people"
        Args:
        people- a dictionary where each key os the name of the person and each 
        value is a object
        
        """
        self.people = {"individuals": Person.name:x.gender
                       "parents": {x.name:x.addparent}
                       "couples": {x.name:x.set_spouse}
                       } 
        
        
    def relation(self,name1,name2):
        """
        
        Args:
        name1-name of first person
        name2- name of second person
        
        Returns:
        If there is a kinship relationship between the objects as an outcome
        """
        name1 = Person()
        name2 = Person()
        
        
        if name1.relation_to(name2) if False:
            return None
        elif name1.relation_to(name2) is relationships.relationships.keys():
            return name1.relation_to(name2)
        
    def main(filepath,name1,name2):
        """Reads the family file to see if there is a relationship between the 
        two people and returns an output of the outcome
        
        Args:
        filepath- path to family file
        name1- name of first person
        name2- name of the second person
        
        """
        
        with open(filepath,"r",encoding="utf-8") as f:
            familydata=json.load(f)
            
            x= Family(familydata)
            
            if x.relation(name1,name2) is None:
                print(f"{name1} is not related to {name2}")
            else:
                print(f"{name1} is {name2}'s {x.relation(name1,name2)}")
                
                
def parse_args(arglist):
    """
    Parses the command line arguments
    
    Args:
    filepath- path to family file
    name1- name of first person
    name2- name of second person
    
    Attributes:
    Arglist- arguments from command line
    
    Returns:
    namespace object- parsed arguments as namespace objects
    Side Effects:
    The parsed arguments are chnaged into objects to parse through
    """
    
    
    parser = argparse.ArgumentParser()
    parser.add_argument("filepath", help = "family file")
    parser.add_argument("name1", help="name of first person object")
    parser.add_argument("name2", help= "name of second person object")
    
    return parser.parse_args(arglist)

if __name__=="__main__":
    args = parse_args(sys.argv[1:])
    main(args.filepath,args.name1, args.name2)
            