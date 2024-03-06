import random


class Player():

    def __init__(self, hands, name):
        self.hands = hands
        self.name = name
        self.hand = None
        self.score = 0

    def random_select(self):
        self.hand = random.choice(list(self.hands.keys()))

    def get_user_input(self, valid_choices):
        options = ', '.join([
            f'{key}:{value}'
            for key, value in self.hands.items()
        ])
        while True:
            print(f"{self.name}さん、じゃんけん（{options}, q)を選んでください: ")
            choice = input()
            if choice in valid_choices:
                return choice
            elif choice == 'q':
                print("強制終了します")
                exit()
            print(f"想定外の手です。{', '.join(list(self.hands.keys()))}の中から入力してください.")

    def show_hand(self):
        print(f"{self.name}の手: {self.hands[self.hand]}")

    def win_lose_check(self, opponent_hand):
        if self.hand == opponent_hand:
            print("Draw!!!")
        elif (self.hand == '0' and opponent_hand == '2') or \
             (self.hand == '2' and opponent_hand == '5') or \
             (self.hand == '5' and opponent_hand == '0'):
            print("You Win!!!")
            self.score += 1
        else:
            print("You Lose!!!")


hand_dict = {"0": "グー", "2": "チョキ", "5": "パー"}


def main():
    print("Game Start")
    player = Player(hand_dict, "Player")
    computer = Player(hand_dict, "Computer")

    while player.score < 3:
        player.hand = player.get_user_input(list(hand_dict.keys()) + ['q'])

        if player.hand == 'q':
            print("強制終了します")
            break

        player.show_hand()
        computer.random_select()
        computer.show_hand()
        player.win_lose_check(computer.hand)
        print(f"Your score: {player.score}\n")


if __name__ == "__main__":
    main()
