{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import numbers\n",
    "import sys\n",
    "import random\n",
    "from typing import Dict\n",
    "import os"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Die():\n",
    "    '''\n",
    "    A die has N sides, or “faces”, and W weights, and can be rolled to select\n",
    "    a face.\n",
    "    \n",
    "    Class Methods:\n",
    "    __init__ \n",
    "    validate_weight\n",
    "    change_weight\n",
    "    roll\n",
    "    show_faces_and_weights\n",
    "    '''      \n",
    "    def __init__(self, faces):\n",
    "        self._data = pd.DataFrame({\"face\": faces, \n",
    "                                   \"weight\": 1.0})\n",
    "        self._data.set_index(\"face\", inplace=True)\n",
    "    \n",
    "    def _validate_face(self, face):\n",
    "        ''' \n",
    "        PURPOSE: A method to validate the weight of a single side of the die\n",
    "        INPUT:  The face value to be validate face_value.\n",
    "        OUTPUT: Error messages if either the face_value is invalid or weight cannot be converted to float.\n",
    "        '''\n",
    "        if face not in self._data.index:\n",
    "            raise ValueError(f\"Face '{face}' is not valid.\")\n",
    "\n",
    "    def _validate_weight(self, weight):\n",
    "        ''' \n",
    "        PURPOSE: A method to validate the weight of a single side of the die\n",
    "        INPUT:  The face value to be validate face_value.\n",
    "        OUTPUT: Error messages if either the face_value is invalid or weight cannot be converted to float.\n",
    "        '''\n",
    "        try:\n",
    "            float_weight = float(weight)\n",
    "        except ValueError:\n",
    "            raise ValueError(\"Weight must be a valid float value.\")\n",
    "        return float_weight\n",
    "\n",
    "    def change_weight(self, face, new_weight):\n",
    "        ''' \n",
    "        PURPOSE: A method to change the weight of a single side of the die\n",
    "        INPUT:  The face value to be changed face_value, and the new weight (new_weight).\n",
    "        OUTPUT: Error messages if either the face_value is invalid or weight cannot be converted to float.\n",
    "        '''\n",
    "        self._validate_face(face)\n",
    "        new_weight = self._validate_weight(new_weight)\n",
    "        self._data.at[face, \"weight\"] = new_weight\n",
    "\n",
    "    def roll(self, rolls=1):\n",
    "        ''' \n",
    "        PURPOSE: A method to roll the die one or more times\n",
    "        INPUT:  Integer - how many times the die is to be rolled; defaults to 1.\n",
    "        OUTPUT: None\n",
    "        '''\n",
    "        if rolls < 1:\n",
    "            raise ValueError(\"Number of rolls must be at least 1.\")\n",
    "        \n",
    "        results = []\n",
    "        for _ in range(rolls):\n",
    "            result = random.choices(self._data.index, weights=self._data[\"weight\"], k=1)[0]\n",
    "            results.append(result)\n",
    "        \n",
    "        return results\n",
    "\n",
    "    def show_faces_and_weights(self):\n",
    "        '''\n",
    "        PURPOSE: This method returns the current set of faces and weights of the die. \n",
    "        INPUT: None\n",
    "        OUTPUT: my_die dataframe\n",
    "        '''\n",
    "        return self._data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Initial faces and weights:\n",
      "      weight\n",
      "face        \n",
      "1        1.0\n",
      "2        1.0\n",
      "3        1.0\n",
      "4        1.0\n",
      "5        1.0\n",
      "6        1.0\n",
      "\n",
      "Faces and weights after changing weight:\n",
      "      weight\n",
      "face        \n",
      "1        1.0\n",
      "2        1.0\n",
      "3        0.5\n",
      "4        1.0\n",
      "5        1.0\n",
      "6        1.0\n",
      "\n",
      "Rolling custom die:\n",
      "['3', '1', '1', '2', '6']\n"
     ]
    }
   ],
   "source": [
    "# Usage\n",
    "initial_faces = [\"1\", \"2\", \"3\", \"4\", \"5\", \"6\"]\n",
    "custom_die = Die(initial_faces)\n",
    "\n",
    "print(\"Initial faces and weights:\")\n",
    "print(custom_die.show_faces_and_weights())\n",
    "\n",
    "custom_die.change_weight(\"3\", 0.5)\n",
    "print(\"\\nFaces and weights after changing weight:\")\n",
    "print(custom_die.show_faces_and_weights())\n",
    "\n",
    "print(\"\\nRolling custom die:\")\n",
    "print(custom_die.roll(5))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Game():\n",
    "    '''\n",
    "    A game consists of rolling of one or more dice of the same kind one or more times. Game passes a list of Die objects. \n",
    "    \n",
    "    Class Methods:\n",
    "    __init__ \n",
    "    play\n",
    "    show_results\n",
    "    ''' \n",
    "    def __init__(self, dice_list):\n",
    "        '''\n",
    "        PURPOSE: An initializer for the class \"Game\"\n",
    "        INPUT: A list of already instantiated similar Die objects.\n",
    "        OUTPUT: None.           \n",
    "        '''\n",
    "        self.dice = dice_list\n",
    "        self.results = None\n",
    "    \n",
    "    def play(self, rolls):\n",
    "        '''\n",
    "        PURPOSE: Create a dataframe with the roll number, die number, and the face rolled in that instance. \n",
    "        INPUT:Takes a parameter to specify how many times the dice should be rolled\n",
    "        OUTPUT: Saves the result of the play to a private dataframe of shape n_rolls by M dice. This results in a table of data with columns for roll number, the die number (its list index), and the face rolled in that instance.\n",
    "        '''\n",
    "        results_list = []\n",
    "        for roll_num in range(1, rolls + 1):\n",
    "            roll_data = {\"Roll Number\": roll_num}\n",
    "            for die_num, die in enumerate(self.dice):\n",
    "                face_rolled = die.roll()[0]\n",
    "                roll_data[f\"Die {die_num+1}\"] = face_rolled\n",
    "            results_list.append(roll_data)\n",
    "        \n",
    "        self.results = pd.DataFrame(results_list)\n",
    "    \n",
    "    def show_results(self, form=\"wide\"):\n",
    "        '''\n",
    "        PURPOSE: This method shows the results of the most recent play. \n",
    "        INPUT: This method just passes the private dataframe to the user. Takes a parameter to return the dataframe in narrow or wide form.\n",
    "        OUTPUT: Game dataframe\n",
    "        ''' \n",
    "        if form == \"wide\":\n",
    "            return self.results.set_index(\"Roll Number\")\n",
    "        elif form == \"narrow\":\n",
    "            return self.results.melt(id_vars=[\"Roll Number\"], var_name=\"Die Number\", value_name=\"Face Rolled\")\n",
    "        else:\n",
    "            raise ValueError(\"Invalid value for the 'form' parameter. Use 'wide' or 'narrow'.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Results in wide form:\n",
      "            Die 1 Die 2\n",
      "Roll Number            \n",
      "1               A     Y\n",
      "2               D     X\n",
      "3               A     Z\n",
      "4               B     Z\n",
      "5               C     Y\n",
      "\n",
      "Results in narrow form:\n",
      "   Roll Number Die Number Face Rolled\n",
      "0            1      Die 1           A\n",
      "1            2      Die 1           D\n",
      "2            3      Die 1           A\n",
      "3            4      Die 1           B\n",
      "4            5      Die 1           C\n",
      "5            1      Die 2           Y\n",
      "6            2      Die 2           X\n",
      "7            3      Die 2           Z\n",
      "8            4      Die 2           Z\n",
      "9            5      Die 2           Y\n"
     ]
    }
   ],
   "source": [
    "# Usage\n",
    "faces1 = [\"A\", \"B\", \"C\", \"D\"]\n",
    "weights1 = [0.2, 0.1, 0.3, 0.4]\n",
    "dice1 = Die(faces1)\n",
    "\n",
    "faces2 = [\"X\", \"Y\", \"Z\"]\n",
    "dice2 = Die(faces2)\n",
    "\n",
    "dice_list = [dice1, dice2]\n",
    "\n",
    "game = Game(dice_list)\n",
    "\n",
    "game.play(5)\n",
    "print(\"Results in wide form:\")\n",
    "print(game.show_results(\"wide\"))\n",
    "\n",
    "print(\"\\nResults in narrow form:\")\n",
    "print(game.show_results(\"narrow\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Analyzer():\n",
    "    def __init__(self, game):\n",
    "        '''\n",
    "        An analyzer takes the results of a single game and computes various descriptive statistical properties about it. \n",
    "        These properties results are available as attributes of an Analyzer object. Attributes (and associated methods) include:\n",
    "    \n",
    "        Class Methods:\n",
    "        __init__\n",
    "        compute_combo\n",
    "        compute_jackpot\n",
    "        compute_face_counts_per_roll\n",
    "        '''\n",
    "        self.game = game\n",
    "        self.roll_data = self.game.results.drop(\"Roll Number\", axis=1)\n",
    "        self.data_type = type(self.roll_data.iloc[0, 0])  # Infer the data type of die faces\n",
    "        \n",
    "        self.face_counts_per_roll = self.compute_face_counts_per_roll()\n",
    "        self.jackpot_results = self.compute_jackpot_results()\n",
    "        self.combo_results = self.compute_combo_results()\n",
    "    \n",
    "    def compute_face_counts_per_roll(self):\n",
    "        '''\n",
    "        PURPOSE: This method computes the distinct combinations of faces rolled, along with their counts. \n",
    "        INPUT: None.\n",
    "        OUTPUT: None. \n",
    "        ''' \n",
    "        face_counts = self.roll_data.apply(lambda col: col.value_counts())\n",
    "        return face_counts.fillna(0).astype(int)\n",
    "    \n",
    "    def compute_jackpot_results(self):\n",
    "        '''\n",
    "        PURPOSE: This method computes how many times the game resulted in all faces being identical. \n",
    "        INPUT: None.\n",
    "        OUTPUT: Integer for the number times to the user. \n",
    "        '''\n",
    "        jackpot_counts = self.roll_data.apply(lambda row: row.nunique() == 1)\n",
    "        return jackpot_counts.astype(int)\n",
    "    \n",
    "    def compute_combo_results(self):\n",
    "        '''\n",
    "        PURPOSE: This method computes the distinct combinations of faces rolled, along with their counts. \n",
    "        INPUT: None.\n",
    "        OUTPUT: None. \n",
    "        ''' \n",
    "        combo_counts = self.roll_data.drop_duplicates().apply(lambda row: tuple(sorted(row)))\n",
    "        combo_results = combo_counts.value_counts().sort_index()\n",
    "        combo_index = pd.MultiIndex.from_tuples(combo_results.index, names=self.roll_data.columns)\n",
    "        combo_df = pd.DataFrame(combo_results.values, index=combo_index, columns=[\"Combo Count\"])\n",
    "        return combo_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Face counts per roll:\n",
      "   Die 1  Die 2\n",
      "A      1      0\n",
      "B      2      0\n",
      "C      2      0\n",
      "X      0      1\n",
      "Y      0      2\n",
      "Z      0      2\n",
      "\n",
      "Jackpot results:\n",
      "Die 1    0\n",
      "Die 2    0\n",
      "dtype: int64\n",
      "\n",
      "Combo results:\n",
      "             Combo Count\n",
      "Die 1 Die 2             \n",
      "A     X                1\n",
      "B     Y                2\n",
      "C     Z                2\n"
     ]
    }
   ],
   "source": [
    "# Usage\n",
    "faces1 = [\"A\", \"B\", \"C\", \"D\"]\n",
    "dice1 = Die(faces1)\n",
    "\n",
    "faces2 = [\"X\", \"Y\", \"Z\"]\n",
    "dice2 = Die(faces2)\n",
    "\n",
    "dice_list = [dice1, dice2]\n",
    "\n",
    "game = Game(dice_list)\n",
    "game.play(5)\n",
    "\n",
    "analyzer = Analyzer(game)\n",
    "print(\"Face counts per roll:\")\n",
    "print(analyzer.face_counts_per_roll)\n",
    "\n",
    "print(\"\\nJackpot results:\")\n",
    "print(analyzer.jackpot_results)\n",
    "\n",
    "print(\"\\nCombo results:\")\n",
    "print(analyzer.combo_results)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
