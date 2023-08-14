{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Defaulting to user installation because normal site-packages is not writeable\n",
      "Requirement already satisfied: montecarlo in /sfs/qumulo/qhome/ymb7fb/Documents/MSDS/DS5100/DS5100-2023-01-ymb7fb/finalproject2 (0.1)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install montecarlo"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'null' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-4-2bdb4aa90d7a>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mpandas\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mpd\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 4\u001b[0;31m \u001b[0;32mfrom\u001b[0m \u001b[0mmontecarlo\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mGame\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mGame\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      5\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0mmontecarlo\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mAnalyzer\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mAnalyzer\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m/sfs/qumulo/qhome/ymb7fb/Documents/MSDS/DS5100/DS5100-2023-01-ymb7fb/finalproject2/montecarlo/__init__.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      3\u001b[0m   {\n\u001b[1;32m      4\u001b[0m    \u001b[0;34m\"cell_type\"\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0;34m\"code\"\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 5\u001b[0;31m    \u001b[0;34m\"execution_count\"\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0mnull\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      6\u001b[0m    \u001b[0;34m\"metadata\"\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0;34m{\u001b[0m\u001b[0;34m}\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      7\u001b[0m    \u001b[0;34m\"outputs\"\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0;34m[\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mNameError\u001b[0m: name 'null' is not defined"
     ]
    }
   ],
   "source": [
    "import unittest\n",
    "import pandas as pd\n",
    "from montecarlo import Die as Die\n",
    "from montecarlo import Game as Game\n",
    "from montecarlo import Analyzer as Analyzer"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "E\n",
      "======================================================================\n",
      "ERROR: /sfs/qumulo/qhome/ymb7fb/ (unittest.loader._FailedTest)\n",
      "----------------------------------------------------------------------\n",
      "AttributeError: module '__main__' has no attribute '/sfs/qumulo/qhome/ymb7fb/'\n",
      "\n",
      "----------------------------------------------------------------------\n",
      "Ran 1 test in 0.001s\n",
      "\n",
      "FAILED (errors=1)\n"
     ]
    },
    {
     "ename": "SystemExit",
     "evalue": "True",
     "output_type": "error",
     "traceback": [
      "An exception has occurred, use %tb to see the full traceback.\n",
      "\u001b[0;31mSystemExit\u001b[0m\u001b[0;31m:\u001b[0m True\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/apps/software/standard/compiler/gcc/9.2.0/jupyter_conda/2020.11-py3.8/lib/python3.8/site-packages/IPython/core/interactiveshell.py:3426: UserWarning: To exit: use 'exit', 'quit', or Ctrl-D.\n",
      "  warn(\"To exit: use 'exit', 'quit', or Ctrl-D.\", stacklevel=1)\n"
     ]
    }
   ],
   "source": [
    "# Define unit tests\n",
    "class TestDieMethods(unittest.TestCase):\n",
    "    def test_roll(self):\n",
    "        die = Die([1, 2, 3, 4, 5, 6])\n",
    "        rolled_face = die.roll()\n",
    "        self.assertTrue(rolled_face in [1, 2, 3, 4, 5, 6])\n",
    "    \n",
    "    def test_invalid_roll_count(self):\n",
    "        die = Die([1, 2, 3, 4, 5, 6])\n",
    "        with self.assertRaises(ValueError):\n",
    "            die.roll(0)\n",
    "\n",
    "\n",
    "class TestGameMethods(unittest.TestCase):\n",
    "    def test_play(self):\n",
    "        dice = [Die([1, 2, 3]), Die([4, 5, 6])]\n",
    "        game = Game(dice)\n",
    "        game.play(3)\n",
    "        self.assertEqual(len(game.results), 3)\n",
    "    \n",
    "    def test_invalid_play_count(self):\n",
    "        dice = [Die([1, 2, 3]), Die([4, 5, 6])]\n",
    "        game = Game(dice)\n",
    "        with self.assertRaises(ValueError):\n",
    "            game.play(0)\n",
    "    \n",
    "\n",
    "\n",
    "class TestAnalyzerMethods(unittest.TestCase):\n",
    "    def test_compute_face_counts_per_roll(self):\n",
    "        dice = [Die([1, 2, 3]), Die([4, 5, 6])]\n",
    "        game = Game(dice)\n",
    "        game.play(3)\n",
    "        analyzer = Analyzer(game)\n",
    "        face_counts = analyzer.compute_face_counts_per_roll()\n",
    "        self.assertEqual(face_counts.shape[1], len(dice))  # Number of dice should match columns\n",
    "        \n",
    "    def test_compute_jackpot_results(self):\n",
    "        dice = [Die([1, 2, 3]), Die([1, 2, 3])]\n",
    "        game = Game(dice)\n",
    "        game.play(5)\n",
    "        analyzer = Analyzer(game)\n",
    "        jackpot_results = analyzer.compute_jackpot_results()\n",
    "        self.assertEqual(jackpot_results.sum(), 5)  # All faces are the same for jackpots\n",
    "        \n",
    "\n",
    "# Run the tests\n",
    "if __name__ == '__main__':\n",
    "    unittest.main()"
   ]
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
