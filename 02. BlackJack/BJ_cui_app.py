import random


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value}の{self.suit}"


class Deck:
    def __init__(self):
        self.cards = []

    def build(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J',
                  'Q', 'K']
        for suit in suits:
            for value in values:
                card = Card(suit, value)
                self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop()


class Player:
    def __init__(self):
        self.hand = []

    def draw_card(self, deck):
        self.hand.append(deck.draw_card())

    def show_hand(self):
        print("プレイヤーの手札:")
        for card in self.hand:
            print(card)

    def calculate_total(self):
        total = 0
        for card in self.hand:
            if card.value.isdigit():
                total += int(card.value)
            elif card.value in ['J', 'Q', 'K']:
                total += 10
            else:
                total += 11
        for card in self.hand:
            if card.value == 'A' and total > 21:
                total -= 10
        return total


class Dealer(Player):
    def show_initial_hand(self):
        print("ディーラーのカード:")
        print(self.hand[0])
        print("1枚のカードは伏せられています")


class Game:
    def __init__(self):
        self.deck = Deck()
        self.player = Player()
        self.dealer = Dealer()

    def play(self):
        while True:
            print("新しいゲームを始めます。")
            self.deck.build()
            self.deck.shuffle()
            self.player.hand.clear()
            self.dealer.hand.clear()
            for _ in range(2):
                self.player.draw_card(self.deck)
                self.dealer.draw_card(self.deck)
            print("プレイヤーの手札:")
            self.player.show_hand()
            self.dealer.show_initial_hand()
            while self.player.calculate_total() < 21:
                choice = input("別のカードを引きますか? はい='y'、いいえ='n': ")
                if choice.lower() == 'y':
                    self.player.draw_card(self.deck)
                    print("プレイヤーの手札:")
                    self.player.show_hand()
                else:
                    break

            player_total = self.player.calculate_total()

            if player_total > 21:
                print("バースト！ディーラーの勝ち")
                self.end_game()

            print("ディーラーの手札を表示:")
            self.dealer.show_hand()
            while self.dealer.calculate_total() < 17:
                self.dealer.draw_card(self.deck)
                print("ディーラーがカードを引きました:")
                self.dealer.show_hand()

            dealer_total = self.dealer.calculate_total()

            if dealer_total > 21:
                print("ディーラーがバーストしました。プレイヤーの勝利！")
            elif dealer_total > player_total:
                print("ディーラーの勝利")
            elif dealer_total < player_total:
                print("プレイヤーの勝利！")
            else:
                print("引き分け")

            self.end_game()

    def end_game(self):
        choice = input("もう一度プレイしますか？ はい='y'、いいえ='n':")
        if choice.lower() == 'n':
            print("ゲームを終了します。")
            exit()


if __name__ == "__main__":
    game = Game()
    game.play()
