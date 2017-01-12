import unittest
from unittest.mock import Mock
from src.PreambleManager import PreambleManager
from src.ResourceManager import ResourceManager

class PreambleManagerTest(unittest.TestCase):

    def setUp(self):
        self.resourceManager = ResourceManager()
        self.sut = PreambleManager(self.resourceManager)

    def testValidatePreamble(self):
        correct_preamble="\documentclass[12pt]{article}"
        self.assertEqual(self.sut.validatePreamble(correct_preamble), (True, ""))

        incorrect_preamble="\documentclass[12pt]{arti}"
        self.assertEqual(self.sut.validatePreamble(incorrect_preamble), (False, self.resourceManager.getString("preamble_invalid")))
        
        too_long_preamble=Mock()
        too_long_preamble.__len__ = Mock(return_value = self.resourceManager.getNumber("max_preamble_length")+1)
        message = self.resourceManager.getString("preamble_too_long")%self.resourceManager.getNumber("max_preamble_length")
        self.assertEqual(self.sut.validatePreamble(too_long_preamble), (False, message))
        
if __name__ == '__main__':
    unittest.main()
    
