import random
from django.db import models

# Define suits and ranks
SUITS = ['H', 'D', 'C', 'S']
RANKS = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 10, 'Q': 10, 'K': 10, 'A': 11
}

def create_deck():
    """Create and shuffle a deck consisting of 6 decks of cards."""
    deck = [{'suit': suit, 'rank': rank, 'value': value} for _ in range(6) for suit in SUITS for rank, value in RANKS.items()]
    random.shuffle(deck)
    return deck

class GameSession(models.Model):
    player_hand = models.JSONField(default=list)
    dealer_hand = models.JSONField(default=list)
    deck = models.JSONField(default=create_deck)
    game_over = models.BooleanField(default=False)
    winner = models.CharField(max_length=10, blank=True)
    showed = models.BooleanField(default=False)

    def initialCards(self):
        """Initialize dealer's hand with two cards."""
        self.dealer_hand = [self.draw_card(), self.draw_card()]

    def draw_card(self):
        """Draw a card from the deck."""
        if not self.deck:
            self.deck = create_deck()  # Reshuffle if the deck is empty
        return self.deck.pop()

    def calculate_score(self, hand):
        """Calculate the score of a given hand."""
        score = sum(card['value'] for card in hand)
        num_aces = sum(1 for card in hand if card['rank'] == 'A')

        # Adjust Aces' value if the score exceeds 21
        while score > 21 and num_aces:
            score -= 10
            num_aces -= 1
        return score

    def start_game(self):
        """Start a new game session."""
        self.deck = create_deck()
        self.player_hand = [self.draw_card(), self.draw_card()]
        self.dealer_hand = [self.draw_card(), self.draw_card()]
        self.game_over = False
        self.winner = ""

    def hit(self):
        """Player draws a card (Hit)."""
        if not self.game_over:
            self.player_hand.append(self.draw_card())
            # If player's score exceeds 21, they lose the game
            if self.calculate_score(self.player_hand) > 21:
                self.game_over = True
                self.winner = "Dealer"
                self.showed = True  # Reveal dealer's cards when player busts

    def stand(self):
        """Player chooses to stand, allowing the dealer to play."""
        if not self.game_over:
            # Dealer must draw cards until reaching at least 17
            while self.calculate_score(self.dealer_hand) < 17:
                self.dealer_hand.append(self.draw_card())

            player_score = self.calculate_score(self.player_hand)
            dealer_score = self.calculate_score(self.dealer_hand)

            # Determine the winner
            if dealer_score > 21 or player_score > dealer_score:
                self.winner = "Player"
            elif dealer_score > player_score:
                self.winner = "Dealer"
            else:
                self.winner = "Draw"

            self.game_over = True
            self.showed = True  # Reveal dealer's cards after standing
