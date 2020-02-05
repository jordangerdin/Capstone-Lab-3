import camelCase
from unittest import TestCase

class TestCamelCase(TestCase):

    def test_camelcase_sentance(self):
        self.assertEqual('helloWorld', camelCase.toCamelCase('Hello World'))

    def test_camelcase_empty_string(self):
        self.assertEqual('', camelCase.toCamelCase(' '))
        self.assertEqual('123abcAbc', camelCase.toCamelCase('123abc abc'))
    
    def test_camelcase_newlines_or_tabs(self):
        self.assertEqual('noNewlinesOrTabs', camelCase.toCamelCase('\tNo Newlines Or Tabs'))
        
    def test_camelcase_multiple_spaces_between_words(self):
        self.assertEqual('noDoubleSpaces', camelCase.toCamelCase('No  Double  Spaces'))

if __name__ == '__main__':
    import unittest
    unittest.main()