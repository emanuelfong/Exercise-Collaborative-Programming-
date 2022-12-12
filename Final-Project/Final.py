import pandas as pd
import matplotlib.pyplot as plt
from argparse import ArgumentParser
import sys

class PersonalityTest():
    """Class for personality test, the program will ask a series of questions 
        for the user to answer : Very Inaccurate(1), Moderately Inaccurate(2),
            Neither Accurate(3), Moderately Accurate(4), or Very Accurate (5).
                It will take the sum of each trait of Extraversion, 
                    Agreeableness, Conscientiousness, Emotional Stability, or 
                        Neuroticism
    Attributes: 
        dictofScores (Dict): A dict that holds the personality attribute 
            as keys, and the results/ sums as a value. 
        dictofAnswers (dict): A dict holding the personality attributes as
            keys, and the list of answers as a value. 
    """
    def __init__(self):
        """Will read a text file with 50 questions onto it, and using input 
            will get the writer’s answer will be added to a list of each 
                personality trait. According to the question it will be marked
                    as a negative or positive. Then at the end of the program it
                        will sum each of the lists into a singular int to get 
                            the final score for each personality.

            Agrs: pathfile (str): a txt file that holds the personality test
        """
        E = []
        A = []
        C = []
        ES = []
        I = []
                
        with open ('Final-Project\PersonalityTest.txt', "r", encoding = "utf-8") as f:
            for line in f:
                ans = 0
                question = line.split(",")[0]
                add_or_sub = line.split("," ,2)[1]
                personality =  line.split("," ,2)[2]
                ans = input(f"{question} ")
                ans = int(ans)
                #Needs to make sure it is an int.
                if personality == 'E':
                    if add_or_sub == "+":
                        E.append(ans)
                    elif add_or_sub == "-":
                        E.append(ans)
                elif personality == 'A':
                    if add_or_sub == "+":
                        A.append(ans)
                    elif add_or_sub == "-":
                        A.append(ans)
                elif personality == 'C':
                    if add_or_sub == "+":
                        C.append(ans)
                    elif add_or_sub == "-":
                        C.append(ans)
                elif personality == 'ES':
                    if add_or_sub == "+":
                        ES.append(ans)
                    elif add_or_sub == "-":
                        ES.append(ans)
                elif personality == 'I':
                    if add_or_sub == "+":
                        I.append(ans)
                    elif add_or_sub == "-":
                        I.append(ans)
                    
            
        dictofAnswers = {'Extraversion': E, 'Agreeableness': A, 
                        'Conscientiousness' : C, 'Emotional Stability': ES, 
                        "Intellect": I}
                
        dictofScores = {'Extraversion': sum(E), 'Agreeableness': sum(A), 
                        'Conscientiousness' : sum(C), 'Emotional Stability': sum(ES), 
                        "Intellect": sum(I)}
    
    def personality_test(self):
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
        #This is not completed, still need to use lamaba/ custom sorting.
        personality = max(self.dictofScores,key=lambda x: self.dictofScores[x])
        
        return personality
        
        
    def personality_user(self):
        """Takes the user's scores from personality_test function and returns 
            print statement. 
        Args: list of strings: the list of user inputs to quiz
        
        Returns: F string: Prints statement that says users scores for each 
            personality attribute.
            
        """
        extra = self.dictofScores['Extraversion']
        agree = self.dictofScores['Agreeableness']
        con = self.dictofScores['Conscientiousness']
        emo = self.dictofScores['Emotional Stability']
        lect = self.dictofScores['Intellect']
        
        print (f" Your Personality Scores are, Extraversion: {extra},  "
               f"Agreeableness: {agree}, Emotional Stablity: {emo}, " 
               f"Conscientiousness: {con}, Intellect and Imagination: {lect} ")
        
    def scatterPlot(self):
        """Creates a dataframe of the answers given from dictofAnswers, to plot 
        them onto a scatter plot to show the concentrations of answers in each 
        section
        
        Side Effects: Creates a plot that appears as the program is ran.
        """
        #Asher Harman, and this shows usage of seaplots
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


class MovieSorter():
    """A class that sets up the organization of the movies that are being 
        used to recommend to the user.
        
        Attributes: 
            dictofAnswers (dict): A dict holding the personality attributes as
                keys, and the list of answers as a value. 
            dictofScores (Dict): A dict that holds the personality attribute 
                as keys, and the results/ sums as a value. 
            movies (dataframe): a dataframe of the top 1000 imbd movies
    """
    def __init__(self, dictofAnswers, dictofScore):
        """Creates the initialization for organizing what movies will be
        recommended.
        
        Args:
            dictofAnswers (dict): A dict holding the personality attributes as
                keys, and the list of answers as a value. 
            dictofScores (Dict): A dict that holds the personality attribute 
                as keys, and the results/ sums as a value. 
                
        Side Effects: Creates a dataframe of movies in self 
        """
        self.dictofAnswers = dictofAnswers
        self.dictofScore = dictofScore
        self.movies = pd.read_csv("imdb_top_1000.csv")
        
    def topMovies(self):
        """Filters movies and return a dict of movies involving Title as key,
                and a set of (genre, ranking as a return)
        
        Return: finalList (list): A list with dict of movie titles, genres, and
            rating
        """
        
        topFilter = self.movies["IMDB_Rating"] > 8.5
        finalList = list()
        df1 = self.movies[topFilter]
        simple = df1[["Series_Title", "Genre", "IMDB_Rating"]]
        dictList = simple.to_dict(orient='record')
        for smallDict in dictList:
            genre = smallDict["Genre"].split(", ")
            newDict = dict()
            newDict["title"] = smallDict["Series_Title"]
            newDict["genre"] = genre
            newDict["rating"] = smallDict['IMDB_Rating']
            finalList.append(newDict)
        return finalList

    def movie_recommend(self, dictofScores, personality):
        """Conditional statements for possible user personality test results 
            (from the personality_user function). The logic for what scores will
                recommend what kinds of movies that are sorted in the various
                    subcategories.
        
        Args: dictofScores (Dict): A dict that holds the personality attribute 
            as keys, and the results/ sums as a value.
    """
        #Might be list comprension to make lists specifically of dicts that has a the specific genre
        traitgenre = {"Extraversion": "",
                    "Agreeableness": "",
                    "Conscientiousness": "",
                    "Emotional Stability": "",
                    "Intellect and Imagination": ""}
        
        genre = traitgenre[personality]
 
if __name__ == "__main__": 
   quiz = PersonalityTest()
   person = quiz.personality_test
   quiz.personality_user
   quiz.scatterPlot
   sorter = MovieSorter(quiz.dictofAnswers, quiz.dictofScores)
   sorter.movie_recommend(person)