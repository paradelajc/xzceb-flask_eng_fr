# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=no-name-in-module
# pylint: disable=E0401

import unittest

from translator import english_to_french, french_to_english

class TestFrenchToEnlish(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english(None), None)
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english('Comment vas-tu?'), 'Fine')


class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french(None), None)
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(english_to_french('How are you?'), 'Fin')

if __name__ == '__main__':
    unittest.main()
