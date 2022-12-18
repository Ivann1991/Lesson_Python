#Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
print ('Введи целое число от от 1 до 7')
userNum = int (input())
if 1 <= userNum <=5:
    print ('workday')
elif userNum == 6 or userNum == 7:
    print ('weekend')
else:
    print ("it's not a day of the week!")
