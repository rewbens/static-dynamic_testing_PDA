import unittest
from src.card import Card
from src.card_game import CardGame


class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.ace = Card("Ace",9)
        self.queen = Card("Queen", 10)
        self.King = Card("king", 11)
        self.card_game = CardGame(0, [])

    
    def test_check_for_ace(self):
        self.card_game.check_for_ace(self.ace)
        self.assertEqual(True, self.card_game.check_for_ace(self.ace))

    def test_is_not_ace(self):
        # self.card_game.check_for_ace(self.queen)
        self.assertEqual(False, self.card_game.check_for_ace(self.queen))

    def test_highest_card(self):
        card1 = self.King
        card2 = self.queen 
        self.card_game.highest_card(card1, card2)
        self.assertEqual(card1, self.card_game.highest_card(card1, card2))
        
        
    def test_cards_total(self):
        card1 = self.ace
        card2 = self.queen
        card3 = self.King
        cards = (card1, card2, card3)
        self.assertEqual( "You have a total of 30", self.card_game.cards_total(cards))





