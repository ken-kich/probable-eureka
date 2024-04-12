import random

hand_dict = {
    "0": "グー",
    "2": "チョキ",
    "5": "パー"
}


class Player:
    def _init_(self, hands, name):
        self.hand_dict = hands
        self.name = name
        self.hand = None

    def random_select(self):
        self.hand = random.choice(hand_dict)

    def select(self):
        while True:
            player_input = input("Playerの手を入力してください。(0:グー, 2:チョキ, 5:パー)")
            if player_input in ['0', '2', '5']:
                if player_input == '0':
                    self.hand = 'グー'
                elif player_input == '2':
                    self.hand = 'チョキ'
                else:
                    self.hand = 'パー'
                break
            elif player_input == 'q':
                print("ゲームを終了します。")
                break
            else:
                print("入力が不正です。再度入力してください。")

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

    def increment_win_count(self):
        self.win_count += 1


player1 = Player("Player")

player1.select(Player.hand)
player1.show()

player2 = Player("CP")

player2.select()
player2.show()

while player2.win_count < 3:
    player1.select_hand()
    player2.hand = random.choice()
