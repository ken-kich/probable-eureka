class Player:
    # Playerクラス: プレイヤー（ユーザーとコンピュータ）を表す
    def __init__(self, hands, name):
        self.hands = hands  # じゃんけんの手の辞書（例：'0': 'グー'）
        self.name = name    # プレイヤー名
        self.hand = ''      # 選択された手

    def random_out(self):
        # コンピュータのランダムな手の選択
        self.hand = random.choice(list(self.hands.keys()))

    def select(self):
        # ユーザーによる手の選択。無効な入力があれば再入力を求める
        print("選択肢: '0' = グー, '2' = チョキ, '5' = パー, 'q' = ゲーム終了")
        while True:
            self.hand = input("じゃんけん ⇒ ")
            if self.hand in self.hands.keys() or self.hand == 'q':
                break
            else:
                print("想定外な手です。'0', '2', '5', 'q'の中から入力してください。")

    def show(self):
        # 選択された手の表示
        hand_name = self.hands.get(self.hand, '')
        print(f"{self.name}の手：{hand_name}")

    def win_lose_check(self, enemy_hand):
        # 勝敗の判定。自分の手と敵の手を比較
        if (self.hand, enemy_hand) in [('0', '2'), ('2', '5'), ('5', '0')]:
            return True
        return False

def main():
    # メイン関数: ゲームの進行管理
    hand_dict = {"0": "グー", "2": "チョキ", "5": "パー"}
    player = Player(hand_dict, "プレイヤー")  # プレイヤーインスタンスの生成
    computer = Player(hand_dict, "コンピュータ")  # コンピュータインスタンスの生成

    player_win_count = 0  # プレイヤーの勝利数カウント
    print("じゃんけんゲーム Game Start!")

    while player_win_count < 3:
        # プレイヤーが3回勝つまでゲームを続行
        print(f"現在の勝利数: {player_win_count}")
        player.select()
        if player.hand == 'q':
            print("強制終了します")
            break

        computer.random_out()
        player.show()
        computer.show()

        if player.hand in hand_dict:
            # 勝敗の判定
            if player.win_lose_check(computer.hand):
                print("You Win!!!")
                player_win_count += 1
            elif player.hand == computer.hand:
                print("Draw!!!")
            else:
                print("You Lose!!!")

    if player_win_count >= 3:
        print("ゲームに勝利しました！")

if __name__ == "__main__":
    main()

#push test
