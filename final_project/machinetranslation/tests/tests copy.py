import unittest
from translator import english_to_french, french_to_english

class TestEng2Fr(unittest.TestCase):
    def test1(self): 
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(english_to_french('None'),'')

class TestFr2eng(unittest.TestCase):
    def test2(self): 
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english(0),0)

if __name__ == '__main__':
    unittest.main()
