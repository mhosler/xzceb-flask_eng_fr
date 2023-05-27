import unittest

from translator import french_to_english, english_to_french

class TestFrenchtoEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english(None), None) 
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        

class TestEnglishtoFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french(None), None)
        self.assertEqual(english_to_french('Hello'), 'Bonjour') 

unittest.main()