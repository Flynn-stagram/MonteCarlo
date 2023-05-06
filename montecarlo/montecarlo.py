import pandas as pd
import numpy as np
import random

class Die():
    """A die has N sides, or “faces”, and W weights, and can be rolled to select
    a face. W defaults to 1.0 for each face but can be changed after the object is created.
    Note that the weights are just numbers, not a normalized probability distribution.
    The die has one behavior, which is to be rolled one or more times.
    Note that what we are calling a “die” here can be any discrete random variable associated with a stochastic process, such as using a deck of cards or flipping a coin or speaking a language. Our probability model for such variable is, however, very simple. since our weights apply to only to single events, we are assuming that the events are independent. This makes sense for coin tosses but not for language use"""
    def __init__(self, faces):
        """Takes an array of faces as an argument. The array's data type (type) may be strings or numbers.
        Internally initializes the weights to 1.0 for each face.
        Saves both faces and weights into a private dataframe that is to be shared by the other methods."""
        self.faces = faces
        self.__thedie = pd.DataFrame({'face': faces, 'weight': [1.0]*len(faces)})
    
    def change_weight(self, face, new_weight):
        """A method to change the weight of a single side.
        • Takes two arguments: the face value to be changed
        and the new weight.
        • Checks to see if the face passed is valid; is it in the
        array of weights?
        • Checks to see if the weight is valid; is it a float? Can it
        be converted to one?"""
        if face in self.__thedie['face'].values:
            try:
                new_weight_float = float(new_weight)
                self.__thedie.loc[self.__thedie['face'] == face, 'weight'] = new_weight_float
                print(f"The weight of face {face} has been changed to {new_weight_float}")
            except ValueError:
                print("Error: The new weight isn't a float")
        else:
            print("Error: The face value you passed couldn't be found")
        
    def roll_die(self, times=1):
        """A method to roll the die one or more times.
        • Takes a parameter of how many times the die is to be
        rolled; defaults to 1.
        • This is essentially a random sample from the vector of
        faces according to the weights.
        •  Returns a list of outcomes.
        •  Does not store internally these results."""
        outcomes = []
        for i in range(times):
            outcome = random.choices(self.__thedie['face'], weights=self.__thedie['weight'], k=1)[0] # type: ignore
            outcomes.append(outcome)
        return outcomes
            
    def __str__(self):
        """A method to show the user the die's current set of faces and
        weights (since the latter can be changed).
        • Returns the dataframe created in the initializer."""
        return str(self.__thedie)



class Game():
    """A game consists of rolling of one or more dice of the same kind one or
    more times.
    • Each game is initialized with one or more of similarly defined
    dice (Die objects).
    • By "same kind" and "similarly defined" we mean that each die
    in a given game has the same number of sides and associated
    faces, but each die object may have its own weights.
    • The class has a behavior to play a game, i.e. to rolls all of the
    dice a given number of times.
    • The class keeps the results of its most recent play."""
    def __init__(self, dice):
        """An initializer takes a single parameter, a list of already instantiated similar Die objects."""
        self.dice = dice
        self.__theresults = pd.DataFrame()
        
    def play(self, howmanyrolls):
        """A play method
        • Takes a parameter to specify how many times the
        dice should be rolled.
        • Saves the result of the play to a private dataframe of
        shape N rolls by M dice.
        • The private dataframe should have the roll number is
        a named index.
        •  This results in a table of data with columns for roll
        number, the die number (its list index), and the face
        rolled in that instance."""
        results = []
        for i in range(howmanyrolls):
            roll = [die.roll_die() for die in self.dice]
            results.append(roll)
        self.__theresults = pd.DataFrame(results, index=range(howmanyrolls), columns=["Die " + str(i+1) for i in range(len(self.dice))])
        self.__theresults.index.name = "Roll Number"
        
    def show_results(self, form='wide'):
        """A method to show the user the results of the most recent play.
        • This method just passes the private dataframe to the user.
        • Takes a parameter to return the dataframe in narrow or wide form.
        • This parameter defaults to wide form.
        • This parameter should raise an exception if the user passes an invalid option.
        • The narrow form of the dataframe will have a two-column index with the roll number and the die number, and a column for the face rolled.
        • The wide form of the dataframe will a single column index with the roll number, and each die number as a column."""
        if form == 'wide':
            return self.__theresults
        elif form == 'narrow':
            return pd.melt(self.__theresults.reset_index(), id_vars="Roll Number", var_name="Die", value_name="Face")
        else:
            raise ValueError("You need to specify either wide or narrow")



class Analyzer():
    """An analyzer takes the results of a single game and computes various descriptive statistical properties about it. These properties results are available as attributes of an Analyzer object. Attributes (and associated methods) include:"""
    def __init__(self, game):
        """An initializer
        •  Takes a game object as its input parameter.
        • At initialization time, it also infers the data type of the die faces used."""
        self.game = game
        
        # Infer data type of die faces
        sample_roll = game.show_results().iloc[0]
        self.dtype = type(sample_roll[0])
        
        self.jackpot_results = pd.DataFrame()
        self.combo_results = pd.DataFrame()
        self.facecount_results = pd.DataFrame()
        
    def jackpot(self):
        """A jackpot method to compute how many times the game resulted in all faces being identical.
        • Returns an integer for the number times to the user.
        •  Stores the results as a dataframe of jackpot results in a public attribute.
        • The dataframe should have the roll number as a named index."""
        jackpot_count = len(self.jackpot_results)
        if jackpot_count == 0:
            # Compute jackpot results
            identical_rolls = self.game.show_results().eq(self.game.show_results().iloc[:, 0], axis=0).all(axis=1)
            self.jackpot_results = pd.DataFrame({'jackpot': identical_rolls})
            self.jackpot_results.index.name = 'Roll Number'
            jackpot_count = identical_rolls.sum()
        return jackpot_count
        
    def combo(self):
        """A combo method to compute the distinct combinations of faces rolled, along with their counts.
        • Combinations should be sorted and saved as a multi-columned index.
        •  Stores the results as a dataframe in a public attribute."""
        if self.combo_results.empty:
            # Compute combo results
            combos = self.game.show_results().apply(lambda row: tuple(sorted(row)), axis=1).value_counts().reset_index()
            combos.columns = ['combo', 'count']
            self.combo_results = combos.set_index('combo').sort_index()
        return self.combo_results
    
    def face_count(self):
        """A face counts per roll method to compute how many times a given face is rolled in each event.
        •  Stores the results as a dataframe in a public attribute.
        • The dataframe has an index of the roll number and face values as columns (i.e. it is in wide format)."""
        face_counts = self.__theresults.melt(var_name='Die', value_name='Face').groupby(['Roll Number', 'Face']).size().unstack(fill_value=0) # type: ignore
        return face_counts

