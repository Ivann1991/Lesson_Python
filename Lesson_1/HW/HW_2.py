#Напишите программу для проверки ложности утверждения (W and Z) or not Y or (not X== not W)
print ('x y z w')
for x in range (2):
    for y in range (2):
        for z in range (2):
            for w in range (2):
                if not ((w and z) or not y or (not x == (not w))):
                    print (x, y, z, w)