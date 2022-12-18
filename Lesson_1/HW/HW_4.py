#напишите программу которая по заданному номеру четверти, показывает возможный диапозон координат точек этой четверти.
print ('введи номер четверти')
Quarter = int (input())
if Quarter == 1:
    print ('x > 0 and y > 0')
elif Quarter == 2:
    print ('x < 0 and y > 0')    
elif Quarter == 3:
    print ('x < 0 and y < 0')  
elif Quarter == 4:
    print ('x > 0 and y < 0') 
else:
    print ('ошибка ввода номера четверти')           