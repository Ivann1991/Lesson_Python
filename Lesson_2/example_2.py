#Создать список, длины n, значения формируются по формуле 3к+1, где к принимает значние от 1 до n включительно.
import os
clear = lambda: os.system('cls')
clear()
num_List = []
n = int(input('введи число N '))
for k in range(1, n+1):
    num_List.append (3*k+1)
print (num_List)    