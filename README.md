# montecarlo
This is a project for data science computer programming final project (DS5100).

Metadata
Name: Brittny Hopwood, Monte Carlo Simulator.
Synopsis: The package provides classes to simulate dice rolling, play dice games, and analyze game results.
Install the Montecarlo Package using pip.
Import the package as montecarlo.  

Package Classes:

Die Class

Simulates a die with multiple faces and weights.

Returns: The rolled face.

Game Class

Simulates playing a game with one or more dice.

Returns (pd.DataFrame): Dataframe containing the game results.

Analyzer Class

Analyzes game results and computes statistics.

Returns (float): Relative frequency of jackpots.

Returns (pd.DataFrame): Dataframe containing distinct combinations of faces.

API description

Class public methods:

Die Class Methods

def change_weight(self, face_value, new_weight):
        ''' 
        PURPOSE: A method to change the weight of a single side of the die
        INPUT:  The face value to be changed face_value, and the new weight (new_weight).
        OUTPUT: Error messages if either the face_value is invalid or weight cannot be converted to float.
        '''

 def roll_die(self, n_rolls = 1):
        ''' 
        PURPOSE: A method to roll the die one or more times
        INPUT:  Integer - how many times the die is to be rolled; defaults to 1.
        OUTPUT: None
        '''

def show(self):
        '''
        PURPOSE: This method returns the current set of faces and weights of the die. 
        INPUT: None
        OUTPUT: my_die dataframe
        '''
        
        
Game Class Methods

 def __init__(self, die_list):
        '''
        PURPOSE: An initializer for the class "Game"
        INPUT: A list of already instantiated similar Die objects.
        OUTPUT: None.           
        '''
def play(self, times):
        '''
        PURPOSE: Create a dataframe with the roll number, die number, and the face rolled in that instance. 
        INPUT:Takes a parameter to specify how many times the dice should be rolled
        OUTPUT: Saves the result of the play to a private dataframe of shape n_rolls by M dice. This results in a table of data with columns for roll number, the die number (its list index), and the face rolled in that instance.
        '''
        
def show(self, times, display='wide'):
        '''
        PURPOSE: This method shows the results of the most recent play. 
        INPUT: This method just passes the private dataframe to the user. Takes a parameter to return the dataframe in narrow or wide form.
        OUTPUT: Game dataframe
        '''   

Analyzer Class Methods

def __init__(self, game_objects):
        '''
        PURPOSE: An initializer for the class "Analyzer"
        INPUT: Takes a game object as its input parameter.
        OUTPUT: None.           
        '''
        
def compute_combo(self, times):
        '''
        PURPOSE: This method computes the distinct combinations of faces rolled, along with their counts. 
        INPUT: None.
        OUTPUT: None. 
        '''

    def compute_jackpot(self, times):
        '''
        PURPOSE: This method computes how many times the game resulted in all faces being identical. 
        INPUT: None.
        OUTPUT: Integer for the number times to the user. 
        '''

Manifest
montecarlo 
    - __init__.py
    - montecarlo.py

montecarlo_demo.py
montecarlo_tests.py
README.md
setup.py
LICENSE.txt
results.txt
