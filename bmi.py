#!/usr/bin/python3
＃BMI計算プログラム
height = float(input('身長をm単位で入力して下さい> '))
weight = float(input('体重をkg単位で入力して下さい> '))
bmi = weight/height**2
print('BMI = ',bmi,sep=' ')
if bmi < 18.5 :
    print('あなたは「'+'痩せすぎ'+'」です。')
elif bmi >= 18.5 and bmi < 25.0 :
    print('あなたは「'+'標準'+'」です。')
elif bmi >= 25.0 and bmi < 30.0 :
    print('あなたは「'+'肥満'+'」です。')
else :
    print('あなたは「'+'高度肥満'+'」です。')
