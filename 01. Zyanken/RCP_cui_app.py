import random

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def select(self):
        while True:
            try:
                hand = input(f"{self.name}の手を選択してください（0: グー, 2: チョキ, 5: パー, q: 終了）: ")
                if hand == "q":
                    print("強制終了します")
                    exit()
                elif hand in ["0", "2", "5"]:
                    return int(hand)
                else:
                    raise ValueError
            except ValueError:
                print("想定外の手です。0, 2, 5, qの中から入力してください。")

    def random_select(self):
        return random.choice([0, 2, 5])

    def show(self, hand):
        hand_dict = {
            0: "グー",
            2: "チョキ",
            5: "パー"
        }
        print(f"{self.name}の手：{hand_dict[hand]}")

    def win_lose_check(self, my_hand, opponent_hand):
        if my_hand == opponent_hand:
            print("Draw!!!")
        elif (my_hand - opponent_hand) % 3 == 1:
            print("You Win!!!")
            self.score += 1
        else:
            print("You Lose!!!")

    def play(self):
        while self.score < 3:
            print("Game Start")
            player_hand = self.select()
            opponent_hand = self.random_select()
            self.show(player_hand)
            self.show(opponent_hand)
            self.win_lose_check(player_hand, opponent_hand)
        print(f"{self.name}の勝ち数：{self.score}")

# メイン処理
if __name__ == "__main__":
    player = Player("Player")
    player.play()
