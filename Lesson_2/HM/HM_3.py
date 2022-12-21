#Задайте список из N чисел, заполенный по формуле (1+1/n)**n и вывидите на экран их сумму
import os
clear = lambda: os.system('cls')
clear()
num_List = []
n = int(input('введи число N '))
for i in range(1, n+1):
    num_List.append ((1+1/i)**i)
print (num_List)  
a = (sum(num_List))
print (f'сумма элементов списка равна -> {a:.3f}')
