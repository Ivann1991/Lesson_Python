#Задайте натуральное число N. Напишите программу, которая составит список простых множитедей числа N.
import os
clear = lambda: os.system('cls')
clear() 
user_num = int(input("введи любое целое число "))
def factors (user_num):
    new_list = []
    a = 2
    while (a <= user_num):
        if (user_num % a) == 0:
            new_list.append(a)
            user_num = user_num/a
        else:
            a = a+1
    return new_list

result = factors(user_num)
print(result)
