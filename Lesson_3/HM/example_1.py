#Задайте список, состоящий из произвольных чисел, количество задает пользователь.
#Напишите программу, которая найдет сумму элементов списка, стоящий на нечетных позициях (не индексах).

import os
clear = lambda: os.system('cls')
clear()
import random

def new_list (num):
    list = []
    for i in range(num):
        list.append(random.randint(1,100))
    return list        

def sum (list):
    sum = 0
    for i in range(0, len(list),2):
        sum = sum + list[i]
    return sum    

user_num = int(input('Введите число: '))
user_list = new_list(user_num)
sum_position = sum(user_list)
print(user_list)
print(sum_position)
