#Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов последовательности в том же порядке.
import os
clear = lambda: os.system('cls')
clear()
import random
def random_list (num):
    list = []
    for i in range(num):
        list.append(random.randint(1,8))
    return list

def result_list (list_2):
   new_list=[] 
   for i in list_2: 
    if list_2.count(i) == 1: 
        new_list.append(i)
   return new_list     

user_num = int(input('Введите целое положительное число: '))
user_list = random_list(user_num)
print (f'сгенерированный список {user_list}')
res_list = result_list(user_list)
print(res_list)