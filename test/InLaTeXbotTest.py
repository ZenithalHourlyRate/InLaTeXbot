import unittest
from unittest.mock import Mock, MagicMock
from src.InLaTeXbot import InLaTeXbot


class InLaTeXbotTest(unittest.TestCase):

    def setUp(self):
        self.sut = InLaTeXbot(MagicMock())
        self.sut._preambleManager.putPreambleToDatabase = Mock()
        
#    def testLaunch(self):
#        self.sut.launch()
#    
#    def testStop(self):
#        self.sut.stop()

    def testOnPreambleArrived(self):

        bot = MagicMock()
        
        update = MagicMock()
        update.message.reply = Mock()
        update.message.text = Mock()
        update.message.text.__len__ = Mock(return_value = self.sut._resourceManager.getNumber("max_preamble_length")+1)
        self.sut.onPreambleArrived(bot, update)
        update.message.reply_text.assert_called_with(self.sut._resourceManager.getString("preamble_too_long")%self.sut._resourceManager.getNumber("max_preamble_length"))
        
    def testOnInlineQuery(self):
        bot = MagicMock()
        
        update = MagicMock()
        update.inline_query.query = "$x^2$"
        update.inline_query.from_user.id = 1151
        update.inline_query.id = "id"
        #For single user (consequent)
        self.sut.onInlineQuery(bot, update)
        self.sut.onInlineQuery(bot, update)
        
        #For different users(concurrent)
        self.sut.onInlineQuery(bot, update)
        update = MagicMock()
        update.inline_query.query = "$x^3$"
        update.inline_query.query = "$x^3$"
        update.inline_query.from_user.id = 1152
        update.inline_query.id = "id"
        self.sut.onInlineQuery(bot, update)

        
        
if __name__ == '__main__':
    unittest.main()
     
