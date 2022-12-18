import unittest
from ../translator import french_to_english, english_to_french

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english("Bonjour"), "Hello") # test when 2 is given as input the output is 4.

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french("Hello"), "Bonjour") # test when 2 is given as input the output is 4.
        
unittest.main()