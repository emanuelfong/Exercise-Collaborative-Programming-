from argparse import ArgumentParser
import re
import sys

class Address:
    def __init__(self, address, house_number,street,city,state,zip):
        """
        Takes a single line of texts as an argument and sets the attributes
        
        Args: 
        address: str
        the address as a string
        house_number: str
        house number as a string
        city : str
        city name as a string
        street: str
        street name as a string
        state: str
        state name as a string
        zip: str
        zip code as a string
        """
        self.address = "address"
        self.house_number = "house_number"
        self.street = "street"
        self.city = "city"
        self.state = "state"
        self.zip = "zip"
        x = r'''(?xm)
        ^(?P<HouseNum>\S+)
        \s
        (?P<Streets>[^,]+)
        ,\s
        (?P<City>(?:\w{3,}\s?)+)
        \s
        (?P<State>[A-Z]{2})
        \s
        (?P<ZipCode>\d{5})'''
        
        self.address = address
        
        match = re.search(x, self.address)
        
        if match == None:
            raise ValueError("The address string could not be pasrsed.")
        
        else:
            self.house_number = match.group(1)
            self.street = match.group(2)
            self.city = match.group(3)
            self.state = match.group(4)
            self.zip = match.group(5)

    def __repr__(self):
    
        return(
            f"address:      {self.address}\n"
            f"house number  {self.house_number}\n"
            f"street        {self.street}\n"
            f"city          {self.city}\n"
            f"state         {self.state}\n"
            f"zip           {self.state}\n"
    )
        
def read_addresses(filepath):
    """Reads addreses and returns list with one instance of Address per line 
    
    Args: 
    filepath: textfile"""
    address_list = []
    with open(filepath) as file:
        for line in file:
            address_list = Address(list) 
    
    

def parse_args(arglist):
    """ Parse command-line arguments.
    
    Expect one mandatory argument, the path to a file of addresses.
    
    Args:
        arglist (list of str): command-line arguments.
    
    Returns:
        namespace: an object with one attribute, file, containing a string.
    """
    parser = ArgumentParser()
    parser.add_argument("file", help="file containing one address per line")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    for address in read_addresses(args.file):
        # the !r tells the f-string to use the __repr__() method to generate
        # a string version of the address object
        print(f"{address!r}\n")
