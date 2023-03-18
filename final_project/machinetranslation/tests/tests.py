import unittest

from translator import english_to_french, french_to_english

class TestEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english("Bonjour"), "Hello") # test when Bonjour is given as input the output is Hello.
        self.assertEqual(french_to_english(None),None)  # test when null is given as input the output is null


class TestFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french("Hello"), "Bonjour") # test when Hello is given as input the output is Bonjour.
        self.assertEqual(english_to_french(None),None)  # test when null is given as input the output is null

unittest.main()