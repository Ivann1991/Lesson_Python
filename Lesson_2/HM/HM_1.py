#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
import os
clear = lambda: os.system('cls')
clear()
userNum = str(input('введи вещественное число '))
num = len(userNum)
print (num)
Num = float(userNum) * 10 ** (num-2)
Result = 0
while Num > 0:
    Result = Num % 10 + Result
    Num = Num//10
print (int(Result))  

