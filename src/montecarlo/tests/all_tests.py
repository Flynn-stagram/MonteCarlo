import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
import pandas as pd
import numpy as np

from montecarlo import Die

class TestDie(unittest.TestCase):
    
    def test_init(self):
        faces = [1, 2, 3, 4]
        die = Die(faces)
        self.assertTrue(isinstance(die, Die))
        self.assertTrue(isinstance(die._Die__thedie, pd.DataFrame))
        self.assertListEqual(die._Die__thedie['face'].tolist(), faces)
        self.assertListEqual(die._Die__thedie['weight'].tolist(), [1.0]*len(faces))
        
    def test_change_weight(self):
        faces = [1, 2, 3, 4]
        die = Die(faces)
        
        # Test changing weight of existing face
        die.change_weight(1, 2.0)
        self.assertAlmostEqual(die._Die__thedie.loc[die._Die__thedie['face'] == 1, 'weight'].values[0], 2.0)
        
        # Test changing weight of non-existing face
        with patch('sys.stdout', new=StringIO()) as fake_output:
            die.change_weight(5, 2.0)
            self.assertEqual(fake_output.getvalue().strip(), "Error: The face value you passed couldn't be found")
        
        # Test changing weight to non-float value
        with patch('sys.stdout', new=StringIO()) as fake_output:
            die.change_weight(1, 'string')
            self.assertEqual(fake_output.getvalue().strip(), "Error: The new weight isn't a float")
            
    def test_roll_die(self):
        faces = [1, 2, 3, 4]
        die = Die(faces)
        
        # Test rolling die
        outcomes = die.roll_die()
        self.assertTrue(isinstance(outcomes, list))
        self.assertIn(outcomes[0], faces)
        self.assertEqual(len(outcomes), 1)
        
        # Test rolling die multiple times
        outcomes = die.roll_die(times=10)
        self.assertEqual(len(outcomes), 10)
        self.assertTrue(all(outcome in faces for outcome in outcomes))
        
    def test_str(self):
        faces = [1, 2, 3, 4]
        die = Die(faces)
        die_str = str(die)
        self.assertIsInstance(die_str, str)
        self.assertEqual(die_str, str(die._Die__thedie))
        
        
if __name__ == '__main__':
    unittest.main(verbosity=2)
    
    
import unittest
import pandas as pd
from montecarlo import Die, Game

class TestGame(unittest.TestCase):
    
    def setUp(self):
        self.dice = [Die([1, 2, 3, 4, 5, 6])]
        self.game = Game(self.dice)
        
    def test_play(self):
        self.game.play(10)
        results = self.game.show_results()
        self.assertIsInstance(results, pd.DataFrame)
        self.assertEqual(len(results), 10)
        self.assertEqual(len(results.columns), 1)
        self.assertEqual(results.index.name, "Roll Number")
        self.assertEqual(results.columns[0], "Die 1")
        
    def test_show_results_wide(self):
        self.game.play(5)
        results = self.game.show_results(form='wide')
        self.assertIsInstance(results, pd.DataFrame)
        self.assertEqual(len(results), 5)
        self.assertEqual(len(results.columns), 1)
        self.assertEqual(results.index.name, "Roll Number")
        self.assertEqual(results.columns[0], "Die 1")
        
    def test_show_results_narrow(self):
        self.game.play(5)
        results = self.game.show_results(form='narrow')
        self.assertIsInstance(results, pd.DataFrame)
        self.assertEqual(len(results), 5)
        self.assertEqual(len(results.columns), 3)
        self.assertEqual(results.columns[0], "Roll Number")
        self.assertEqual(results.columns[1], "Die")
        self.assertEqual(results.columns[2], "Face")
        
if __name__ == '__main__':
    unittest.main()

import unittest
import pandas as pd
from montecarlo import Die, Game, Analyzer

class TestAnalyzer(unittest.TestCase):
    def setUp(self):
        dice = [Die([1,2,3,4,5,6]), Die([1,2,3,4,5,6])]
        self.game = Game(dice)
        self.analyzer = Analyzer(self.game)

    def test_jackpot(self):
        self.assertEqual(self.analyzer.jackpot(), 0)
        self.game.play()
        self.assertEqual(self.analyzer.jackpot(), 1)

    def test_combo(self):
        self.assertTrue(self.analyzer.combo().empty)
        self.game.play()
        self.assertFalse(self.analyzer.combo().empty)

    def test_face_count(self):
        face_counts = self.analyzer.face_count()
        self.assertIsInstance(face_counts, pd.DataFrame)
        self.assertEqual(face_counts.index.name, 'Roll Number')
        self.assertListEqual(face_counts.columns.tolist(), [1, 2, 3, 4, 5, 6])
        self.assertTrue((face_counts.sum(axis=1) == 2).all())
if __name__ == '__main__':
    unittest.main()

