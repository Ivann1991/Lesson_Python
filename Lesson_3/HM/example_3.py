#Напишите программу, которая будет преобразовывать десятичное число в двоичное.
import os
clear = lambda: os.system('cls')
clear()   
s = ""
n = int(input("Введите десятичное число для преобразовывания в двоичное:\n"))
while n != 0:
    s = str(n % 2) + s
    n //= 2
print(s)    


#def conv_bin(num: int):
#    list_nums = []
#    while num > 0:
#        list_nums.insert(0, num % 2)
#        num //= 2
#    print(*list_nums, sep="")

#conv_bin(int(input())) 