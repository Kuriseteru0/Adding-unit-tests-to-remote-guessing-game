import random
import unittest
from unittest.mock import patch
from server import evaluate_guess

class TestGuessingGame(unittest.TestCase):

    @patch('server.random.randint')
    def test_correct_guess_with_mock(self, mock_randint):
        mock_randint.return_value = 50 
        number = random.randint(1, 100)
        self.assertEqual(evaluate_guess(50, number), "Correct")

    def test_low_guess(self):
        self.assertEqual(evaluate_guess(30, 50), "Too low")

    def test_high_guess(self):
        self.assertEqual(evaluate_guess(70, 50), "Too high")
