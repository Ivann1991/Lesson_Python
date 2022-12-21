#Напишите программу, которая принимает число N и выдает набор произведений чисел от 1 до N в виде списка....
import os
clear = lambda: os.system('cls')
clear()
n = int(input('введи целое число '))
a = 1
for i in range(1, n+1):
    print (a*i, end=', ')
    a = a*i
  
    
