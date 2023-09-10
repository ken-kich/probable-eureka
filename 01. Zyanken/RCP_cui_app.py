import random
import sys
class Player:
#必ず使用する（コンストラクタ）
  def __init__(self,hands=None,name=None):
    
    self.hands = hands
    self.name = name
    print('Game Start')
#4相手の手ランダム
  def random_out(self):
    hand_dict = {
    "0": "グー",
    "2": "チョキ",
    "5": "パー"}
    self.hand_c = random.choice(list(hand_dict.values()))

#3プレイヤーの手
  def select(self):
    hand_dict = {
    "0": "グー",
    "2": "チョキ",
    "5": "パー"}
    
    
    hands = input('入力値:')#文字型
    if '0' == hands:
     self.hand = hands
    elif '2' == hands:
      self.hand = hands
    elif '5' == hands:
      self.hand = hands
    elif 'q' == hands:
      self.hand = hands 
      print('強制終了します')
      sys.exit()
    else:
     print('再入力してください')

    self.hand_p = hand_dict[self.hand]
#5メゾット
  def show(self):
    self.name_p = input('プレイヤー名入力してください')
    print (self.name_p+':'+ self.hand_p)
    print(self.hand_c)
 #6メゾット勝利判定 
  def win_lose_check(self,enemy_hand=None):
     
    
     self.enemy_hand = enemy_hand
     if self.hand_p == self.hand_c:
      print("Draw!!!")
     elif self.hand_p > self.hand_c:
      print("You Win!!!")
     else:
      print("You Lose!!!")
      
     
     
        
    
#2 メインフロー5
while True: #(無限ループ)
#インスタンス生成 
 game_play =  Player()

#3メゾット呼び出し プレイヤーの手決定
 game_play.select()

#4メゾット呼び出し 相手の手ランダム決定
 game_play.random_out()

#5メゾットそれぞれ呼び出し
 game_play.show()

#6メゾット勝利判定
 game_play.win_lose_check()