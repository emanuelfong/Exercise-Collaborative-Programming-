import pandas as pd
import matplotlib.pyplot as plt

class PersonalityTest():
    """Class for personality test, the program will ask a series of questions for
  the user to answer : Very Inaccurate(1), Moderately Inaccurate(2),
  Neither Accurate(3), Moderately Accurate(4), or Very Accurate (5).
  It will take the sum of each trait of Extraversion, Agreeableness,
  Conscientiousness, Emotional Stability, or Neuroticism
  
  Attributes: dictofScores (Dict): A dict that holds the personality attribute 
                as keys, and the results/ sums as a value.
        dictofAnswers (dict): A dict holding the personality attributes as
            keys, and the list of answers as a value. 
    """
    def __init__(self, questiontextfilepath):
        """Will read a text file with 50 questions onto it, and using input 
            will get the writer’s answer will be added to a list of each 
                personality trait. According to the question it will be marked
                    as a negative or positive. Then at the end of the program it
                        will sum each of the lists into a singular int to get 
                            the final score for each personality.

            Agrs: pathfile (str): a txt file that holds the personality test
        """
    def personality_test(self, score):
        """Calculates what various levels/scores on the questions of the test
            mean and what the scores for user are in each personality attribute
        
        Args:
        Score - How many points the user has finished the questions with. 
            Each question will give a negative or positive change to the overall 
                score for each list.
        Returns:
        list of scores - list of scores from the user answering questions to 
            show which personality is the most acceptable.
        """
    def personality_user(self):
        """Takes the user's scores from personality_test function and returns 
            print statement. 
        Args: list of strings: the list of user inputs to quiz
        
        Returns: F string: Prints statement that says users scores for each 
            personality attribute.
        """
    def scatterPlot(self):
        """Creates a dataframe of the answers given from dictofAnswers, to plot 
        them onto a scatter plot to show the concentrations of answers in each 
        section
        
        Side Effects: Creates a plot that appears as the program is ran.
        """
        type = []
        ans = []
        for key, values in self.dictofScores.items():
            for value in values:
                type.append(key)
                ans.append(value)

        dict = {'Type': type, 'Answers': ans}

        
        df = pd.DataFrame.from_records(dict)
        plt.scatter(df['Type'], df['Answers'])
        plt.title("Result of Answers")
        plt.xlabel('Personality Types')
        plt.ylabel('Answers')
        plt.show()


class MovieSorter(PersonalityTest):
    """A class that sets up the organization of the movies that are being 
        used to recommend to the user.
    """
    def __init__(self, dictofAnswers, dictofScore, dbPathfile):
        """Creates the initialization for organizing what movies will be
        recommended.
        
        Args: dictofAnswers (dict): A dict holding the personality attributes as
                keys, and the list of answers as a value. 
            dbPathfile (str): a string that leads to a pathfile that holds a
                json file of movies and their genres and ratings.
        Side Effects: Creates a dataframe of movies in self 
        """
        self.dictofAnswers = dictofAnswers
        self.dictofScore = dictofScore
        self.dbPathfile = dbPathfile
    def topMovies(self):
        """Filters movies and return a dict of movies involving Title as key,
                and a set of (genre, ranking as a return)
        
        Return: dictofMovies (dict): A dict of movies with the titles as keys, 
            and sets of rating and genre as values.
        """
    def movie_recommend(self, dictofScores):
        """Conditional statements for possible user personality test results 
            (from the personality_user function). The logic for what scores will
                recommend what kinds of movies that are sorted in the various
                    subcategories.
        
        Args: dictofScores (Dict): A dict that holds the personality attribute 
            as keys, and the results/ sums as a value.
    """

def personality_test(self, score):
    """ Calculates what various levels/scores on the questions of the test mean
            and what the scores for user are in each personality attribute
        
        Args:
        Score - How many points the user has finished the questions with. 
            Each question will give a negative or positive change to the overall
                score for each list.
                
        Returns: list of scores - list of scores from the user answering 
                    questions to show which personality is the most acceptable.
"""

def personality_user(self):
    """Takes the user's scores from personality_test function and returns print
            statement.
    Args:
	    list of strings: the list of user inputs to quiz
    Returns:
        F string: Prints statement that says users scores for each personality
            attribute.
	
"""

if __name__ == "__main__": 
   args = parse_args(sys.argv[1:])