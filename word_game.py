"""Compute a team's score for a (fictitious) word game.

In this game, two players independently find words in a matrix of letters.
Each player's words are added to a text file with one word per line. Duplicates
are removed from each player's list. For each word that appears on both players'
lists, the team's score increases by the number of letters in the word minus 2
(words less than three characters long are not worth any points).
"""


from argparse import ArgumentParser
import sys

class PlayerWords:
    """A class for my word game that adds up the characters from two similar 
    sets of words.
    Attributes:
    Words (set)- This is the player's words
    """
    def __init__(self , filepath):
        """Args:
    Filepath(string)- path to a text file
    Side Effects: The self.words = set()- We changed self to be able to 
    instantiate the class""" 
        self.words = set()
        with open(filepath, "r", encoding="utf-8")as f:
            for set in f:
                self.words.add(set.strip)
             
    def score(self , partner):
        """Args:
        Partner(Playerwords) One of the sets that I am using to score the 
        team's points
        Return:
        We return the answer which is an integer
        """
        x = self.words.intersection(partner.words)
        for word in x:
            word == len(x)
            score = len(x)- 2
            answer = 0
            if score > 0:
                answer + score
                
            return answer
            
                     
def main(filepath1 , filepath2):
    filepath1 = PlayerWords(filepath1)
    filepath2 = PlayerWords(filepath2)
print(f"Your team scored {PlayerWords}")
"""Args:
    Both filepath1 and filepath2 are paths to text files.
    Side Effects:
    The instance of my PlayerWords class creates my created printed f string 
    in my terminal"""  
    

def parse_args(arglist):
    """Parse command line arguments.
    
    Expect two mandatory arguments:
        - str: path to a text file containing words found by player 1.
        - str: path to a text file containing words found by player 2.
    
    Args:
        arglist (list of str): arguments from the command line.
    
    Returns:
        namespace: the parsed arguments, as a namespace.

    """
    parser = ArgumentParser()
    parser.add_argument("wordfile1", help="file containing player 1's words")
    parser.add_argument("wordfile2", help="file containing player 2's words")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.wordfile1, args.wordfile2)
