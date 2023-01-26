#Вычислить число с заданной точностью d
import os
clear = lambda: os.system('cls')
clear() 
from decimal import Decimal
user_num = input("введи любое вещественное число ")
accuracy = input("введи точность, например: 0.001 ")
a = Decimal(str(user_num)).quantize(Decimal(str(accuracy)))
print(a)
