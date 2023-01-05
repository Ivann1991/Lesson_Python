#Задайте список, состоящий из произвольных чисел, количество задает пользователь. Напишите прорамму, определяющую присутствует ли в заданом списке число, полученное от пользователя.   
import os
clear = lambda: os.system('cls')
clear()

from random import sample
def find_number (amount, user_number):
    new_list = sample(range(1, (amount+1)*2), k=amount)
    print(new_list)
    if user_number in new_list:
        return "yes"
    return "no"

some_number = find_number (int(input('Enter amout - ')),
                        int(input("Enter the desired number - ")))   
print (some_number)                             