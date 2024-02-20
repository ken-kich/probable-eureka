import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

        for suit in suits:
            for value in values:
                self.cards.append(Card(suit, value))

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop()

class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def calculate_score(self):
        score = 0
        num_aces = 0

        for card in self.cards:
            if card.value.isnumeric():
                score += int(card.value)
            elif card.value in ['J', 'Q', 'K']:
                score += 10
            elif card.value == 'A':
                num_aces += 1
                score += 11

        while num_aces > 0 and score > 21:
            score -= 10
            num_aces -= 1

        return score

class Player:
    def __init__(self):
        self.hand = Hand()

    def show_hand(self):
        for card in self.hand.cards:
            print(f"{card.value} of {card.suit}")

class Dealer(Player):
    def show_hand(self):
        print(f"First card: {self.hand.cards[0].value} of {self.hand.cards[0].suit}")

class BlackjackGame:
    def __init__(self):
        self.deck = Deck()
        self.player = Player()
        self.dealer = Dealer()

    def play(self):
        print("Welcome to Blackjack!")

        # 初期の2枚のカードを引く
        for _ in range(2):
            self.player.hand.add_card(self.deck.draw_card())
            self.dealer.hand.add_card(self.deck.draw_card())

        # プレイヤーとディーラーの手札を表示
        print("Your hand:")
        self.player.show_hand()
        print("\nDealer's hand:")
        self.dealer.show_hand()

        # プレイヤーのターン
        while True:
            choice = input("Do you want to 'hit' or 'stand'? ").lower()

            if choice == 'hit':
                self.player.hand.add_card(self.deck.draw_card())
                print("\nYour hand:")
                self.player.show_hand()
                if self.player.hand.calculate_score() > 21:
                    print("Bust! You went over 21. You lose.")
                    return
            elif choice == 'stand':
                break
            else:
                print("Invalid input. Please enter 'hit' or 'stand'.")

        # ディーラーのターン
        print("\nDealer's turn:")
        while self.dealer.hand.calculate_score() < 17:
            self.dealer.hand.add_card(self.deck.draw_card())
            self.dealer.show_hand()

        # 勝敗判定
        player_score = self.player.hand.calculate_score()
        dealer_score = self.dealer.hand.calculate_score()

        print("\nYour final hand:")
        self.player.show_hand()
        print(f"Your final score: {player_score}")

        print("\nDealer's final hand:")
        self.dealer.show_hand()
        print(f"Dealer's final score: {dealer_score}")

        if dealer_score > 21 or (player_score <= 21 and player_score > dealer_score):
            print("You win!")
        elif player_score == dealer_score:
            print("It's a draw.")
        else:
            print("You lose.")

    def play_again(self):
        choice = input("Do you want to play again? (yes/no): ").lower()
        return choice == 'yes'

if __name__ == "__main__":
    while True:
        game = BlackjackGame()
        game.play()

        if not game.play_again():
            print("Thanks for playing. Goodbye!")
            break
