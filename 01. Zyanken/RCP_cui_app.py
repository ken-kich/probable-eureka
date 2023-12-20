import random 

#じゃんけんの選択肢の辞書
hand_dict = {
    "0": "グー",
    "2": "チョキ",
    "5": "パー"
}
#じゃんけんの選択肢のリスト
input_dict = list(hand_dict.keys())
input_dict.append("q")

#Playerクラス
class Player:
    def __init__(self, hands="", name=""):
        self.hands = hands
        self.name = name
    #プレイヤーの手をランダムに決めるメソッド
    def random_select(self):
        self.hand = random.choice(list(hand_dict.keys()))
        return self.hand
    #プレイヤーの手を決めるメソッド
    def select(self):
        tmp = ""
        while True:
            if tmp == "":
                tmp = input(f"じゃんけん⇒")
            elif tmp == "q":
                print("強制終了します")
                break
            elif tmp in input_dict:
                self.hand = tmp
                break
            else:
                tmp = input(f"想定外の手です。{input_dict}の中から入力してください⇒")
        return self.hand
    #プレイヤー名と手を表示するメソッド
    def show(self):
        print(f"{self.name}の手：{hand_dict[str(self.hands)]}")
    #勝敗を決めるメソッド
    def win_lose_check(self, enemy_hand):
        if self.hands == enemy_hand:
            print("Draw!!!")
            return False
        elif (self.hands, enemy_hand) in [("0","2"),("2","5"),("5","0")]:
            print("You Win!!!")
            return True
        else:
            print("You Lose!!!")
            return False
        

#ゲームスタート
print("Game Start")
print("これはじゃんけんゲームです。ルールを説明します。\n[グー]  のときは[0]\n[チョキ]のときは[2]\n[パー]  のときは[5]\n[終了]  のときは[q]を入力してください。\nコンピュータに合計3回勝利すれば終了します。")

#自分のインスタンスを作成
player = Player("","プレイヤー")
#対戦相手のインスタンスを作成
enemy_player = Player("","コンピュータ")
#勝利回数を数える
count = 0
#3回勝利するまでゲームをする
while True:
    if count >=3:
        break
    player.hands = player.select()
    player.show()

    enemy_player.hands = enemy_player.random_select()
    enemy_player.show()
    
    if player.win_lose_check(enemy_player.hands):
        count += 1
    print(f"勝利回数：{count}回")
#終了
print("コンピュータに合計3回勝利しました。終了します。")