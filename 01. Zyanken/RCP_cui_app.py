import random

hand_dict = {
    "0": "グー",
    "2": "チョキ",
    "5": "パー"
}


winning_hands = {
    'グー': 'チョキ',
    'チョキ': 'パー',
    'パー': 'グー'
}

print('Game Start!')


class Player:
    def __init__(self, hands, name):
        self.hand_dict = hands
        self.name = name
        self.hand = None

    def random_select(self):
        self.hand = random.choice(list(self.hand_dict.values()))

    def select(self):
        while True:
            player_input = input("Playerの手を入力してください。{0:グー, 2:チョキ, 5:パー,q:終了\
                じゃんけん⇒")
            if player_input in ['0', '2', '5']:
                self.hand = self.hand_dict[player_input]
                break
            elif player_input == 'q':
                print("強制終了します。")
                break
            else:
                print("想定外の手です。{}の中から入力してください。")

    def show(self):
        if self.hand is not None:
            print(f"{self.name}の手: {self.hand}")
        else:
            print(f"{self.name}はまだ手を選んでいません。")

    def win_lose_check(self, enemy_hand):
        if self.hand == "グー" and enemy_hand == "チョキ":
            return True
        elif self.hand == "チョキ" and enemy_hand == "パー":
            return True
        elif self.hand == "パー" and enemy_hand == "グー":
            return True
        else:
            return False

    def play_game(self):
        main_player_wins = 0
        while main_player_wins < 3:
            self.select()

            computer_hand = random.choice(['0', '2', '5'])

            print(f"CPの手: {self.hand_dict[computer_hand]}")

            if self.hand_dict[computer_hand] in winning_hands[self.hand]:
                print("You Win!!!")
                main_player_wins += 1
            elif self.hand == self.hand_dict[computer_hand]:
                print("Draw!!!")
            else:
                print("You Lose!!!")

            print(f"YOUの勝利数: {main_player_wins}")

            if self.hand == 'q':
                print("ゲーム終了")
                break
            elif main_player_wins >= 3:
                print("ゲーム終了")
                break


player1 = Player(hand_dict, 'YOU')

player1.play_game()
