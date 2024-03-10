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
        # スートと値のリストを使ってデッキを構築
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
                  'J', 'Q', 'K', 'A']
        for suit in suits:
            for value in values:
                self.cards.append(Card(suit, value))

    def shuffle(self):
        # デッキをシャッフル
        random.shuffle(self.cards)

    def draw_card(self):
        # デッキからカードを引く
        if len(self.cards) == 0:
            print("The deck is empty!")
            return None
        return self.cards.pop()


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0

    def add_card(self, card):
        # 手札にカードを追加し、手札の合計値を計算
        self.cards.append(card)
        if card.value.isdigit():
            self.value += int(card.value)
        elif card.value in ['J', 'Q', 'K']:
            self.value += 10
        else:  # A
            self.value += 11

        # Aを1として扱うかチェック
        num_aces = sum(1 for card in self.cards if card.value == 'A')
        while num_aces > 0 and self.value > 21:
            self.value -= 10
            num_aces -= 1

    def display(self):
        # 手札を表示
        for card in self.cards:
            print(f"{card.value} of {card.suit}")
        print(f"Total value: {self.value}")


class Player:
    def __init__(self):
        self.hand = Hand()


class Dealer(Player):
    def show_hand(self):
        # ディーラーの最初のカードのみ表示
        print("Dealer's Hand:")
        print(f'''First card: {self.hand.cards[0].value} of
                {self.hand.cards[0].suit}''')


class BlackjackGame:
    def __init__(self):
        # ゲームの初期化
        self.deck = Deck()
        self.player = Player()
        self.dealer = Dealer()

    def deal_initial_cards(self):
        # 初期カードの配布
        for _ in range(2):
            self.player.hand.add_card(self.deck.draw_card())
            self.dealer.hand.add_card(self.deck.draw_card())

    def player_turn(self):
        # プレイヤーのターン
        while True:
            self.player.hand.display()
            action = input("Do you want to hit or stand? (h/s): ").lower()
            if action == 'h':
                drawn_card = self.deck.draw_card()
                print(f"You drew: {drawn_card.value} of {drawn_card.suit}")
                self.player.hand.add_card(drawn_card)
            if self.player.hand.value > 21:
                print("Bust! You lose.")
                print("The card that caused the bust:")
                print(f"{drawn_card.value} of {drawn_card.suit}")
                return
            elif action == 's':
                break
            else:
                print("Invalid input!")

    def dealer_turn(self):
        # ディーラーのターン
        while self.dealer.hand.value < 17:
            drawn_card = self.deck.draw_card()
            print(f"Dealer drew: {drawn_card.value} of {drawn_card.suit}")
            self.dealer.hand.add_card(drawn_card)
        self.dealer.hand.display()

    def determine_winner(self):
        # 勝者の決定
        if self.player.hand.value > 21:
            print("Bust! You lose.")
        elif self.dealer.hand.value > 21:
            print("Dealer busts! You win.")
        elif self.player.hand.value > self.dealer.hand.value:
            print("You win!")
        elif self.player.hand.value < self.dealer.hand.value:
            print("You lose.")
        else:
            print("It's a tie.")

    def play_game(self):
        # ゲームのメインループ
        print("Let's play Blackjack!")
        while True:
            self.deck.shuffle()
            self.deal_initial_cards()
            self.dealer.show_hand()
            self.player_turn()
            if self.player.hand.value <= 21:
                self.dealer_turn()
                self.determine_winner()
            if not self.play_again():
                break

    def play_again(self):
        # 再プレイの確認
        while True:
            play_again = input("Do you want to play again? (y/n): ").lower()
            if play_again == 'y':
                # 再プレイ時にデッキと手札を再度初期化
                self.deck = Deck()
                self.player = Player()
                self.dealer = Dealer()
                return True
            elif play_again == 'n':
                return False
            else:
                print("Invalid input! Please enter 'y' or 'n'.")


if __name__ == "__main__":
    game = BlackjackGame()
    game.play_game()
