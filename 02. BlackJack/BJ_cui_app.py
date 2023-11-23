import random

# カードクラス
class Card:
    def __init__(self, suit, value):
        self.suit = suit  # カードのスート（スペード、クラブ、ダイヤ、ハート）
        self.value = value  # カードの値（2〜10、J、Q、K、A）

    def __repr__(self):
        return f"{self.value}の{self.suit}"  # カードの文字列表現（例：5のハート）

# デッキクラス
class Deck:
    def __init__(self):
        self.cards = []  # デッキ内のカードを保持するリスト
        self.build()  # デッキを構築する

    def build(self):
        # 52枚のカードを生成し、デッキに追加する
        for suit in ["スペード", "クラブ", "ダイヤ", "ハート"]:
            for value in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]:
                self.cards.append(Card(suit, value))
        self.shuffle()  # カードをシャッフルする

    def shuffle(self):
        random.shuffle(self.cards)  # デッキ内のカードをランダムに並び替える

    def draw_card(self):
        return self.cards.pop()  # デッキの一番上のカードを取り出す

# class Deck:
#     def __init__(self):
#         self.cards = [Card(suit, value) for suit in ["スペード", "クラブ", "ダイヤ", "ハート"] 
#                       for value in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]]
#         random.shuffle(self.cards)

#     def draw_card(self):
#         return self.cards.pop()

# プレイヤークラス
class Player:
    def __init__(self):
        self.hand = []  # プレイヤーの手札を初期化

    def draw(self, deck):
        self.hand.append(deck.draw_card()) # デッキからカードを引き、手札に加える

    def show_hand(self):
        return ', '.join(str(card) for card in self.hand)  # 手札を文字列で表示する

    def calculate_hand(self):
        # 手札の合計値を計算する
        total, ace_count = 0, 0
        for card in self.hand:
            if card.value in ["J", "Q", "K"]:
                total += 10  # 絵札は10として計算
            elif card.value == "A":
                ace_count += 1
                total += 11  # エースは11として計算（必要に応じて1に変更）
            else:
                total += int(card.value)
        # 手札が21を超える場合、Aを1として再計算する
        while total > 21 and ace_count:
            total -= 10
            ace_count -= 1
        return total

# ディーラークラス（プレイヤークラスを継承）
class Dealer(Player):
    def show_hand(self, show_all=False):
        # ディーラーの手札を表示する（最初のカードは隠すオプションあり）
        if show_all:
            return super().show_hand()
        else:
            return str(self.hand[0]) + ", 隠されたカード" if self.hand else ""

# ゲームクラス
class BlackjackGame:
    def __init__(self):
        self.deck = Deck()  # 新しいデッキを生成
        self.player = Player()  # プレイヤーのインスタンスを生成
        self.dealer = Dealer()  # ディーラーのインスタンスを生成
    
    def play(self):
        # ゲーム開始前に手札とデッキをリセット
        self.player.hand = []
        self.dealer.hand = []
        self.deck = Deck()  # 新しいデッキを生成

        # プレイヤーとディーラーがそれぞれ2枚ずつカードを引く
        for _ in range(2):
            self.player.draw(self.deck) 
            self.dealer.draw(self.deck) 
            
        # プレイヤーのターン処理
        player_busted = self.player_turn()

        # ディーラーのターン処理
        if not player_busted:
            self.dealer_turn()
            self.determine_winner()

        return self.play_again()

    def player_turn(self):
        # プレイヤーのターンを処理
        while True:
            print(f"あなたの手札: {self.player.show_hand()} [合計: {self.player.calculate_hand()}]")
            print(f"ディーラーの手札: {self.dealer.show_hand()} [合計: ？]")

            choice = self.get_choice("ヒットしますか、スタンドしますか？ ( hit / stand ): ", ["hit", "stand"])
            
            if choice == "hit":
                self.player.draw(self.deck)
                player_total = self.player.calculate_hand()
                # プレイヤーの手札の合計を確認
                if player_total == 21:
                    print(f"あなたの手札: {self.player.show_hand()} [合計: {player_total}]\n  BLACK JACK!! あなたの勝ちです!!")
                    return True
                elif player_total > 21:
                    print(f"あなたの手札: {self.player.show_hand()} [合計: {player_total}]\n  バスト!! あなたの負けです。")
                    return True
            else:
                break

        return False

  
    def dealer_turn(self):
        # ディーラーのターンを処理
        while self.dealer.calculate_hand() < 17:
            self.dealer.draw(self.deck) # ディーラーが17未満の場合はカードを引き続ける

    def determine_winner(self):
        # 勝敗を決定する
        player_total = self.player.calculate_hand()
        dealer_total = self.dealer.calculate_hand()
        # 最終的な手札と合計を表示
        print(f"あなたの手札: {self.player.show_hand()} [合計: {player_total}]")
        print(f"ディーラーの手札: {self.dealer.show_hand(show_all=True)} [合計: {dealer_total}]")

        # 勝敗のロジック
        if dealer_total > 21 or player_total > dealer_total:
            print(" あなたの勝ちです！")
        elif player_total < dealer_total:
            print(" ディーラーの勝ちです。")
        else:
            print(" 引き分けです。")

    def play_again(self):
        # ゲームの再プレイを尋ねる
        return self.get_choice("もう一度プレイしますか？ ( yes / no ): ", ["yes", "no"]) == "yes"

    def get_choice(self, prompt, choices):
        while True:
            choice = input(prompt).lower()
            if choice in choices:
                return choice
            print(f'"{choices[0]}" または "{choices[1]}" から選択してください。')

# メインフロー
def main():
    # ゲームインスタンスを生成し、プレイヤーが再プレイを望む限りゲームを続ける
    game = BlackjackGame() 
    while game.play():
        pass

if __name__ == "__main__":
    main()
