import pandas as pd
import numpy as np
import numbers
import random
from typing import Dict

##Faces are the sides of the die
##Weights are probability of rolling a side, frequency of the number on each side.

DEFAULT_WEIGHT = 1.0

class Die():
    '''
    A die has N sides, or “faces”, and W weights, and can be rolled to select
    a face.
    
    Class Methods:
    __init__ 
    change_weight
    roll_die
    show
    '''      
    def __init__(self, faces):
        '''
        PURPOSE: An initializer for the class "Die"
        INPUT: Array of faces as an argument
        OUTPUT: Saves both faces and weights into a private dataframe that is to be shared by the other methods.
        '''
        self.faces = faces if isinstance(faces, list) else list(faces)
        self._my_die = pd.DataFrame({
            'faces': self.faces,
            'weights': [DEFAULT_WEIGHT] * len(self.faces)
        })
        return None

    def change_weight(self, face_value, new_weight):
        ''' 
        PURPOSE: A method to change the weight of a single side of the die
        INPUT:  The face value to be changed face_value, and the new weight (new_weight).
        OUTPUT: Error messages if either the face_value is invalid or weight cannot be converted to float.
        '''
        #Checks to see if the face passed is valid; is it in the array of weights 

        if face_value not in self._my_die['faces'].values:
            raise KeyError(f"Face value {face_value} not found on the die.")
        
        try:
            new_weight = float(new_weight)
        except ValueError:
            raise ValueError("The new weight cannot be converted to a float value.")
        
        self._my_die.loc[self._my_die['faces'] == face_value, 'weights'] = new_weight
                    
    def roll_die(self, n_rolls = 1):
        ''' 
        PURPOSE: A method to roll the die one or more times
        INPUT:  Integer - how many times the die is to be rolled; defaults to 1.
        OUTPUT: None
        '''
        results = self._my_die.sample(n=n_rolls, weights='weights', replace=True)['faces'].tolist()
        return results
        
    def show(self):
        '''
        PURPOSE: This method returns the current set of faces and weights of the die. 
        INPUT: None
        OUTPUT: my_die dataframe
        '''
        return self._my_die
    
class Game():
    '''
    A game consists of rolling of one or more dice of the same kind one or more times. Game passes a list of Die objects. 
    
    Class Methods:
    __init__ 
    play
    show
    '''  
    def __init__(self, die_list):
        '''
        PURPOSE: An initializer for the class "Game"
        INPUT: A list of already instantiated similar Die objects.
        OUTPUT: None.           
        '''
        self.die_list = die_list
        
    def play(self, times):
        '''
        PURPOSE: Create a dataframe with the roll number, die number, and the face rolled in that instance. 
        INPUT:Takes a parameter to specify how many times the dice should be rolled
        OUTPUT: Saves the result of the play to a private dataframe of shape n_rolls by M dice. This results in a table of data with columns for roll number, the die number (its list index), and the face rolled in that instance.
        '''
        results = []
        for die in self.die_list:
            results.extend(die.roll_die(n_rolls=times))
        
        n_dice = len(self.die_list)
        roll_numbers = list(range(1, times+1)) * n_dice
        die_numbers = [i for i in range(n_dice) for _ in range(times)]
        
        self._dice_play = pd.DataFrame({
            'roll_number': roll_numbers,
            'die_number': die_numbers,
            'face_rolled': results
        }).pivot(index='roll_number', columns='die_number')
        
        return self._dice_play
    
    def show(self, times, display='wide'):
        '''
        PURPOSE: This method shows the results of the most recent play. 
        INPUT: This method just passes the private dataframe to the user. Takes a parameter to return the dataframe in narrow or wide form.
        OUTPUT: Game dataframe
        '''      
        results = self.play(times)
        
        if display.lower() == 'narrow':
            return results.stack(level='die_number')
        elif display.lower() == 'wide': 
            return results
        else:
            raise ValueError('Please use parameter either wide or narrow. Try again!')

class Analyzer():
    '''
    An analyzer takes the results of a single game and computes various descriptive statistical properties about it. 
    These properties results are available as attributes of an Analyzer object. Attributes (and associated methods) include:
    
    Class Methods:
    __init__
    compute_combo
    compute_jackpot
    compute_face_counts_per_roll
    '''
    def __init__(self, game_objects):
        '''
        PURPOSE: An initializer for the class "Analyzer"
        INPUT: Takes a game object as its input parameter.
        OUTPUT: None.           
        '''
        self.games = game_objects
        self.df = {}
        self.jackpot_results_df = []
        self.face_counts_df = [] # Initialize the attribute for storing face counts
        
    def compute_combo(self, times):
        '''
        PURPOSE: This method computes the distinct combinations of faces rolled, along with their counts. 
        INPUT: None.
        OUTPUT: None. 
        '''
        combo_data = []
        for game in self.games:
            df = game.play(times)
            combo_df = df.apply(tuple, axis=1).value_counts().reset_index()
            combo_df.columns = ['combinations', 'count']
            combo_data.append(combo_df)
        
        self.combo_df = pd.concat(combo_data, keys=range(len(self.games)), names=['game_number', None]).sort_index()
        return self.combo_df  # Return the computed combo_df
           
    def compute_jackpot(self, times):
        '''
        PURPOSE: Calculate the number of times the game resulted in all faces being identical for all games. 
        INPUT: Integer for the number of rounds to iterate over.
        OUTPUT: DataFrame containing the jackpot results with roll numbers as the index. 
        '''
        
        jackpot_results = []

        for game in self.games:
            df = game.play(times)
            is_jackpot = df.apply(lambda row: len(set(row)) == 1, axis=1)
            jackpot_results.extend(is_jackpot.astype(int))  # Convert bool to int
        
        jackpot_df = pd.DataFrame({'jackpot_count': jackpot_results}, index=range(1, times + 1))
        jackpot_df.index.name = 'roll_number'
        return jackpot_df


    def compute_face_counts_per_roll(self):
        '''
        PURPOSE: Computes how many times a given face is rolled in each event and stores the results as a DataFrame in wide format.
        INPUT: None.
        OUTPUT: None.
        '''
        face_counts = []
        for game in self.games:
            df = game.play()
            face_counts.append(df['face_rolled'].value_counts())
        
        self.face_counts_df = pd.DataFrame(face_counts).fillna(0)