#じゃんけんプログラム
import random #乱数設定
yours = int(input('あなたは？(0:グー, 1:チョキ, 2:パー)> '))
comp = random.randint(0,2)
if comp == 0 : # グー
    compstr = 'わたしはグー！'
    if yours == 0 :
        yourstr = 'あなたもグー！'
        result = 'あいこです！'
    elif yours == 1 :
        yourstr = 'あなたはチョキ！'
        result = 'あなたの負けです！'
    else :
        yourstr = 'あなたはパー！'
        result = 'あなたの勝ちです！'
elif comp == 1 : # チョキ
    compstr = 'わたしはチョキ！'
    if yours == 0 :
        yourstr = 'あなたはグー！'
        result = 'あなたの勝ちです！'
    elif yours == 1 :
        yourstr = 'あなたもチョキ！'
        result = 'あいこです！'
    else :
        yourstr = 'あなたはパー！'
        result = 'あなたの負けです！'
else : # パー
    compstr = 'わたしはパー！'
    if yours == 0 :
        yourstr = 'あなたはグー！'
        result = 'あなたの負けです！'
    elif yours == 1 :
        yourstr = 'あなたはチョキ！'
        result = 'あなたの勝ちです！'
    else :
        yourstr = 'あなたもパー！'
        result = 'あいこです！'
print(compstr+yourstr+result)
