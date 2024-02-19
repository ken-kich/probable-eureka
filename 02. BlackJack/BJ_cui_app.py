import random

class Player:
    def __init__(self, hands, name):
        self.hands = hands
        self.name = name
        self.hand = ""

    def random_select(self):
        self.hand = random.choice(list(self.hands.keys()))

    def select(self):
        while True:
            print("**じゃんけん ⇒ ", end="")
            choice = input()
            if choice == "q":
                print("**強制終了します")
                exit()
            elif choice in self.hands.keys():
                self.hand = choice
                break
            else:
                print("**想定外の手です。{}の中から入力してください。".format(list(self.hands.keys())))

    def show(self):
        print("**{}の手：{}".format(self.name, self.hands[self.hand]))

    def win_lose_check(self, enemy_hand):
        if (self.hand == "0" and enemy_hand == "2") or \
           (self.hand == "2" and enemy_hand == "5") or \
           (self.hand == "5" and enemy_hand == "0"):
            return True
        else:
            return False

def main():
    print("Game Start")
    hands_dict = {
        "0": "グー",
        "2": "チョキ",
        "5": "パー"
    }
    
    player = Player(hands_dict, "Player")
    opponent = Player(hands_dict, "Opponent")

    while True:
        player.select()
        opponent.random_select()
        
        player.show()
        opponent.show()
        
        if player.win_lose_check(opponent.hand):
            print("**You Win!!!")
            break
        else:
            print("**You Lose!!!")

if __name__ == "__main__":
    main()
