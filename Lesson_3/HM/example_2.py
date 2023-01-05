#напишите программу, которая найдет произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследий и т.д.
import os
clear = lambda: os.system('cls')
clear()
import random

def new_list (num):
    list = []
    for i in range(num):
        list.append(random.randint(1,100))
    return list
    
def proizvedenie (list):
    new_list = []
    length = len(list)
    for i in range(length // 2):
        new_list.append(list[i] * list[length-i-1])
    if length % 2:
        new_list.append(list[length // 2]) 
    return new_list       


user_num = int(input('Введите число: '))
user_list = new_list(user_num)
print(user_list)
list_proiz = proizvedenie(user_list)
print (list_proiz)